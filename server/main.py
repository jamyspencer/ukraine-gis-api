from fastapi import FastAPI
from server.data.railroad import *
import uvicorn
from server.util.util import feature_group

print(__name__)
app = FastAPI()

@app.get("/")
async def root():    
    return {"hello": "world"}

@app.get("/api/railroads/")
async def railroads():
    data = get_all_railroads()
    return feature_group([r.to_geo_json() for r in data], "Ukraine Railroads")



if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)