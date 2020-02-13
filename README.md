# StarJWT
Basic [JWT](https://jwt.io/) authentication integration for [Starlette](https://starlette.io/).
All it does is validate and sign JWTs and set their contents on the request's
`auth` and `user` attributes. See the [Starlette documentation](https://www.starlette.io/authentication/)
for more details.

## Usage

Create a `JWTBackend` instance and install Starlette's `AuthenticationMiddleware`
using it. Then in your login and logout routes, wrap your responses in
`backend.set_login_cookie(repsonse, sub)` and `backend.logout(response)`. For
a general guide to Starlette's authentication system see the [here](https://www.starlette.io/authentication/).

By default, the user is a `SimpleUser` with username set to the `sub` value of
the JWT, and the scopes are empty. To change this behaviour, you can subclass
`JWTBackend` and override the `get_user` method to, for example, get the user
in the database.

### Example

```python
from starlette.applications import Starlette
from starlette.middleware.authentication import AuthenticationMiddleware
from starlette.responses import PlainTextResponse
from starlette_jwt import JWTBackend

app = Starlette()
backend = JWTBackend(...)
app.add_middleware(AuthenticationMiddleware, backend=backend)

@app.route("/login")
async def login():
    # do login
    return backend.set_login_cookie(PlainTextResponse("ok"), "username")

@app.route("/logout")
async def logout():
    # do logout
    return backend.logout(PlainTextResponse("ok"))

```

## Requirements
Starlette JWT requires [Starlette](https://starlette.io/), [PyJWT](https://pyjwt.readthedocs.io)
and Python 3.8 or higher ([why?](https://because-you-should-always-use-the-latest-version.invalid)). 

## License
Starlette JWT is licensed under the [AGPL 3.0](https://www.gnu.org/licenses/agpl-3.0.en.html).

