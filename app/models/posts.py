from app.extensions import db

class Post(db.Model):
    __tablename__="Posty"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    post = db.Column(db.String(1000), unique=True,nullable=False)
    category = db.Column(db.String(20), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    author = db.relationship("User", back_populates="posts")


