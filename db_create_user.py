from app import db
from models.user import User
from models.comment import Comment

# insert data
db.session.add(User(name="adriana1",
                    email="adriana1@gmail.com", password="adriana1",
                    comments=[Comment(id=1, title='first comment')]
                   )
               )

# commit the changes
db.session.commit()
