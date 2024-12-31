from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from kamera.camera import Camera
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory="kamera/templates")

camera = Camera()

app.mount("/static", StaticFiles(directory="kamera/static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """Serve the web interface."""
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/video_feed")
async def video_feed():
    """Stream video frames."""

    def generate_frames():
        while True:
            frame = camera.get_frame()
            if frame is None:
                break
            yield (b"--frame\r\nContent-Type: image/jpeg\r\n\r\n" + frame + b"\r\n")

    return StreamingResponse(
        generate_frames(), media_type="multipart/x-mixed-replace; boundary=frame"
    )


@app.post("/settings")
async def update_settings(
    rotate: int = Form(0), brightness: float = Form(1.0), grayscale: bool = Form(False)
):
    """Update camera settings dynamically."""
    camera.rotate = rotate
    camera.brightness = brightness
    camera.grayscale = grayscale
    return {"status": "success", "message": "Settings updated successfully"}


def main():
    """CLI entry point."""
    uvicorn.run("kamera.app:app", host="0.0.0.0", port=4141, reload=False)


if __name__ == "__main__":
    main()
