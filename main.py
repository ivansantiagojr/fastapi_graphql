from fastapi import FastAPI
from src.config import settings
import uvicorn
from src.graphql_api import graphql_app

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")


@app.get("/")
async def root():
    return {"messagge": settings.PORT}

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        reload=True,
        port=settings.PORT,
    )
