import tornado.web as _web

__author__ = 'Michael Kim'


class UrlBindingClashError(Exception):
    def __init__(self, url, method):
        self.__url = url
        self.__method = method

    def __str__(self):
        return "Url binding \"{}\" ({}) has already been defined".format(
            self.__url,
            "any" if self.__method is None else self.__method
        )


class HttpMethodError(Exception):
    def __init__(self, method):
        self.__method = method

    def __str__(self):
        return "Method \"{}\" not allowed".format(self.__method)


class UrlBindings(object):
    def __init__(self):
        self.__bindings = {}

    def add(self, func, url, method=None):
        if method not in [None, "get", "post"]:
            raise HttpMethodError(method)
        if url in self.__bindings:
            methods = self.__bindings[url]
            if (method is None) or (None in methods) or (method in methods):
                raise UrlBindingClashError(url, method)
        else:
            methods = {}
            self.__bindings[url] = methods
        methods[method] = func

    @staticmethod
    def __gen_method(func, __params):
        _params = __params[func]

        def __method(self):
            params = _params.parse(self)
            val = func(**params)
            if val is None:
                return
            if isinstance(val, str):
                self.write(val)
                return
            if not isinstance(val, dict):
                raise ValueError(val)
            if "status" in val:
                status = val["status"]
                self.set_status(status)
            if "header" in val:
                header = val["header"]
                for key in header:
                    self.add_header(key, header[key])
            if "data" in val:
                self.write(val["data"])

        return __method

    def get_handlers(self, params):
        handlers = []
        for url in self.__bindings:
            methods = self.__bindings[url]
            get_method = None
            post_method = None
            if None in methods:
                get_method = post_method = methods[None]
            if "get" in methods:
                get_method = methods["get"]
            if "post" in methods:
                post_method = methods["post"]

            class __NewHandler(_web.RequestHandler):
                pass

            if get_method is not None:
                __NewHandler.get = UrlBindings.__gen_method(get_method, params)
            if post_method is not None:
                __NewHandler.post = UrlBindings.__gen_method(post_method, params)

            handlers.append((url, __NewHandler))

        return handlers
