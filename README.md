# GitHub REST API Handler

## Prerequisites

* Node.js (v14 or higher)
* Python (v3 or higher)

## Installation

1. Clone the repository `git clone https://github.com/MarkNisarg/SE577-CourseProject.git`
2. Checkout to `proj-release-2` branch
3. Navigate to the `server` directory and run `pip install -r requirements.txt` to install the necessary dependencies for the backend
4. Navigate to the `github-rest-api-handler` directory and run `yarn` to install the necessary dependencies for the frontend

## Usage

1. Navigate to the `server` directory and run `python app.py` to start backend server
2. In a separate terminal window, navigate to the `github-rest-api-handler` directory and run `yarn dev` to start the frontend development server
3. Open your web browser and navigate to `http://localhost:9095/repo` to get all repositories data
4. Open your web browser and navigate to Vue.js app

## Features

* Feature 1: Under `Repositories` page, get all repositories data from web service
* Feature 2: Under `Pull Requests` page, render all pull requests for all repositories
* Feature 3: Under `Pull Requests` page, get every pull requests for specific repository using filter options

## API Endpoints

* `http://localhost:9095/repo`: Get all repositories data.
* `http://localhost:9095/pull`: Get all pull requests from all repositories.
* `http://localhost:9095/pull?repo=<example>`: Get all pull requests from `<example>` repository.

## Technologies Used

* Vue.js
* Python Flask
