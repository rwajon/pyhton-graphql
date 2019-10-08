from graphene import ObjectType, Schema

from authors.graphql.schema import Query as AuthorQuery, Mutation as AuthorMutation
from books.graphql.schema import Query as BookQuery, Mutation as BookMutation


class Query(AuthorQuery, BookQuery,  ObjectType):
    pass

class Mutation(AuthorMutation, BookMutation, ObjectType):
    pass

schema = Schema(query=Query, mutation=Mutation)