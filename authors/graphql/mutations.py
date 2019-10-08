import graphene
from graphene_django.types import DjangoObjectType, ObjectType

from .queries import AuthorType
from ..models import Author

class AuthorInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()

class CreateAuthor(graphene.Mutation):
    class Arguments:
        # input = AuthorInput(required=True)
        id = graphene.ID()
        name = graphene.String()
    
    author = graphene.Field(AuthorType)

    @staticmethod
    def mutate(root, info, name=None):
        author_instance = Author(name=name)
        author_instance.save()
        return CreateAuthor(author=author_instance)

class Mutation(graphene.ObjectType):
    create_author = CreateAuthor.Field()