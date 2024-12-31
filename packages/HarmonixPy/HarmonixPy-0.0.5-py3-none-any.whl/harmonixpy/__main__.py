'''__main__'''
import argparse
from harmonixpy import __version__
from harmonixpy.flask_app import HarmonixPy

def main():
    """Entry point for the HarmonixPy CLI."""
    parser = argparse.ArgumentParser(description="HarmonixPy Command-Line Interface")

    # Define basic arguments
    parser.add_argument("--version", action="store_true", help="Show the version of HarmonixPy")
    parser.add_argument("--start", action="store_true", help="Start the HarmonixPy server")
    parser.add_argument("--stop", action="store_true", help="Stop the HarmonixPy server")
    parser.add_argument("--config", type=str, help="Specify a configuration file for the server")
    parser.add_argument("--help", action="help", help="Show this help message and exit")

    # Parse the arguments
    args = parser.parse_args()

    if args.version:
        print(f"HarmonixPy version {__version__}")
    elif args.start:
        print("Starting HarmonixPy server...")
        server = HarmonixPy()  # Initialize the server
        server.run()           # Start the Flask server
    elif args.stop:
        print("Stopping the HarmonixPy server...")  # Implement the stop functionality if needed
        # Code to stop the server goes here
    elif args.config:
        print(f"Using configuration file: {args.config}")
        # Code to handle custom config file path goes here
    else:
        print("No valid argument provided. Use --help to see available commands.")

if __name__ == "__main__":
    main()
