"""The main entrypoint file for the Zinny Flask server."""

import os
import argparse
import webbrowser

from zinny_webui import create_app


def main():
    """create the flask app and start the Zinny server."""
    # Parse CLI arguments or environment variables for configuration
    parser = argparse.ArgumentParser(description="Run the Zinny Web UI.")
    parser.add_argument(
        "--port",
        type=int,
        default=int(os.getenv("ZINNY_PORT", "7219")),
        help="Port number to run the server (default: 7219 or environment variable ZINNY_PORT)."
    )
    parser.add_argument(
        "--no-browser",
        action="store_true",
        help="Do not launch the default web browser."
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Run the server in debug mode."
    )

    args = parser.parse_args()

    flask_app = create_app()

    banner_text = """
 ______                   
 |__  (_)_ __  _ __  _   _ 
   / /| | '_ \| '_ \| | | |
  / /_| | | | | | | | |_| |
 /____|_|_| |_|_| |_|\__, |
                     |___/ 

    What's the skinny?
    -----------------
    The Zinny Web UI is launching
    http://localhost:{port}
    """

    if not args.no_browser:
        url = f"http://127.0.0.1:{args.port}"
        webbrowser.open(url)

    print(banner_text.format(port=args.port))
    #flask_app.run(port=args.port)
    flask_app.run(debug=args.debug, port=args.port)


if __name__ == '__main__':
    main()
