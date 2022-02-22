import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from graphene_sqlalchemy_filter import FilterableConnectionField
from app.model import UserModel, UserFilter
 
class User(SQLAlchemyObjectType):
    class Meta:
        model = UserModel
        interfaces = (graphene.relay.Node,)
 
class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    user = FilterableConnectionField(connection=User, filters=UserFilter(), sort=User.sort_argument())
 
 
schema = graphene.Schema(query=Query, types=[User])