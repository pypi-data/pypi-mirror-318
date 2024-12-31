'''HMNX'''
import os
import subprocess
from flask import Flask, render_template_string

class HarmonixPy:
    '''initial setup'''
    def __init__(self, project_dir="../my_project"):
        self.project_dir = os.path.abspath(project_dir)
        self.static_folder = os.path.join(self.project_dir, "static")
        self.templates_folder = os.path.join(self.project_dir, "templates")
        self.html_files = [os.path.join(self.templates_folder, "index.html")]
        self.css_files = [os.path.join(self.static_folder, "styles.css")]
        self.js_files = [os.path.join(self.static_folder, "script.js")]
        self.py_files = [os.path.join(self.project_dir, "app.py")]  # Default Python file
        self.requirements_file_path = os.path.join(self.project_dir, "requirements.txt")
        self.app = Flask(__name__, static_folder=self.static_folder, template_folder=self.templates_folder)

        # Define the home route
        @self.app.route("/")
        def home():
            html_content = self.load_html_content()
            return render_template_string(html_content)

    def html(self, path):
        """Add a custom path for the HTML file."""
        self.html_files.append(path)
        return self.html_files

    def css(self, path):
        """Add a custom path for the CSS file."""
        self.css_files.append(path)
        return self.css_files

    def js(self, path):
        """Add a custom path for the JavaScript file."""
        self.js_files.append(path)
        return self.js_files

    def py(self, path):
        """Add a custom path for the Python file."""
        self.py_files.append(path)
        return self.py_files

    def load_html_content(self):
        """Load content from the first HTML file in the list."""
        try:
            with open(self.html_files[0], "r", encoding="utf-8") as html_file:
                html_content = html_file.read()
            # Add dynamic links for multiple CSS and JS files
            html_content = self.add_static_links(html_content)
            return html_content
        except FileNotFoundError:
            return "<h1>Error: HTML file not found.</h1>"

    def add_static_links(self, html_content):
        """Dynamically link external JS and CSS files using Flask's url_for."""
        # Add all CSS links
        css_links = "\n".join([f'<link rel="stylesheet" href="{{{{ url_for(\'static\', filename=\'{os.path.basename(css_file)}\') }}}}">' for css_file in self.css_files])

        # Add all JS links
        js_links = "\n".join([f'<script src="{{{{ url_for(\'static\', filename=\'{os.path.basename(js_file)}\') }}}}"></script>' for js_file in self.js_files])

        if "</head>" in html_content:
            html_content = html_content.replace("</head>", f"{css_links}\n{js_links}\n</head>")
        else:
            raise ValueError("No closing </head> tag found in the HTML file.")

        return html_content

    def install_dependencies(self):
        """Install dependencies listed in the specified requirements file."""
        try:
            if os.path.exists(self.requirements_file_path):
                with open(self.requirements_file_path, "r", encoding="utf-8") as file:
                    dependencies = file.read().splitlines()

                for dependency in dependencies:
                    subprocess.check_call(["pip", "install", dependency])
                print("All dependencies installed successfully!")
            else:
                print(f"Error: {self.requirements_file_path} not found.")
        except subprocess.CalledProcessError as e:
            print(f"Error installing a package: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def run(self):
        """Install dependencies and start the Flask app."""
        self.install_dependencies()

        # Execute all Python files before running the app
        self.execute_python_files()

        self.app.run(debug=True, host="0.0.0.0", port=5000)

    def execute_python_files(self):
        """Execute all Python files listed in self.python_files."""
        for python_file in self.py_files:
            if os.path.exists(python_file):
                try:
                    subprocess.check_call(["python", python_file])
                    print(f"Successfully executed {python_file}")
                except subprocess.CalledProcessError as e:
                    print(f"Error executing Python file {python_file}: {e}")
            else:
                print(f"Error: Python file {python_file} not found.")

    def create_default_files(self, *file_types):
        """Create default files based on the passed file types."""
        # Create directories if not exist
        os.makedirs(self.static_folder, exist_ok=True)
        os.makedirs(self.templates_folder, exist_ok=True)

        if "html" in file_types:
            if not os.path.exists(self.html_files[0]):
                with open(self.html_files[0], 'w', encoding='utf-8') as html_file:
                    html_file.write("""<!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Flask with External CSS and JS</title>
                </head>
                <body>
                    <h1>Welcome to HarmonixPy!</h1>
                    <p>This page uses an external CSS and JS file.</p>
                    
                    <!-- Button to trigger the change -->
                    <button id="changeTextButton">Click me to change text</button>

                    <!-- Linking the JS file -->
                </body>
                </html>""")

        if "css" in file_types:
            if not os.path.exists(self.css_files[0]):
                with open(self.css_files[0], 'w', encoding='utf-8') as css_file:
                    css_file.write("""body {
                    font-family: Arial, sans-serif;
                    background-color: green;
                    text-align: center;
                    padding: 50px;
                }

                h1 {
                    color: yellow;
                }

                p {
                    color: blue;
                }""")

        if "js" in file_types:
            if not os.path.exists(self.js_files[0]):
                with open(self.js_files[0], 'w', encoding='utf-8') as js_file:
                    js_file.write("""document.addEventListener("DOMContentLoaded", function() {
                                        const button = document.getElementById("changeTextButton");
                                        const welcomeMessage = document.querySelector("h1");
                                        button.addEventListener("click", function() {
                                            welcomeMessage.textContent = "You clicked the button! The text has changed.";
                                        });
                                    });""")

        if "py" in file_types:
            if not os.path.exists(self.py_files[0]):
                with open(self.py_files[0], 'w', encoding='utf-8') as py_file:
                    # Dynamically load HTML file into the home route
                    py_file.write(f"""from flask import Flask, render_template
                    app = Flask(__name__)

                    @app.route('/')
                    def home():
                        # Dynamically render the HTML file specified in self.html_files
                        return render_template("{os.path.basename(self.html_files[0])}")

                    if __name__ == '__main__':
                        app.run(debug=True)""")
