import inspect
import types
from typing import Any
from parse import parse
from frameapi.request import Request
from frameapi.response import Response

SUPPORTED_METHODS = {'GET', 'POST', 'DELETE'}

class FrameAPI:
    def __init__(self, middlewares=[]) -> None:
        """
        Initialize the FrameAPI class with an empty dictionary to store routes.

        """
        self.routes = dict()
        self.middlewares = middlewares
        self.middlewares_for_routes = dict()
    
    def __call__(self, environ, start_response) -> Any:
        """
        This method is called by the WSGI server when a request comes in.
        It is responsible for routing the request to the appropriate handler
        and returning the response to the server.

        """
        response = Response()
        request = Request(environ)

        for middleware in self.middlewares:
            if isinstance(middleware, types.FunctionType):
                middleware(request)
            else:
                raise ValueError('Middleware must be a function!')
        
        for path, handler_dict in self.routes.items():
            res = parse(path, request.path_info)
            
            for request_method, handler in handler_dict.items():
                if request.request_method == request_method and res:

                    route_mw_list = self.middlewares_for_routes[path][request_method]

                    for mw in route_mw_list:
                        if isinstance(mw, types.FunctionType):
                            mw(request)
                        else:
                            raise ValueError('Middleware must be a function!')
                    
                    handler(request, response, **res.named)
                    return response.as_wsgi(start_response)
                    
        
        return response.as_wsgi(start_response)
    
    def route_common(self, path, handler, method_name, middlewares):    
        """
        Common method to add a route to the routes dictionary
    
        """
        
        path_name = path or f"/{handler.__name__}"
        
        if path_name not in self.routes:
            self.routes[path_name] = {}
        
        self.routes[path_name][method_name] = handler

        if path_name not in self.middlewares_for_routes:
            self.middlewares_for_routes[path_name] = {}
        
        self.middlewares_for_routes[path_name][method_name] = middlewares
        return handler
    
    def get(self, path=None, middlewares=[]):
        """
        Decorator to add a GET route to the routes dictionary
        
        """
        def wrapper(handler):
            return self.route_common(path, handler, 'GET', middlewares)

        return wrapper

    def post(self, path=None, middlewares = []):
        """
        Decorator to add a POST route to the routes dictionary
        
        """
        def wrapper(handler):
            return self.route_common(path, handler, 'POST', middlewares)

        return wrapper
    
    def delete(self, path=None, middlewares = []):
        """
        Decorator to add a DELETE route to the routes dictionary
        
        """
        def wrapper(handler):
            return self.route_common(path, handler, 'DELETE', middlewares)

        return wrapper
    
    def route(self, path=None, middlewares=[]):
        """
        Decorator to create a class based route
        
        """
        def wrapper(handler):
            if isinstance(handler, type):
                class_members = inspect.getmembers(handler, lambda x: inspect.isfunction(x) and not (
                    x.__name__.startswith("__") and x.__name__.endswith("__")
                ) and x.__name__.upper() in SUPPORTED_METHODS)
                
                for fn_name, fn_handler in class_members:
                    self.route_common(path or f"/{handler.__name__}", fn_handler, fn_name.upper(), middlewares)
            else:
                raise ValueError("Route decorator can only be used with classes")
        
        return wrapper
    
    def welcome(self, default_template="frameapi/templates/default.html"):
        """
        Register a welcome route to serve the default.html file.
        """
        @self.get("/")
        def default_handler(request, response):
            response.render(default_template)