# 0.1.3

Param type in `docstring` can be `@body`, which makes the param takes the request body.

```
@bind_url("/body"):
def body(b):
    """
    :type b: @body
    """
    print(b)
```
