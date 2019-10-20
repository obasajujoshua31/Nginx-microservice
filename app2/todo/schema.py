import graphene
import graphql
from graphene_django import DjangoObjectType
from .models import Todo


class TodoObjectType(DjangoObjectType):
    class Meta:
        model = Todo


class Query(graphene.ObjectType):
    all_todos = graphene.List(TodoObjectType)
    get_todo = graphene.Field(TodoObjectType, id=graphene.Int())

    def resolve_all_todos(self, info):
        # Make a request to the user service and get user object
        # If notRaise GraphQl Error
        user = {'id': 1}
        return Todo.objects.filter(user_id__exact=user['id'])

    def resolve_get_todo(self, info, id):
        user = {'id': 1}
        todo = Todo.objects.filter(user_id__exact=user['id'], id__exact=id)
        if not todo:
            raise graphql.GraphQLError('Todo not found')
        return todo[0]


class CreateTodo(graphene.Mutation):
    ''' Create A New Todo '''
    class Arguments:
        item_name = graphene.String()
        completed = graphene.Boolean()
        user_id = graphene.Int()

    todo = graphene.Field(TodoObjectType)

    def mutate(root, info, **args):
        todo = Todo(item_name=args['item_name'], completed=False, user_id=1)
        todo.save()
        return CreateTodo(todo=todo)


class UpdateTodo(graphene.Mutation):
    ''' Update A Todo '''
    class Arguments:
        todo_id = graphene.Int(required=True)
        item_name = graphene.String()
        completed = graphene.Boolean()

    todo = graphene.Field(TodoObjectType)

    def mutate(self, root, info, **args):
        todo = Todo.objects.filter(user_id__exact=args.get(
            'user_id', 1), id__exact=args.get('todo_id'))
        if not todo:
            raise graphql.GraphQLError('Todo not found')
        todo = todo[0].update_item(item_name=args.get('item_name'))
        return UpdateTodo(todo=todo)


class DeleteTodo(graphene.Mutation):
    ''' Delete A Todo '''
    class Arguments:
        todo_id = graphene.Int(required=True)
        item_name = graphene.String()
        completed = graphene.Boolean()

    todo = graphene.String()

    def mutate(self, root, info, **args):
        todo = Todo.objects.filter(user_id__exact=args.get('user_id', 1),
                                   id__exact=args.get('todo_id'))
        if not todo:
            raise graphql.GraphQLError('Todo not found')
        todo[0].delete()

        return DeleteTodo(todo='Todo was deleted successfully')


class Mutation(graphene.ObjectType):
    create_todo = CreateTodo.Field()
    update_todo = UpdateTodo.Field()
    delete_todo = DeleteTodo.Field()
