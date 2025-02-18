from django.shortcuts import render, get_object_or_404
from .models import Book
from django.http import Http404
from django.db.models import Avg

# Create your views here.
def index(request):
    books = Book.objects.all().order_by("-rating") # -rating is for descending order
    num_books = books.count()
    average_rating = books.aggregate(Avg("rating"))
    return render(request, "book_outlet/index.html", 
                  {"books": books,
                   "total_books": num_books,
                   "average_rating": average_rating
                   })

def book_detail(request, slug):
    
    try:
        book = Book.objects.get(slug=slug) # pk is the primary key of the book
    except:
        raise Http404()
    
    # or a different way to handle the error bellow 
    # book = get_object_or_404(Book, pk=id)
    return render(request, "book_outlet/book_detail.html", 
                  {"title": book.title,
                   "author": book.author,
                   "rating": book.rating,
                   "is_bestselling": book.is_bestselling})

# def create_book(request):
