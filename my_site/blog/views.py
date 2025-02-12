from django.shortcuts import render
from datetime import date

# Create your views here.

all_posts = [
    {
        "slug": "hiking-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Nikolas",
        "date": date(2025, 2, 12),
        "title": "Mountain Hiking",
        "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for that!",
        "content": """
        Lorem ipsum dolor sit amet consectetur adipisicing elit. 
        Quisquam, quos."""
    },
    {
        "slug": "coding",
        "image": "coding.jpg",
        "author": "Nikolas",
        "date": date(2025, 2, 15),
        "title": "Coding again",
        "excerpt": "I love coding!",
        "content": """
        Lorem ipsum dolor sit amet consectetur adipisicing elit. 
        Quisquam, quos."""
    },
    {
        "slug": "woods",
        "image": "woods.jpg",
        "author": "Nikolas",
        "date": date(2025, 2, 5),
        "title": "Living in the woods",
        "excerpt": "Timber is the best!",
        "content": """
        Lorem ipsum dolor sit amet consectetur adipisicing elit. 
        Quisquam, quos."""
    }
]

def get_date(post):
    return post['date']


def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html",{
        "posts": latest_posts
    })



def posts(request):
    return render(request, "blog/all-posts.html",{
        "all_posts": all_posts
    }) 



def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html",{
        "post": identified_post
    })

