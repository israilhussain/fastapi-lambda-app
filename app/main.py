from fastapi import FastAPI
from mangum import Mangum
from app.routers import auth

app = FastAPI()

# Include Routers
app.include_router(auth.router)

# AWS Lambda Handler
handler = Mangum(app)
