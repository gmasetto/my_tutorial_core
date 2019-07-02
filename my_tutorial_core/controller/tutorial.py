from my_tutorial_core.restplus import api
from flask_restplus import Resource
from my_tutorial_core.schemas.tutorial import tutorial_schemas
from my_tutorial_core.service.tutorial.service import TutorialService

ns_tutorial = api.namespace('Tutorial', description='Tutorials')


@ns_tutorial.route('/')
class TutorialCollection(Resource):

    def __init__(self, api=None, *args, **kwargs):
        super(TutorialCollection, self).__init__(api, args, kwargs)
        self.service = TutorialService()

    @api.marshal_list_with(tutorial_schemas)
    def get(self):
        return self.service.get_all()

    @api.expect(tutorial_schemas)
    @api.marshal_with(tutorial_schemas, code=201)
    def post(self):
        return self.service.add(api.payload['title'], api.payload['description'])


@ns_tutorial.route('/<int:id>')
@api.response(404, 'Tutorial not found.')
class TutorialItem(Resource):

    def __init__(self, api=None, *args, **kwargs):
        super(TutorialItem, self).__init__(api, args, kwargs)
        self.service = TutorialService()

    @api.marshal_with(tutorial_schemas)
    def get(self, id):
        return self.service.get_by_id(id)
