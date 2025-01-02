from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.routes.ppt import router as ppt_router

app = FastAPI()

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://localhost:3000", "https:/127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routes
app.include_router(ppt_router, tags=["PowerPoint Operations"])


@app.get("/")
async def root():
    return {"message": "Hello World"}
