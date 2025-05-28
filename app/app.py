from flask import Flask, render_template
from app.database import Database

class App():
    # Initialise the app
    def __init__(self):
        self.app = Flask(__name__)
        self.setup_database()
        self.setup_routes()

    # Setup routes for the app
    def setup_routes(self):
        @self.app.route("/")
        def main():
            return render_template("index.html")

    # Setup database for the app
    def setup_database(self):
        self.database = Database()

    # Run the app
    def run(self):
        self.app.run(debug=True)
