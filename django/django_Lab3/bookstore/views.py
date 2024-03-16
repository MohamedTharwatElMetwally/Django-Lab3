from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from bookstore.models import BookModel, AuthorModel
from bookstore.forms import BookModelForm, AuthorModelForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def homePage(request):
    return render(request, r"bookstore/home.html")

def allBooks(request):
    books = BookModel.objects.all()
    return render(request, r"bookstore/all books.html", context={"books": books})

def allAuthors(request):
    authors = AuthorModel.objects.all()
    return render(request, r"bookstore/all authors.html", context={"authors": authors})


def getBook(request, id):
    try:
        book = BookModel.objects.get(id=id)
        author = AuthorModel.objects.get(id=book.author_id)
        return render(request, r"bookstore/book desc.html", context={"book": book, "author": author})
    except Exception as e:
        return HttpResponse(e)
    
@login_required(login_url='/users/login')
def addBook(request):

    form = BookModelForm()
    if request.method == 'POST':
        form = BookModelForm(request.POST, request.FILES)
        if form.is_valid():
            newbook = form.save()  
            url = reverse("all_books")
            return redirect(url)
    
    # request GET
    return render(request, r'bookstore/forms/add book.html', context={"form":form})

@login_required(login_url='/users/login')
def deleteBook(request, id):

    book = BookModel.objects.get(id=id)
    book.delete()

    # reverse name to the url
    url = reverse("all_books")
    return redirect(url)

@login_required(login_url='/users/login')
def editBook(request, id):

    book = BookModel.get_book_by_id(id)
    form = BookModelForm(instance=book) 

    if request.method == 'POST':
        form = BookModelForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            url = reverse("get_book", kwargs={'id': id})
            return redirect(url)

    # request GET
    return render(request, r"bookstore/forms/edit book.html", context={"form":form})

    
def getAuthor(request, id):
    try:
        author = AuthorModel.objects.get(id=id)
        books = BookModel.objects.filter(author_id=author.id)
        books = list(books.values_list('name', flat=True))
        return render(request, r"bookstore/author desc.html", context={"author": author, "books": books})
    except Exception as e:
        return HttpResponse(e)

@login_required(login_url='/users/login')
def addAuthor(request):

    form = AuthorModelForm()
    if request.method == 'POST':
        form = AuthorModelForm(request.POST, request.FILES)
        if form.is_valid():
            newauthor = form.save()  
            url = reverse("all_authors")
            return redirect(url)
    
    # request GET
    return render(request, r'bookstore/forms/add author.html', context={"form":form})

@login_required(login_url='/users/login')
def deleteAuthor(request, id):

    author = AuthorModel.objects.get(id=id)
    author.delete()

    # reverse name to the url
    url = reverse("all_authors")
    return redirect(url)

@login_required(login_url='/users/login')
def editAuthor(request, id):
    author = AuthorModel.get_author_by_id(id)
    form = AuthorModelForm(instance=author) 

    if request.method == 'POST':
        form = AuthorModelForm(request.POST, request.FILES, instance=author)
        if form.is_valid():
            form.save()
            url = reverse("get_author", kwargs={'id': id})
            return redirect(url)

    # request GET
    return render(request, r"bookstore/forms/edit author.html", context={"form":form})

    


