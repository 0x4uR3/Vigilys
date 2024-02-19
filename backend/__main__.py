import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from backend.routes import devices, users, settings

app = FastAPI(title="Vigilys",
    description="Vigilys Backend",
    version="1.0.0",)

app.include_router(devices.router)
app.include_router(users.router)
app.include_router(settings.router)

@app.exception_handler(Exception)
def validation_exception_handler(request, err):
    base_error_message = f"Failed to execute: {request.method}: {request.url}"
    return JSONResponse(status_code=400, content={"message": f"{base_error_message}. Detail: {err}"})
    
if __name__ == "__main__":
    uvicorn.run("backend.__main__:app", port=9000, reload=True)