import graphene
from graphene_django.types import DjangoObjectType, ObjectType

from ..models import Book

class BookTypeMutation(DjangoObjectType):
    class Meta:
        model = Book

class Query(ObjectType):
    books = graphene.List(BookTypeMutation)

    def resolve_books(self, info, **kwargs):
        return Book.objects.all()