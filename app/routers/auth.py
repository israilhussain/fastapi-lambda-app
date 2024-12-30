from fastapi import APIRouter, HTTPException
from app.models.user import UserSignUp, UserSignIn
from app.utils.hashing import hash_password
from app.utils.db import users_table

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/signup")
async def signup(user: UserSignUp):
    """User Sign-Up Endpoint."""
    hashed_password = hash_password(user.password)

    # Check if user exists
    response = users_table.get_item(Key={"email": user.email})
    if "Item" in response:
        raise HTTPException(status_code=400, detail="User already exists")

    # Save user in DynamoDB
    users_table.put_item(
        Item={
            "email": user.email,
            "password": hashed_password,
            "created_at": "2024-12-29",  # Example timestamp
        }
    )
    return {"message": "User registered successfully"}


@router.post("/signin")
async def signin(user: UserSignIn):
    """User Sign-In Endpoint."""
    response = users_table.get_item(Key={"email": user.email})
    if "Item" not in response:
        raise HTTPException(status_code=400, detail="Invalid email or password")

    stored_password = response["Item"]["password"]
    if hash_password(user.password) != stored_password:
        raise HTTPException(status_code=400, detail="Invalid email or password")

    return {"message": "Sign-in successful", "email": user.email}
