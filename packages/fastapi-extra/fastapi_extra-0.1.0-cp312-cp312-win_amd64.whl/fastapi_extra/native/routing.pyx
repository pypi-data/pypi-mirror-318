__author__ = "ziyan.yin"
__describe__ = ""

cimport cython

from typing import MutableMapping

from basex.common import strings
from fastapi import APIRouter
from starlette import _utils as starlette_utils
from starlette.datastructures import URL
from starlette.responses import RedirectResponse


def get_route_path(scope: MutableMapping) -> str:
    root_path = scope.get("root_path", "")
    route_path = scope["path"].removeprefix(root_path)
    return route_path

starlette_utils.get_route_path = get_route_path


@cython.no_gc
cdef class RouteNode:
    cdef readonly:
        list routes
        dict leaves
        unicode prefix

    def __cinit__(self, prefix):
        self.prefix = prefix
        self.routes = []
        self.leaves = {}

    def add_route(self, route):
        self.routes.append(route)

    def add_leaf(self, node):
        if node.prefix in self.leaves:
            raise KeyError(node.prefix)
        else:
            self.leaves[node.prefix] = node


cdef list change_path_to_ranks(unicode path):
    ranks = path.lstrip('/').split('/')
    return ranks


cdef void add_route(unicode path, object root, object route):
    current_node = root
    ranks = change_path_to_ranks(path)
    for r in ranks:
        if r.find('{') >= 0 and r.find('}') > 0:
            break
        if not r:
            continue
        if r in current_node.leaves:
            current_node = current_node.leaves[r]
        else:
            next_node = RouteNode.__new__(RouteNode, r)
            current_node.add_leaf(next_node)
            current_node = next_node
    current_node.add_route(route)


cdef list find_routes(unicode path, RouteNode root):
    current_node = root
    ranks = change_path_to_ranks(path)

    routes = []
    routes += current_node.routes
    for r in ranks:
        if not r:
            continue
        if r in current_node.leaves:
            current_node = current_node.leaves[r]
            routes += current_node.routes
            continue
        break

    routes.reverse()
    return routes


_super_router = APIRouter


class BaseRouter(_super_router):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root_node = RouteNode.__new__(RouteNode, '')
        for route in self.routes:
            add_route(route.path, self.root_node, route)

    def add_route(self, path, endpoint, **kwargs):
        super().add_route(path, endpoint, **kwargs)
        add_route(self.routes[-1].path, self.root_node, self.routes[-1])

    def add_api_route(self, path, endpoint, **kwargs):
        super().add_api_route(path)
        add_route(self.routes[-1].path, self.root_node, self.routes[-1])

    def add_websocket_route(self, path, endpoint, **kwargs):
        super().add_websocket_route(path, endpoint, **kwargs)
        add_route(self.routes[-1].path, self.root_node, self.routes[-1])

    def add_api_websocket_route(self, path, endpoint, **kwargs):
        super().add_api_websocket_route(path, endpoint, **kwargs)
        add_route(self.routes[-1].path, self.root_node, self.routes[-1])

    def mount(self, path, app, **kwargs):
        super().mount(path, app, **kwargs)
        add_route(self.routes[-1].path, self.root_node, self.routes[-1])

    async def __call__(self, scope, receive, send):
        assert scope["type"] in ("http", "websocket", "lifespan")

        if "router" not in scope:
            scope["router"] = self

        if scope["type"] == "lifespan":
            await self.lifespan(scope, receive, send)
            return

        partial = None

        route_path = get_route_path(scope)
        matched_routes = find_routes(route_path, self.root_node)

        for route in matched_routes:
            match, child_scope = route.matches(scope)
            if match.value == 2:
                scope.update(child_scope)
                await route.handle(scope, receive, send)
                return
            elif match.value == 1 and partial is None:
                partial = route
                partial_scope = child_scope

        if partial is not None:
            scope.update(partial_scope)
            await partial.handle(scope, receive, send)
            return


        if scope["type"] == "http" and self.redirect_slashes and route_path != "/":
            redirect_scope = dict(scope)
            if route_path.endswith("/"):
                redirect_scope["path"] = redirect_scope["path"].rstrip("/")
            else:
                redirect_scope["path"] = redirect_scope["path"] + "/"

            for route in matched_routes:
                match, child_scope = route.matches(redirect_scope)
                if match.value != 0:
                    redirect_url = URL(scope=redirect_scope)
                    response = RedirectResponse(url=str(redirect_url))
                    await response(scope, receive, send)
                    return

        await self.default(scope, receive, send)
