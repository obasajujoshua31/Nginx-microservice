from todo.schema import Query, Mutation
import graphene

class Query(Query, graphene.ObjectType):
    pass

class Mutations(Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutations)
