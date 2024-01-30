from fastapi import FastAPI, BackgroundTasks, HTTPException
from pydantic import BaseModel
from extract import *
import os
from a2wsgi import ASGIMiddleware
from fastapi.middleware.cors import CORSMiddleware
import asyncio

SECRET = os.getenv("SECRET")

#
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
wsgi_app = ASGIMiddleware(app)


class BackgroundRunner:
    def __init__(self):
        self.value = 0

    async def run_main(self):
        while True:
            await asyncio.sleep(0.1)
            self.value += 1


runner = BackgroundRunner()


@app.on_event('startup')
async def app_startup():
    asyncio.create_task(runner.run_main())


@app.get("/")
def root():
    return runner.value
