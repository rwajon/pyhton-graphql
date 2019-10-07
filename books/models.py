from django.db import models
from authors.models import Author

class Book(models.Model):
    title = models.CharField(max_length=100)
    synopsis = models.TextField()
    author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)
    published_date = models.DateField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title', )
