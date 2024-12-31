import argparse
from kamera.web import start_web_server


def main():
    parser = argparse.ArgumentParser(
        description="Stream your webcam with adjustable settings."
    )
    parser.add_argument(
        "--ip",
        type=str,
        default="0.0.0.0",
        help="IP address to host the stream (default: 0.0.0.0)",
    )
    parser.add_argument(
        "--port", type=int, default=4141, help="Port to host the stream (default: 4141)"
    )
    parser.add_argument(
        "--camera", type=int, default=0, help="Camera device number (default: 0)"
    )
    parser.add_argument(
        "--rotate",
        type=int,
        default=0,
        help="Rotate the video feed by 90, 180, or 270 degrees.",
    )
    parser.add_argument(
        "--brightness", type=float, default=1.0, help="Adjust brightness (0.1 to 2.0)."
    )
    parser.add_argument(
        "--grayscale", action="store_true", help="Stream the video in grayscale."
    )

    args = parser.parse_args()

    print(f"Starting stream on http://{args.ip}:{args.port}/video_feed")
    start_web_server(
        args.ip, args.port, args.camera, args.rotate, args.brightness, args.grayscale
    )


if __name__ == "__main__":
    main()
