from fastapi import FastAPI

from controller.main_controller import toggle_process
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/sent_to_cmpho/{option}")
async def sent_to_cmpho(option: str):
    return toggle_process(option)
   