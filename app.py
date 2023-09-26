import asyncio
import time

from fastapi import FastAPI, Request
from sentence_transformers import SentenceTransformer

app = FastAPI()

sbertmodel = SentenceTransformer('multi-qa-MiniLM-L6-cos-v1')

def model_predict():
    return sbertmodel.encode('how big is london')

async def vector_search(vector):
    await asyncio.sleep(0.005)

@app.get("/")
async def entrypoint(request:Request):
    ts = time.time()
    vector = model_predict()
    print(f'Model: {int((time.time()-ts)*1000)}ms')

    ts = time.time()
    await vector_search(vector)
    print(f'io task: {((time.time()-ts)*1000)}ms')
    return "ok"







