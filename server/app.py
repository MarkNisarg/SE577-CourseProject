from flask import Flask, jsonify
from flask_cors import CORS
from proxy import GithubProxy

# Instantiate the app.
app = Flask(__name__)
app.config.from_object(__name__)
app.config['JSON_SORT_KEYS'] = False

# Enable CORS.
CORS(app, resources={r'/*': {'origins': '*'}})

# Instantiate proxy object.
proxy = GithubProxy()

# Repositories route.
@app.route('/repos', methods=['GET'])
def get_repositories():
    repositories = proxy.get_data('user/repos')
    return jsonify(repositories)

# All request route.
@app.route('/pulls', methods=['GET'])
def get_pulls():
    # Send a GET request to the Reverse Proxy API to get all repos.
    repositories = proxy.get_data('user/repos')

    # Create an empty list to store all pull requests.
    pull_requests = []

    for repo in repositories:
      # Send a GET request to the GitHub API to get all pull requests for the repo.
      pr_response = proxy.get_data(f'repos/MarkNisarg/{repo["name"]}/pulls?state=all')

      # Add the pull requests to the list.
      pull_requests.extend(pr_response)

    # Return the list of pull requests as JSON
    return jsonify(pull_requests)

# Pull request for specific repo route.
@app.route('/pulls/<path:repo>', methods=['GET'])
def get_pull_for_repo(repo):
    # Send a GET request to the Reverse Proxy API to get all repos.
    pull_requests = proxy.get_data(f'repos/MarkNisarg/{repo}/pulls?state=all')

    # Return the list of pull requests as JSON
    return jsonify(pull_requests)

if __name__ == '__main__':
    app.run(host='localhost', port=9095, debug=True)
