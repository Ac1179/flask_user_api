from app import db

class BaseDAO:
    def __init__(self, model):
        self.model = model

    def get_by_id(self, pk):
        return self.model.query.get(pk)

    def get_by_field(self, **kwargs):
        return self.model.query.filter_by(**kwargs).first()

    def add(self, obj):
        try:
            db.session.add(obj)
            db.session.commit()
            return obj
        except Exception as e:
            db.session.rollback()
            raise e

    def update(self):
        try:
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            raise e

    def delete(self, obj):
        try:
            db.session.delete(obj)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            raise e