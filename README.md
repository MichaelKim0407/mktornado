# Michael Kim's Tornado helper

Easy way to setup a [tornado](http://www.tornadoweb.org/en/stable/index.html) server.

Author: Michael Kim <jinzheng19930407@sina.com>

## Installation

    pip install mktornado

## Usage

* Binding methods

    Declare a function and decorate it with `bind_url`:

    ```
    @mktornado.bind_url("/")
    def hello():
        return "Hello world!"
    ```

    Specify `get` or `post`:

    ```
    @mktornado.bind_url("/test", "get")
    def test():
        return "Test GET"
    ```

* Taking HTTP parameters:

    Simply add arguments to the function:

    ```
    @mktornado.bind_url("/hi")
    def hi(name):
        return "Hi, {}!".format(name)
    ```

    Specify argument types using `pydoc`:

    ```
    @mktornado.bind_url("/login")
    def login(id):
        '''
        :type id: int
        '''
        logging.debug(type(id))
        return "Logged in as user {}".format(id)
    ```

    Making a parameter optional by specifying the argument's default value:

    ```
    @mktornado.bind_url("/delete")
    def delete(id, clear_files=False):
        '''
        :type id: int
        :type clear_files: bool
        '''
        # TODO do stuff here
        return "OK"
    ```

    Take a list of argument by specifying parameter type as `list`. Elements contained will be of type `str`. No default value should be given. (See [`RequestHandler.get_arguments`](http://www.tornadoweb.org/en/stable/web.html#tornado.web.RequestHandler.get_arguments))

* Return values

    Return `None` to set an empty response.

    Return a `str`, as the examples above.

    Or, return a `dict` containing `header` and `data` (both optional).

    `header` should also be a `dict`, containing all the fields you would like to set. (See [`RequestHandler.add_header`](http://www.tornadoweb.org/en/stable/web.html#tornado.web.RequestHandler.add_header))

    `data` should be a `str` to be written into the response body.

    Specifically, if you want to respond a `json`, use `mktornado.json`:

    ```
    @mktornado.bind_url("/api", "get")
    def api(id):
        '''
        :type id: int
        '''
        data = {}
        # TODO do stuff here
        return mktornado.json(data)
    ```

* Starting the server

    ```
    mktornado.start(port, **kwargs)
    ```

    `port` is the port on which you wish to start the server.

    `kwargs` are the arguments to be passed into the server application. See [Application settings](http://www.tornadoweb.org/en/stable/web.html#tornado.web.Application.settings).
