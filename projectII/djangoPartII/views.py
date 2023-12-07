from django.shortcuts import render
from django.http import HttpResponse
from djangoPartII.models import AccessRecord, Topic, webpage, Friends
from djangoPartII import forms
from djangoPartII.forms import NewUser
import instaloader
import os

# Create your views here.

def index(request):
    return render(request, 'djangoPartII/index.html')

def help(request):
    return render(request, 'djangoPartII/help.html')

def research(request):
    webpage_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpage_list}
    return render(request, 'djangoPartII/research.html', context=date_dict)

def friends(request):
    form = NewUser()

    if request.method == "POST":
        form = NewUser(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("Error buddy!")
    return render(request, 'djangoPartII/friends.html', {'form':form})

def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            print("validation success")
            print("NAME: " + form.cleaned_data['name'])
            print("EMAIL: " + form.cleaned_data['email'])
            print("TEXT: " + form.cleaned_data['text'])


        
    return render(request, 'djangoPartII/form.html', {'form': form})


def download_instagram_posts(username):
    loader = instaloader.Instaloader()

    try:
        # Retrieve the profile of the specified username
        profile = instaloader.Profile.from_username(loader.context, username)

        # Create a folder to store downloaded images
        folder_path = os.path.join("media", "instagram_posts", username)
        os.makedirs(folder_path, exist_ok=True)

        # Download each post
        for post in profile.get_posts():
            loader.download_post(post, target=folder_path)

        print(f"Download complete. Images saved in: {folder_path}")
    except Exception as e:
        print(f"Error: {e}")

def instagram_posts_view(request, username):
    download_instagram_posts("abilash_krishnann")

    # Assuming the images are saved in the 'media/instagram_posts/username/' folder
    image_folder_path = os.path.join("media", "instagram_posts", username)

    # List all files in the folder
    image_files = [f for f in os.listdir(image_folder_path) if os.path.isfile(os.path.join(image_folder_path, f))]

    # Create a list of image paths
    image_paths = [os.path.join(image_folder_path, image_file) for image_file in image_files]

    return render(request, 'instagram_post.html', {'image_paths': image_paths})
