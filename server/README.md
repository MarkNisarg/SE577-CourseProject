# Flask GitHub Proxy API

This is a simple Flask application that serves as a proxy for the GitHub API. It provides endpoints to retrieve repository and pull request data from the GitHub API.

## Prerequisites

To run this web service, you need to have the following software installed:

* Python 3.x
* Flask (`pip install flask`)
* Flask-CORS (`pip install -U flask-cors`)
* Requests (`pip install requests`)
* Python-dotenv (`pip install python-dotenv`)
* GitHub API token (you can generate one [here](https://github.com/settings/tokens))

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/MarkNisarg/SE577-CourseProject.git
   ```

2. Navigate to the project directory:

   ```shell
   cd SE577-CourseProject/server
   ```

3. Install the dependencies:

   ```shell
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the backend root directory (`server`) and provide the following environment variables:

   ```plaintext
   GITHUB_API_URL=<GitHub API base URL>
   GITHUB_TOKEN=<GitHub access token>
   ```

   Replace `<GitHub API base URL>` with the base URL of the GitHub API (e.g., `https://api.github.com/`) and `<GitHub access token>` with your personal access token.

## Usage

To run the application, use the following command:

```
python app.py
```
The application will be available at http://localhost:9095/.

## Endpoints

### Get repositories

- URL: `/repos`
- Method: GET
- Description: Retrieves all repositories for the authenticated user.
- Response: JSON array containing repository information.

### Get all pull requests

- URL: `/pulls`
- Method: GET
- Description: Retrieves all pull requests for all repositories of the authenticated user.
- Response: JSON array containing pull request information.

### Get pull requests for a specific repository

- URL: `/pulls/<repo>`
- Method: GET
- Description: Retrieves all pull requests for a specific repository of the authenticated user.
- Parameters:
  - `repo`: The repository name.
- Response: JSON array containing pull request information.

