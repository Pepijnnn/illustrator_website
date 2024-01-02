import os
from django.shortcuts import render
from django.conf import settings

# def my_work(request):
#     return render(request, 'portfolio/my_work.html')
# def my_work(request):
#     images = [
#         {'filename': 'image1.png', 'thumbnail_filename': 'image1.png', 'caption': 'Image 1'},
#         {'filename': 'image2.png', 'thumbnail_filename': 'image2.png', 'caption': 'Image 2'},
#         # Add more images as needed
#     ]
#     return render(request, 'portfolio/my_work.html', {'images': images})

def my_work(request):
    # Path to the images directory using BASE_DIR
    images_directory = os.path.join(settings.BASE_DIR, 'static', 'portfolio', 'images')

    # Get a list of all files in the images directory
    image_files = [f for f in os.listdir(images_directory) if os.path.isfile(os.path.join(images_directory, f))][1:]

    # Create a list of dictionaries with image information
    images = [{'filename': file, 'thumbnail_filename': file, 'caption': f'Caption for {file}'}
              for file in image_files]

    return render(request, 'portfolio/my_work.html', {'images': images})

def contact(request):
    return render(request, 'portfolio/contact.html')

def about_me(request):
    return render(request, 'portfolio/about_me.html')

def shop(request):
    return render(request, 'portfolio/shop.html')
