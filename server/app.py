import os
from flask import Flask, json, jsonify, request
from flask_cors import CORS

# Instantiate the app.
app = Flask(__name__)
app.config.from_object(__name__)

# Enable CORS.
CORS(app, resources={r'/*': {'origins': '*'}})

# Repositories route.
@app.route('/repos', methods=['GET'])
def repositories():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, 'static', 'repositories.json')
    return json.load(open(json_url))

@app.errorhandler(404)
def invalid_route():
    return jsonify({'errorCode' : 404, 'message' : 'Route not found!'}), 404

# Pull requests route.
@app.route('/pull', methods=['GET'])
def pull_requests():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, 'static', 'pull_requests.json')
    pulls_data = json.load(open(json_url))
    repo = request.args.get('repo')
    if repo:
        pulls_data = [x for x in pulls_data if x['repo'].lower() == repo.lower()]
        if not pulls_data:
            return invalid_route()

    return pulls_data

if __name__ == '__main__':
    app.run(host='localhost', port=9095, debug=True)
