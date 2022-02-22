 
from app import db
 
class UserModel(db.Model):
    __tablename__ = 'user'
    userid      = db.Column(db.Integer, primary_key=True)
    name        = db.Column(db.String(256))
    surname     = db.Column(db.String(256))
    age         = db.Column(db.Integer)
 
    def __repr__(self):
        return '<User {} {} {} {}>'.format(self.id, self.name, self.surname, self.age)


from graphene_sqlalchemy_filter import FilterSet
from app.model import UserModel
ALL_OPERATIONS = ['eq', 'ne', 'like', 'ilike', 'is_null', 'in', 'not_in', 'lt', 'lte', 'gt', 'gte', 'range'] 

class UserFilter(FilterSet):
    class Meta:
        model = UserModel
        fields = {
            'userid': ALL_OPERATIONS,
            'name': ALL_OPERATIONS,
            'surname': ALL_OPERATIONS,
            'age': ALL_OPERATIONS,
        }