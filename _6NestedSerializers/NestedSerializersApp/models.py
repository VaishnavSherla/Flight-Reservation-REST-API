from django.db import models

# Create your models here.
class Author(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.firstName} {self.lastName}'
    
class Book(models.Model):
    title = models.CharField(max_length=20)
    ratings = models.CharField(max_length=10)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
