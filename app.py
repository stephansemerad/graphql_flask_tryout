
'''
Thanks to
https://www.jorgehernandezramirez.com/2020/03/21/flask-and-graphql-filters-graphene-sqlalchemy-filters/
https://www.apollographql.com/blog/graphql/python/complete-api-guide/

'''


from app import app

if __name__ == "__main__":
    app.run(    #host='0.0.0.0',
                port=5000,
                debug=True
            )
