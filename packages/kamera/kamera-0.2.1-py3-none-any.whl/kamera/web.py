from flask import Flask, Response, request, jsonify, render_template
from kamera.stream import CameraStream

app = Flask(__name__, static_folder="static", template_folder="templates")
camera_stream = None


def start_web_server(host, port, camera_index, rotate, brightness, grayscale):
    global camera_stream
    camera_stream = CameraStream(camera_index, rotate, brightness, grayscale)
    app.run(host=host, port=port)


@app.route("/")
def index():
    """Serve the web interface."""
    return render_template("index.html")


@app.route("/video_feed")
def video_feed():
    """Stream the video feed."""

    def generate_frames():
        while True:
            frame = camera_stream.get_frame()
            if frame is None:
                break
            yield (b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n")

    return Response(
        generate_frames(), mimetype="multipart/x-mixed-replace; boundary=frame"
    )


@app.route("/settings", methods=["POST"])
def settings():
    """Update camera settings dynamically."""
    data = request.json
    for key, value in data.items():
        if hasattr(camera_stream, key):
            setattr(camera_stream, key, value)
    return jsonify({"status": "success", "message": "Settings updated"})
