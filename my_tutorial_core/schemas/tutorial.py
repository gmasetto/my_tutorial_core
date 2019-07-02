from my_tutorial_core.restplus import api
from flask_restplus import fields

tutorial_schemas = api.model('Tutorial', {
    'id': fields.Integer(readonly=True),
    'title': fields.String(required=True, description='Title tutorial'),
    'description': fields.String(required=True, description='Description tutorial')
})
