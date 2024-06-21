from flask import Flask
from .pet import bp as pet_bp  # Importing the 'bp' Blueprint instance from pet.py

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello():
        return 'Hello, PetFax!'

    # Registering the 'pet' Blueprint
    app.register_blueprint(pet_bp)

    return app
