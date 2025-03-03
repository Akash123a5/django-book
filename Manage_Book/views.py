from django.shortcuts import render,redirect
from .models import *


# Create your views here.

def manage_book(request):
    books = Book.objects.all()  
    context = {'books': books}  
    return render(request, 'index.html', context) 




def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        isbn = request.POST.get('isbn')
        book = Book(title=title, author=author, isbn=isbn)
        book.save()
        return redirect('home')
    return render(request, 'index.html')


def edit_book(request, id):
    book = Book.objects.all()
    contaxt = {'book': book}
    return render(request, 'index.html', contaxt)


def update_book(request, id):
    emp = Book.objects.get(id=id)
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        isbn = request.POST.get('isbn')
        book = Book(id =id,title=title, author=author, isbn=isbn)
        book.save()
        return redirect('home')
    return render(request, 'index.html')


def delete_book(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('home')



def delete_all(request):
    book = Book.objects.all()
    book.delete()
    return redirect('home')

