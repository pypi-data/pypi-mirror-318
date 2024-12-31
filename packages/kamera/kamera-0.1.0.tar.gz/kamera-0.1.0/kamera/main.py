import cv2
from flask import Flask, Response
import argparse


def start_stream(host="0.0.0.0", port=4141):
    app = Flask(__name__)
    video_capture = cv2.VideoCapture(0)

    def generate_frames():
        while True:
            success, frame = video_capture.read()
            if not success:
                break
            else:
                _, buffer = cv2.imencode(".jpg", frame)
                frame = buffer.tobytes()
                yield (
                    b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n"
                )

    @app.route("/video_feed")
    def video_feed():
        return Response(
            generate_frames(), mimetype="multipart/x-mixed-replace; boundary=frame"
        )

    @app.route("/")
    def index():
        return "Webcam Streaming! Visit /video_feed to view the stream."

    app.run(host=host, port=port)


def main():
    parser = argparse.ArgumentParser(description="Stream your webcam over the network.")
    parser.add_argument(
        "--ip",
        type=str,
        default="0.0.0.0",
        help="IP address to host the stream (default: 0.0.0.0)",
    )
    parser.add_argument(
        "--port", type=int, default=4141, help="Port to host the stream (default: 4141)"
    )
    args = parser.parse_args()

    print(f"Starting stream on http://{args.ip}:{args.port}/video_feed")
    start_stream(host=args.ip, port=args.port)


if __name__ == "__main__":
    main()
