"""Main File."""
import uvicorn
from fastapi import FastAPI

from app.endpoints import health, ideas

app = FastAPI(docs_url='/ui')
app.include_router(health.router)
app.include_router(ideas.router)


if __name__ == '__main__':
    uvicorn.run(app='app.__main__:app', reload=True, access_log=False)
