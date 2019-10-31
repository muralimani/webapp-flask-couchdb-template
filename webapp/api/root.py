"About API endpoints."

import http.client

import flask

import utils
import about


blueprint = flask.Blueprint('api', __name__)

@blueprint.route('/api')
def root():
    "API root."
    items = {
        'schema': {
            'root': {'href': utils.url_for('api_schema.root')},
            'logs': {'href': utils.url_for('api_schema.logs')},
            'user': {'href': utils.url_for('api_schema.user')},
            'about/software': {'href': utils.url_for('api_schema.about_software')}
        },
        'about': {
            'software': {'href': utils.url_for('api_about.software')}
        }
    }
    if flask.g.current_user:
        items['user'] = {
            'username': flask.g.current_user['username'],
            'href': utils.url_for('api_user.profile',
                                  username=flask.g.current_user['username'])
        }
    if flask.g.is_admin:
        items['users'] = {
            'href': utils.url_for('api_user.all')
        }
    return utils.jsonify(utils.get_json(**items), schema='/root')