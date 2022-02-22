from app import app
from flask_graphql import GraphQLView
from app.schema import schema
from flask import render_template, jsonify, request

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/endpoint")
def endpoint():
    query = request.args.get('query', None)
    
    if not query: return 'missing query'
    
    result = schema.execute(query).data
    
    return jsonify(result)


app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True
    )
)
