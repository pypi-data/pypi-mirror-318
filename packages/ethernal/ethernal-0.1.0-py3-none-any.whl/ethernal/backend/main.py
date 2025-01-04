from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import router
from config.settings import Settings

app = FastAPI(title="Ethernal AI Platform")
settings = Settings()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api/v1")


@app.on_event("startup")
async def startup_event():
    # Initialize services
    from services.agent_service import AgentService
    from services.blockchain import BlockchainService

    await AgentService.initialize()
    await BlockchainService.initialize()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)