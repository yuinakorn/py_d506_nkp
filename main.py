from fastapi import FastAPI

from controller.main_controller import toggle_process
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

# ##### เอาไปรวมไว้ใน sendd506 แล้ว อย่าหลงเข้ามาในนี้อีก
@app.post("/sent_to_cmpho/{option}")
async def sent_to_cmpho(option: str):
    return toggle_process(option)
   