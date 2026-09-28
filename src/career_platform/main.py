from fastapi import FastAPI

app = FastAPI(title="Career Platform")


@app.get("/health")
async def health_check() -> dict[str, str]:
    return {"status": "ok"}

