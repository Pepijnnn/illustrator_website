import os
from django.shortcuts import render
from django.conf import settings

# def my_work(request):
#     # Path to the images directory using BASE_DIR
#     images_directory = os.path.join(settings.BASE_DIR, 'static', 'portfolio', 'images')

#     # Get a list of all files in the images directory
#     image_files = [f for f in os.listdir(images_directory) if os.path.isfile(os.path.join(images_directory, f))][1:]

#     # Create a list of dictionaries with image information
#     images = [{'filename': file, 'thumbnail_filename': file, 'caption': f'Caption for {file}'}
#               for file in image_files]

#     return render(request, 'portfolio/my_work.html', {'images': images})


def my_work(request):
    # Path to the images directory using BASE_DIR
    images_directory = os.path.join(settings.BASE_DIR, 'static', 'portfolio', 'images')

    # Get a list of all files in the images directory
    image_files = [f for f in os.listdir(images_directory) if os.path.isfile(os.path.join(images_directory, f))]

    # Define a dictionary with custom captions for each image
    captions = {
        'ThesisApe.png': 'I proudly worked with the Dr Selas Bots and her epic idea on the illustrations for the chapter pages, bookcover for her PhD dissertation: ¨Nonhuman primate adenoviruses for use as oncolytic agents¨ in Amsterdam.',
        'amazona.jpg': 'La visión',
        'medusa.png': 'In 2019 I researched and illustrated the reproduction of the moon jellyfish in San Sebastian Donostia AQUARIUM in Spain. The piece is digitally exposed next to the large jellyfish tank in 4 different languages; Spanish, Euskera, French and English.',
        'colClimateChange.png': 'Climate Change',
        'boremeSelf.png': 'In 2018 I had the opportunity to work with a very special restaurant in Bordeaux-France, now I want to share the concept and result of the piece of wall that I painted. - Made with love and acrylics -',
        'siataCity.png': 'SIATA is a science and technology project that studies different environmental variables and alerts the community to possible dangers caused by these variables. In this illustration you can find some sensors that they manufacture and install themselves to be informed and to be able to protect the citizens of "El Valle de Aburrá". ',
        'boreme2.jpg': 'In 2018 I had the opportunity to work with a very special restaurant in Bordeaux-France, now I want to share the concept and result of the piece of wall that I painted.',
        'elkeKatTelt.png': 'I had the honor to make the logo for the beatiful project "Stichting Elke Kat Telt?" that works helping disadvantaged cats to have a safe and secure future.',
        'hidrologia.png': 'Working at SIATA I had the opportunity to make infographics hand by hand with an interdisciplinary team of scientists and communicators. The results served to explain to the community different concepts of geosciences.',
        'uitsmijter.png': 'After so many years working behind the computer I wanted to try something new. This feeling led me to my first experience cooking in a restaurant. These months were completely full of enriching knowledge, it was challenging, but I enjoyed it very much. And the best part was finishing with the opportunity to see my poster hanging around the streets of the city of Amsterdam for the first time.',        
        'hydration.jpg': 'Working at SIATA I had the opportunity to make infographics hand by hand with an interdisciplinary team of scientists and communicators. The results served to explain to the community different concepts of geosciences.',
        'siata_ground_levels.png': 'Design of the calendar with the relief of the Picacho hill in the city of Medellín',
        'siata2020.png': 'Design for SIATA, Sistema de Alerta Temprana del Valle de Aburrá',
         }

    # Convert captions into an ordered list of filenames
    caption_order = list(captions.keys())  

    # Create a list of dictionaries with image information
    images = [
        {'filename': file, 'thumbnail_filename': file, 'caption': captions.get(file)}
        for file in caption_order
    ]

    return render(request, 'portfolio/my_work.html', {'images': images})

def contact(request):
    return render(request, 'portfolio/contact.html')

def about_me(request):
    return render(request, 'portfolio/about_me.html')

def shop(request):
    return render(request, 'portfolio/shop.html')
