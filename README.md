# GitHub REST API Handler

## Prerequisites

* Node.js (v14 or higher)
* Python (v3 or higher)

## Installation

1. Clone the repository `git clone https://github.com/MarkNisarg/SE577-CourseProject.git`
2. Checkout to `proj-release-3` or `main` branch
3. Navigate to the `server` directory and run `pip install -r requirements.txt` to install the necessary dependencies for the backend
4. Navigate to the `client` directory and run `yarn` to install the necessary dependencies for the frontend

## Usage

1. Navigate to the `server` directory and run `python app.py` to start backend server
2. In a separate terminal window, navigate to the `client` directory and run `yarn dev` to start the frontend development server
3. Open your web browser and navigate to `http://localhost:9095/repos` to get all repositories data
4. Open your web browser and navigate to `http://localhost:9095/pulls` to get all pull requests from all repositories data
5. Open your web browser and navigate to `http://localhost:9095/pulls/<repo>` to get all pull requests for specific `<repo>`
4. Open your web browser and navigate to Vue.js app and check for Repositories and Pull Requests pages.

## Features

* Feature 1: Under `Repositories` page, get all repositories data from web service
* Feature 2: Under `Pull Requests` page, render all pull requests for all repositories
* Feature 3: Under `Pull Requests` page, get every pull requests for specific repository using filter options

## API Endpoints

* `http://localhost:9095/repos`: Get all repositories data.
* `http://localhost:9095/pulls`: Get all pull requests from all repositories.
* `http://localhost:9095/pulls/<repo>`: Get all pull requests from `<repo>` repository.

## Technologies Used

* Vue.js
* Python Flask
