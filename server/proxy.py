import os
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

  # Get data from Github using REST API.
  def get_data(self, path):
    url = f'{self.base_url}{path}'
    response = requests.get(url, headers=self.headers)
    return response.json()
