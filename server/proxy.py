import os
from flask import jsonify
import requests
from dotenv import load_dotenv

# Load environment variables from .env file.
load_dotenv()

class GithubProxy:
  def __init__(self):
    self.base_url = os.getenv('GITHUB_API_URL')
    self.token = os.getenv('GITHUB_TOKEN')
    self.headers = {
      'Authorization': f'Bearer {self.token}',
      'Accept': 'application/vnd.github+json'
    }

  # Get details of all repos.
  def get_repos(self):
    path = 'user/repos'
    response = requests.get(f'{self.base_url}{path}', headers=self.headers)
    return response.json()

  # Get all pull requests for a repository.
  def get_pulls(self, path):
    response = requests.get(f'{self.base_url}{path}', headers=self.headers)
    return response.json()

  # Post a comment to a pull request.
  def post_comment(self, path, comment):
    url = f'{self.base_url}{path}'
    payload = {'body': comment}
    response = requests.post(url, headers=self.headers, json=payload)

    if response.status_code == 201:
        return 'Comment posted successfully! Please check on GitHub!'
    else:
        return 'Failed to post comment!', 500

  # Merge pull request.
  def merge_pr(self, path):
    url = f'{self.base_url}{path}'
    print(url)
    response = requests.put(url, headers=self.headers)

    if response.status_code == 200:
        return 'Pull request merged successfully! Please check on GitHub!'
    else:
        return 'Failed to merge pull request!', 500

  # Post a comment to a pull request.
  def close_pr(self, path):
    url = f'{self.base_url}{path}'
    payload = {'state': 'closed'}
    response = requests.patch(url, headers=self.headers, json=payload)

    if response.status_code == 200:
        return 'Pull request closed successfully! Please check on GitHub!'
    else:
        return 'Failed to close pull request!', 500
