

def initialize():
    from app.model import db, UserModel
    import random
    
    db.create_all()
    
    names = ['Olivia','Emma','Ava','Charlotte','Sophia','Amelia','Isabella','Mia','Evelyn','Harper']
    surnames = ['Smith','Johnson','Williams','Brown','Jones','Garcia','Miller','Davis','Rodriguez','Martinez', 'Hernandez', 'Lopez','Gonzalez', 'Wilson', 'Anderson', 'Thomas', 'Taylor', 'Moore']
    
    check = db.session.query(UserModel).all()
    if check == []:
        for name in names:
            for surname in surnames:        
                age = random.randint(15, 100)
                print('name: ', name, ' surname: ', surname, ' age: ', age)
                db.session.add(UserModel(name=f'{name}', surname=f'{surname}', age=age))
    db.session.commit()
