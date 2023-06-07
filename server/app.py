from flask import Flask, jsonify, request
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
    repositories = proxy.get_repos()
    return jsonify(repositories)

# All pull request route.
@app.route('/pulls', methods=['GET'])
def get_pull_requests():
    # Send a GET request to the Reverse Proxy API to get all repos.
    repos = proxy.get_repos()

    # Create an empty list to store all pull requests.
    pull_requests = []

    for repo in repos:
      # Send a GET request to get all pull requests for the repo.
      prs = proxy.get_pulls(f'repos/MarkNisarg/{repo["name"]}/pulls?state=open')
      pull_requests.extend(prs)

    return jsonify(pull_requests)

# Pull request for specific repo route.
@app.route('/pulls/<repo>', methods=['GET'])
def get_pulls_for_repo(repo):
    pull_requests = proxy.get_pulls(f'repos/MarkNisarg/{repo}/pulls?state=open')
    return jsonify(pull_requests)

# Leave a comment on a pull request.
@app.route('/pulls/<repo>/comment', methods=['POST'])
def post_pr_review_comment(repo):
    pull_number = request.json['pull_number']
    comment = request.json['comment']
    path = f'repos/MarkNisarg/{repo}/issues/{pull_number}/comments'

    return proxy.post_comment(path, comment)

# Merge pull request.
@app.route('/pulls/<repo>/merge', methods=['PUT'])
def merge_pull_request(repo):
    pull_number = request.json['pull_number']
    path = f'repos/MarkNisarg/{repo}/pulls/{pull_number}/merge'

    return proxy.merge_pr(path)

# Close pull request.
@app.route('/pulls/<repo>/close', methods=['PATCH'])
def close_pull_request(repo):
    pull_number = request.json['pull_number']
    path = f'repos/MarkNisarg/{repo}/pulls/{pull_number}'

    return proxy.close_pr(path)

if __name__ == '__main__':
    app.run(host='localhost', port=9095, debug=True)
