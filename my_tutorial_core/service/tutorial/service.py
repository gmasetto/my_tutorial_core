from my_tutorial_core.service.tutorial.model import Tutorial
from my_tutorial_core.db import db


class TutorialService(object):

    def add(self, title, description):
        tutorial = Tutorial(title=title, description=description)
        db.session.add(tutorial)
        db.session.commit()
        return tutorial

    def get_all(self):
        return Tutorial.query.all()

    def get_by_id(self, id):
        return Tutorial.query.filter(Tutorial.id == id).one()
