from app import db
import datetime
import uuid

class CategoryTitle(db.Model):
    __tablename__ = 'category_title'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    public_id = db.Column(db.String, unique=True, nullable=False)
    title_id = db.Column(db.Integer, db.ForeignKey('title.id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_on = db.Column(db.DateTime, nullable=False)
    modified_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    modified_on = db.Column(db.DateTime, nullable=True)
    is_deleted = db.Column(db.Boolean, nullable=False)
    deleted_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    deleted_on = db.Column(db.DateTime, nullable=True)

    def __init__(self, category_id, title_id, created_by, created_on):
        self.public_id = str(uuid.uuid4())
        self.title_id = title_id
        self.category_id = category_id
        self.created_by = created_by
        self.created_on = datetime.datetime.now()
        self.modified_by = None
        self.modified_on = None
        self.is_deleted = False
        self.deleted_by = None
        self.deleted_on = None