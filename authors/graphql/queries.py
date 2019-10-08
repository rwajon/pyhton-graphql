import graphene
from graphene_django.types import DjangoObjectType, ObjectType

from ..models import Author

class AuthorType(DjangoObjectType):
    class Meta:
        model = Author

class Query(ObjectType):
    authors = graphene.List(AuthorType)
    search_author = graphene.List(AuthorType, name=graphene.String(), id=graphene.ID())

    def resolve_authors(self, info, **kwargs):
        return Author.objects.all()
    
    def resolve_search_author(self, info, **kwargs):
        name = kwargs.get('name', '')
        id = kwargs.get('id', '')
        return Author.objects.filter(name__icontains=name) if name else Author.objects.filter(id=id)