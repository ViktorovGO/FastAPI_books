from fastapi_users import FastAPIUsers

from auth.models import User
from auth.utils import get_user_manager
from auth.service import auth_backend

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

current_user = fastapi_users.current_user()