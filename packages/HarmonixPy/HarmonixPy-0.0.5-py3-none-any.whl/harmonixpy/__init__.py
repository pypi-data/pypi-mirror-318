''' harmonixpy/__init__.py '''
__version__ = "0.0.5"

from .flask_app import HarmonixPy as _HarmonixPy

# Default class instance for easy access to HarmonixPy functions
_app = _HarmonixPy()

# User-facing functions
def html(file_paths):
    """Set the HTML file paths. Accepts a list of file paths."""
    if isinstance(file_paths, list):
        for path in file_paths:
            _app.html(path)
    else:
        _app.html(file_paths)

def css(file_paths):
    """Set the CSS file paths. Accepts a list of file paths."""
    if isinstance(file_paths, list):
        for path in file_paths:
            _app.css(path)
    else:
        _app.css(file_paths)

def js(file_paths):
    """Set the JavaScript file paths. Accepts a list of file paths."""
    if isinstance(file_paths, list):
        for path in file_paths:
            _app.js(path)
    else:
        _app.js(file_paths)

def dependency(file_path):
    """Set the requirements.txt file path for dependencies."""
    _app.requirements_file_path = file_path

def create_default_files(*args):
    """Create default HTML, CSS, JS, and Python files in the specified directories based on input types."""
    _app.create_default_files(*args)

def install_dependencies():
    """Install dependencies from requirements.txt."""
    _app.install_dependencies()

def load_html_content():
    """Load the content of the main HTML file as a string."""
    return _app.load_html_content()

def run(host="127.0.0.1", port=5000):
    """Run the Flask application."""
    _app.app.run(debug=True, host=host, port=port)

# Allow a single function to initialize and run the app
def harmonixpy(html_files=["index.html"], css_files=["static/styles.css"], js_files=["static/script.js"], requirements_file="requirements.txt", static_folder="static"):
    """
    Initialize the app with specified files and folders and run it.

    Args:
        html_files (list): List of HTML file paths.
        css_files (list): List of CSS file paths.
        js_files (list): List of JavaScript file paths.
        requirements_file (str): Path to the requirements.txt file.
        static_folder (str): Path to the static folder.
    """
    if html_files:
        html(html_files)
    if css_files:
        css(css_files)
    if js_files:
        js(js_files)
    if requirements_file:
        dependency(requirements_file)

    _app.static_folder = static_folder
    create_default_files("html", "css", "js", "py")  # Create all default files
    run()
