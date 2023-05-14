# Flask Web Service

This is a simple Flask web service that provides a RESTful API for interacting with a GitHub APIs. It uses Python 3 and Flask framework to handle HTTP requests and responses.

## Prerequisites

To run this web service, you need to have the following software installed:

* Python 3
* Flask (`pip install flask`)
* Flask-CORS (`pip install -U flask-cors`)

## Installation

To install the Flask web service, you can use pip:

```
pip install -r requirements.txt
```

## Running the Application

To run the application, use the following command:

```
python app.py
```
The application will be available at http://localhost:9095/.

## Features

* Feature 1: Under `/repositories` page, get all repositories data
* Feature 2: Under `/pull` page, get all pull requests for all repositories
* Feature 3: Under `/pull?repo=vaccination` page, get all pull requests for `vaccination` repository using filter options

## API Endpoints

* `http://localhost:9095/repo`: Get all repositories data.
* `http://localhost:9095/pull`: Get all pull requests from all repositories.
* `http://localhost:9095/pull?repo=<example>`: Get all pull requests from `<example>` repository.
