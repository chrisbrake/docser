import responder
from marshmallow import Schema, fields

from ._version import get_versions

api = responder.API(title='Documentation Server',
                    version=get_versions()['version'],
                    openapi='3.0',
                    docs_route='/api/docs')
fake_db = [{'name': 'example'}]


@api.schema("Project")
class ProjectSchema(Schema):
    name = fields.Str()


@api.route("/api/projects")
async def projects(req, resp):
    """
    The end point for all the projects hosted here
    ---
    get:
        description: Get all the stored projects
        responses:
            200:
                description: All the stored projects
                schema:
                    $ref = "#/components/schemas/Project"
    """
    resp.media = [ProjectSchema().dump(i) for i in fake_db]

if __name__ == '__main__':
    api.run(address='0.0.0.0', port=8080)
