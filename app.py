from select import select
from flask import Flask, request, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoption_agency'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['SECRET_KEY'] = 'fruitsmell57892'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def show_home():
    pets = Pet.query.all()
    return render_template('home.html', pets=pets)

@app.route('/add', methods=["GET", "POST"])
def show_add_pet_form():
    """Show add pet form and handle submission"""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        new_pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(new_pet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('add-pet.html', form=form)

@app.route('/pet/<int:pet_id>', methods=["GET", "POST"])
def show_pet_details(pet_id):
    """Shows more information about the pet and a form to edit the pet.
    Also, handles edit submission."""

    selected_pet = Pet.query.get(pet_id)
    form = EditPetForm()

    if form.validate_on_submit():
        photo_url = form.photo_url.data
        notes = form.notes.data
        available = form.available.data
        if photo_url != "":
            selected_pet.photo_url = photo_url
        if notes != "":
            selected_pet.notes = notes
        if available == "Yes":
            selected_pet.available = True
        elif available == "No":
            selected_pet.available = False
        db.session.add(selected_pet)
        db.session.commit()
        flash(f'Details have been successfully updated for {selected_pet.name}')
        return redirect(f'/pet/{pet_id}')
    else:
        return render_template('pet-details.html', pet=selected_pet, form=form)

