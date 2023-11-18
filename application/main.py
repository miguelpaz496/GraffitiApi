"""FastAPI starter sample
"""

from fastapi import Depends, FastAPI, Response, status
from fastapi.security import HTTPBearer
from application.config.utils import VerifyToken
from application.router.router import post
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
token_auth_scheme = HTTPBearer()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(post)


@app.get("/api/public")
def public():
    """No access token required to access this route"""

    result = {
        "status": "success",
        "msg": ("Hello from a public endpoint! "
                "You don't need to be authenticated to see this.")
    }
    return result


@app.get("/api/private")
def private(response: Response, token: str = Depends(token_auth_scheme)):
    """A valid access token is required to access this route"""

    # We need to protect this endpoint!

    result = VerifyToken(token.credentials).verify()

    if result.get("status"):
        response.status_code= status.HTTP_400_BAD_REQUEST
        return result

    result = {
        "status": "success",
        "msg": ("Hello from a private endpoint! "
                "You need to be authenticated to see this.")
    }
    return result

