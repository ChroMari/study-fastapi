from fastapi import FastAPI, Header, Response
 
app = FastAPI()
 
 
@app.get("/")
def root(user_agent: str = Header()):
    data = "Hello from here"
    
    return Response(content=data, media_type="text/plain", headers={"Secret-Code" : "123459"})
