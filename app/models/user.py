from app import db, bc
import uuid

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    public_id = db.Column(db.String, unique=True, nullable=False)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=True)
    display_name = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False)
    is_active = db.Column(db.Boolean, nullable=False)
    token = db.Column(db.String, nullable=True)

    def __init__(self, username, password, display_name, is_admin):
        self.public_id = str(uuid.uuid4())
        self.username = username
        self.password = bc.generate_password_hash(password).decode('utf-8')
        self.display_name = display_name
        self.is_admin = is_admin
        self.is_active = True
        self.token = None