from flask import Flask, request
from flask_restful import Resource, Api
from flask_restful import fields, marshal_with

from nf_core import schema, list

app = Flask(__name__)
api = Api(app)

# get the parameters to the nextflow list function

resource_fields = {
    'filter_by':   fields.List,
    'sort_by':    fields.String,
    'as_json': fields.Boolean,
}

class NextflowWorkflows(Resource):
    @marshal_with(resource_fields)
    def get(self,  **kwargs):
         # do some sanity checks here
        data = {'filter_by': kwargs['filter_by']} 
        pl = PipelineSchema(inputparams = data)
        
        if not pl.validate_params():
            print('error')
            return 1
        return {workflows: nf_core.list.list_workflows(filter_by=data['filter_by'])}



api.add_resource(NextflowWorkflows, '/')

if __name__ == '__main__':
    app.run(debug=True, host = '0.0.0.0',port = 5005)

