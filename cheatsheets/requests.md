# requests

`requests` is a python package that simplifies the process of making HTTP requests to remote servers.

## Usage


### GET

In its most basic form, you can perform HTTP GET requests with the `.get` function:

``` python
import requests

r = requests.get("http://10.0.10.10:5001")

print(r.status_code)
# prints 200

print(r.content)
# prints the data (in this case, HTML) returned by the request
```

### POST

To perform POST requests, use the `.post` function. To pass form parameters, use the `data=` parameter and pass a dictionary.

``` python
import requests

r = requests.post("http://10.0.10.10:5001", data={"username": "admin", "password": "Hello!"})

print(r.status_code)
# print 403, because the username/password combo was not correct
```
