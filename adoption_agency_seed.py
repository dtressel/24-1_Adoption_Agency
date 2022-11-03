from models import db, Pet
from app import app

db.drop_all()
db.create_all()

# create seed pets

buffy = Pet(
    name = 'Buffy',
    species = 'Hamster',
    photo_url = 'https://www.statnews.com/wp-content/uploads/2022/06/AdobeStock_168830140-768x432.jpeg',
    notes = 'cute, fluffy, likes raisins'
    )

ash = Pet(
    name = 'Ash',
    species = 'Dog',
    photo_url = 'https://www.dogbreedinfo.com/images18/AustralianCattleDogMaxFullGrown.JPG',
    notes = 'friendly, good with kids',
    age = 5
    )

sophia = Pet(
    name = 'Sophia',
    species = 'Parakeet',
    photo_url = 'https://i.pinimg.com/originals/de/01/22/de01222bc0f32f06b19684aad6b413d7.jpg',
    available = False
    )

#add pets to database
pets = [buffy, ash, sophia]

db.session.add_all(pets)
db.session.commit()
