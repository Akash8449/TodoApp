from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from routers import tasks

app = FastAPI()

app.include_router(tasks.router)

@app.get("/", include_in_schema=False)
def redirect_to_docs():
    return RedirectResponse(url="/docs")
