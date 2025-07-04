import uvicorn
from fastapi import FastAPI

app=FastAPI()


@app.post('/hi_world')
async def hi_world():
    return "Hi world"

if __name__ == '__main__':
    uvicorn.run("main:app",reload=True)