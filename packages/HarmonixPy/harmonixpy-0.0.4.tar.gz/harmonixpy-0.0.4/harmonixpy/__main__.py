import argparse
from harmonixpy import __version__
from harmonixpy.flask_app import HarmonixPy

def main():
    """Entry point for the HarmonixPy CLI."""
    parser = argparse.ArgumentParser(description="HarmonixPy Command-Line Interface")
    parser.add_argument("--version", action="store_true", help="Show the version of HarmonixPy")
    args = parser.parse_args()

    if args.version:
        print(f"HarmonixPy version {__version__}")
    else:
        print("Starting HarmonixPy server...")
        server = HarmonixPy()  # Initialize your Flask server
        server.run()           # Start the server

if __name__ == "__main__":
    main()
