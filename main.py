import time
import random
from fastapi import FastAPI, Response
from fastapi.responses import StreamingResponse


app = FastAPI()


async def fake_number_streamer():
    for i in range(random.randint(10, 20)):
        yield "{}".format(i+1)
        time.sleep(0.1 * random.randint(1, 10))


@app.get("/")
async def index():
    # 读取html内容输出给客户端
    return Response(open("index.html", encoding="utf-8").read())


@app.get("/sse")
async def sse():
    return StreamingResponse(fake_number_streamer(), media_type="text/event-stream")
