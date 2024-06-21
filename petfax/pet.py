from flask import Blueprint, render_template
import json

# Load pets data from JSON file
with open('pets.json', 'r') as f:
    pets = json.load(f)

# Blueprint definition
bp = Blueprint('pet', __name__, url_prefix='/pets')

# Index route - displays all pets
@bp.route('/')
def index():
    return render_template('index.html', pets=pets)

# Show route - displays details of a specific pet
@bp.route('/<int:index>')
def show(index):
    # Adjust index to zero-indexed for Python lists
    pet = pets[index - 1]  # Assuming your URL starts from 1
    return render_template('show.html', pet=pet)

# Fact creation route - serves form for submitting new facts
@bp.route('/facts/new')
def new_fact():
    return render_template('new_fact.html')
