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
# prints 403, because the username/password combo was not correct
```

### Cookies

In order to deal with cookies, `requests` exposes `.cookies` attribute on request objects.

Be careful to access the cookies on the correct request object. If a page issues a redirect, the request object returned will be for the final page, but cookies may have been returned from previous requests in the chain. In order to access these cookies, index into the `.history` list, which contains request objects from the redirect chain, and inspect `.cookies` on each.

``` python
import requests

r = requests.post("http://10.0.10.10:5005", data={"username": "hello"})

print(r.cookies)
# prints a blank CookieJar, because a redirect was issued

print(r.history[0].cookies)
# prints a CookieJar with multiple cookies inside of it

cookies = r.history[0].cookies
```

Individual cookies can be inspected by looking up the cookie name with the mapping syntax:

``` python
username = cookies["username"]
```

If you don't need to modify cookies but need to send them back on future requests, you can simply pass the CookieJar to the appropriate request function:

``` python
requests.get("http://10.0.10.10:5005/loggedin", cookies=r.history[0].cookies)
```

However, if you _do_ need to modify cookies, it is easier to pass requests a `dict` of cookies instead of trying to modify the CookieJar (due to various design choices):

``` python
requests.get("http://10.0.10.10:5005/loggedin", cookies={"username": r.history[0].cookies["username"] + "asdf", "nonce": "0"})
```
