from fastapi import FastAPI, Request, HTTPException

app = FastAPI()

def checkout_headers(headers: Request.headers):
    if "user-agent" not in headers:
        raise HTTPException(status_code=400, detail="The User-Agent header not found!")
    if "Accept-Language" not in headers:
        raise HTTPException(status_code=400, detail="The Accept-Language header not found!")

@app.get("/")
def root(request: Request):
    #return request.headers["user-agent"]
    checkout_headers(request.headers)

    return {
        "User-Agent": request.headers["user-agent"],
        "Accept-Language": request.headers["accept-language"], 
    }
