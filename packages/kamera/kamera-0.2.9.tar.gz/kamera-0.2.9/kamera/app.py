import logging
import os

import cv2
import uvicorn
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.websockets import WebSocket

from kamera.camera import Camera
from kamera.settings import AVAILABLE_FILTERS

# Initialize FastAPI app
app = FastAPI()

# Initialize camera and logger
camera = Camera()
logger = logging.getLogger("kamera")
logging.basicConfig(level=logging.INFO)

static_path = os.path.join(os.path.dirname(__file__), "static")
template_path = os.path.join(os.path.dirname(__file__), "templates")

if not os.path.exists(static_path):
    raise RuntimeError(f"Static directory not found: {static_path}")


# Serve static files
app.mount("/static", StaticFiles(directory=static_path), name="static")
templates = Jinja2Templates(directory=template_path)


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
    rotate: int = Form(0),
    brightness: float = Form(1.0),
    grayscale: bool = Form(False),
    mirror: bool = Form(False),
    filter_name: str = Form("none"),
    camera_index: int = Form(0),  # Added camera index
):
    """Update camera settings dynamically."""
    # Reinitialize camera if the index has changed
    if camera_index != camera.camera_index:
        camera.release()
        camera.camera_index = camera_index
        camera.cap = cv2.VideoCapture(camera.camera_index)
        if not camera.cap.isOpened():
            logger.error(
                f"Failed to initialize camera with index {camera.camera_index}"
            )
            return {"status": "error", "message": "Failed to switch camera"}
        logger.info(f"Camera index changed to {camera.camera_index}")

    camera.rotate = rotate
    camera.brightness = brightness
    camera.grayscale = grayscale
    camera.mirror = mirror
    camera.filter_name = filter_name
    logger.info("Settings updated: %s", camera.__dict__)
    return {"status": "success", "message": "Settings updated successfully"}


@app.websocket("/ws/video_feed")
async def websocket_video_feed(websocket: WebSocket):
    """Serve video feed via WebSocket."""
    await websocket.accept()
    try:
        while True:
            frame = camera.get_frame()
            if frame is None:
                break
            await websocket.send_bytes(frame)
    except Exception as e:
        logger.error("WebSocket error: %s", str(e))
    finally:
        await websocket.close()


@app.on_event("shutdown")
def shutdown_event():
    """Release camera resources on shutdown."""
    camera.release()
    logger.info("Camera released.")


def main():
    uvicorn.run("kamera.app:app", host="0.0.0.0", port=4141, reload=True)


if __name__ == "__main__":
    main()
