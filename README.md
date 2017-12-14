# Michael Kim's Tornado helper

Easy way to setup a [tornado](http://www.tornadoweb.org/en/stable/index.html) server.

Author: [Michael Kim](http://michaelkim0407.com) <mkim0407@gmail.com>

***IMPORTANT*** This package has been merged into [mklibpy](https://github.com/MichaelKim0407/mklibpy/tree/master/mklibpy) (v0.8) and is now inactive. Please install that package instead.

## Installation

```
pip install mktornado
```

## Usage

Please refer to [the project wiki](https://github.com/MichaelKim0407/mktornado/wiki) for a complete guide.

Hello world script:

```
import random

from mktornado import bind_url, start, json

__author__ = 'Michael Kim'


@bind_url("/")
def hello_world():
    return "Hello world!"


@bind_url("/random", "get")
def random_points(size=10):
    """
    :type size: int
    """
    data = []
    for i in range(size):
        x = random.random()
        y = random.random()
        data.append({
            "x": x,
            "y": y
        })
    return json(data)


start(8080, debug=True)

# try these:
# http://localhost:8080
# http://localhost:8080/random
# http://localhost:8080/random?size=20
```

## License

MIT
