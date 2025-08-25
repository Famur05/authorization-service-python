from fastapi import APIRouter, Depends, Response
from app.schemas.user import UserAddDTO, UserLoginDTO, UserDTO
from app.datasources.database import SessionDep
from app.services.user import UserService
from app.config.auth import auth, config
from app.core.permissions import admin_required
from authx.schema import TokenPayload

router = APIRouter()


def get_user_service(session: SessionDep) -> UserService:
    return UserService(session)


@router.post("/", summary="Register a new user")
async def create(
    new_user: UserAddDTO, user_service: UserService = Depends(get_user_service)
) -> dict[str, str | int]:
    return await user_service.create(new_user)


@router.get("/", summary="Get all users 🔒", dependencies=[Depends(admin_required)])
async def get_all(
    user_service: UserService = Depends(get_user_service),
) -> list[UserDTO]:
    return await user_service.get_all()


@router.post("/login", summary="Login a user")
async def login(
    credentials: UserLoginDTO,
    response: Response,
    user_service: UserService = Depends(get_user_service),
) -> dict[str, str | int]:
    return await user_service.login(credentials, response)


@router.get("/protected", summary="Protected route")
async def protected(
    payload: TokenPayload = Depends(auth.access_token_required),
) -> dict[str, str]:
    return {
        "message": "Protected information",
        "user_id": payload.sub,
        "role": payload.role,
    }


@router.get("/logout", summary="Logout a user")
async def logout(response: Response) -> dict[str, str]:
    response.delete_cookie(key=config.JWT_ACCESS_COOKIE_NAME)
    return {"message": "User logged out successfully"}


@router.get("/{user_id}", summary="Get user by id 🔒", dependencies=[Depends(admin_required)])
async def get_by_id(
    user_id: int,
    user_service: UserService = Depends(get_user_service),
) -> UserDTO:
    return await user_service.get_by_id(user_id)


@router.delete("/{user_id}", summary="Delete user by id 🔒", dependencies=[Depends(admin_required)])
async def delete(
    user_id: int,
    user_service: UserService = Depends(get_user_service),
) -> dict[str, str | int]:
    return await user_service.delete(user_id)
