from flask import Flask

# Initialize the Flask app
app = Flask(__name__)

# Import routes from routes.py and register blueprints
from app.routes import extendible_hashing_blueprint, linear_hashing_blueprint

# Register the blueprints
app.register_blueprint(extendible_hashing_blueprint)
app.register_blueprint(linear_hashing_blueprint)

# Define a root route
@app.route("/")
def index():
    return "Welcome to the Flask app!"
