from django.db import models
from django.shortcuts import  reverse, get_object_or_404

# Create your models here.

class AuthorModel(models.Model):
    
    name = models.CharField(max_length=100)
    bdate = models.DateField(null=True) 
    image = models.ImageField(upload_to='bookstore/images/', null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True) 
    updated_at = models.DateTimeField(auto_now=True, null=True)  

    def __str__(self):
        return f"{self.name}"
    
    @property
    def image_url(self):
        return f'/media/{self.image}'
    
    @classmethod
    def get_author_by_id(cls, id):
        return get_object_or_404(cls, id=id)
    

class BookModel(models.Model):
    
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    author = models.ForeignKey(AuthorModel, on_delete=models.CASCADE, related_name='books')  
    pages = models.IntegerField(default=100, null=True)
    image = models.ImageField(upload_to='bookstore/images/', null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True) 
    updated_at = models.DateTimeField(auto_now=True, null=True)  

    def __str__(self):
        return f"{self.name}"
    
    @property
    def image_url(self):
        return f'/media/{self.image}'
    
    @classmethod
    def get_book_by_id(cls, id):
        return get_object_or_404(cls, id=id)
    




