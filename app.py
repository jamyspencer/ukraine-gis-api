from fastapi import FastAPI
print("running")
app = FastAPI()

@app.get("/")
async def root():    
    return {"hello": "world"}