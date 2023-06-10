# GitHub REST API Handler - Final Release

## Introduction

GitHub REST API Handler is a web application that allows users to interact with the GitHub API and perform various operations on repositories and pull requests. The application provides a user-friendly interface for managing repositories, viewing pull requests, posting comments, merging pull requests, and closing pull requests. It is built using Vue.js for the frontend and Python Flask for the backend.

## Prerequisites

Before running the GitHub REST API Handler, ensure that the following prerequisites are met:

* Node.js (v14 or higher) is installed.
* Python (v3 or higher) is installed.

## Installation

To install and set up the GitHub REST API Handler, follow these steps:

1. Clone the repository:

   ```shell
   git clone https://github.com/MarkNisarg/SE577-CourseProject.git
   ```

2. Checkout to the `proj-final` or `main` branch:

   ```shell
   git checkout proj-final
   ```

3. Navigate to the `server` directory and install the necessary dependencies for the backend:

   ```shell
   pip install -r requirements.txt
   ```

   For more information, refer to the `README.md` file in the `server` directory.

4. Navigate to the `client` directory and install the necessary dependencies for the frontend:

   ```shell
   yarn
   ```

   For more information, refer to the `README.md` file in the `client` directory.

## Usage

To run the GitHub REST API Handler, follow these steps:

1. Start the backend server:

   ```shell
   cd server
   python app.py
   ```

2. In a separate terminal window, start the frontend development server:

   ```shell
   cd client
   yarn dev
   ```

3. Open your web browser and navigate to `http://localhost:9095/repos` to access the application.

## Features

The GitHub REST API Handler provides the following features:

1. **Repositories Page**: Displays all repositories data retrieved from the GitHub API.

2. **Pull Requests Page**: Renders all open pull requests from all repositories.

3. **Filter Options**: Allows users to filter pull requests by repository to view only the pull requests for a specific repository.

4. **Post Comment**: Enables users to post comments on a particular pull request.

5. **Merge Pull Request**: Allows users to merge a specific pull request.

6. **Close Pull Request**: Enables users to close a specific pull request.

## API Endpoints

The GitHub REST API Handler includes the following API endpoints:

* `http://localhost:9095/repos`: Retrieves all repositories data.

* `http://localhost:9095/pulls`: Fetches all open pull requests from all repositories.

* `http://localhost:9095/pulls/<repo>`: Retrieves all open pull requests from a specific repository.

* `http://localhost:9095/pulls/<repo>/comment`: Posts a comment on a pull request of a specific repository.

* `http://localhost:9095/pulls/<repo>/merge`: Merges a pull request of a specific repository.

* `http://localhost:9095/pulls/<repo>/close`: Closes a pull request of a specific repository.

## Technologies Used

The GitHub REST API Handler utilizes the following technologies:

* **Vue.js**: A JavaScript framework for building user interfaces.

* **Python Flask**: A web framework for building server-side applications.

## Architecture Description

The GitHub REST API Handler follows a client-server architecture, with the frontend serving as the client and the backend serving as the server. The client and server components communicate with each other through HTTP requests.

### Models

To refer architectural model, kindly locate the `architectural-model.pdf` document within the project's roor directory, encompassing the C4 diagrams.

### Architecture Decisions

1. **Frontend Framework**: Vue.js was chosen as the frontend framework for its simplicity, reactivity, and component-based architecture. It provides a smooth development experience and allows for the creation of interactive user interfaces.

2. **Backend Framework**: Python Flask was selected as the backend framework due to its lightweight nature, simplicity, and ease of use. Flask is well-suited for building small to medium-sized applications and provides the necessary functionalities for handling HTTP requests and interacting with the GitHub API.

3. **Client-Server Architecture**: The application follows a client-server architecture, with the frontend and backend components separated. This separation enables independent development, scalability, and easy maintenance of the application.

4. **REST API**: The backend exposes a RESTful API to handle requests from the frontend. REST principles are followed, where different endpoints are provided for retrieving repositories, pull requests, posting comments, merging pull requests, and closing pull requests. This allows for a standardized and predictable communication between the frontend and backend.

### Quality Attributes

1. **Usability**: The application aims to provide a user-friendly interface that is easy to navigate and understand. The UI components are designed to be intuitive and responsive, ensuring a smooth user experience.

2. **Performance**: Efforts are made to optimize the application's performance, both on the frontend and backend. Caching mechanisms and efficient data retrieval techniques are implemented to minimize the response time for fetching repositories, pull requests, and other data from the GitHub API.

3. **Scalability**: The application architecture is designed to be scalable, allowing for the addition of new features or enhancements in the future. The separation of the frontend and backend components enables horizontal scaling by distributing the load across multiple servers if needed.

4. **Security**: The application takes security measures into consideration, especially when interacting with the GitHub API. It ensures secure communication between the frontend and backend using HTTPS. Additionally, proper authentication and authorization mechanisms can be implemented to protect sensitive data and restrict access to authorized users.

5. **Maintainability**: The codebase is structured and organized to promote maintainability. Clear separation of concerns, modularization, and adherence to coding best practices help in understanding and modifying the codebase as needed. Documentation and comments are also provided to aid in future maintenance and development.

6. **Reliability**: The application aims to provide reliable and consistent functionality. Robust error handling and graceful error recovery mechanisms are implemented to handle potential failures, such as network errors or API rate limits. Proper logging and monitoring can also be implemented to identify and address any issues or errors promptly.

Overall, the architecture of the GitHub REST API Handler focuses on usability, performance, scalability, security, maintainability, and reliability to provide a robust and efficient user experience for interacting with the GitHub API.

## Conclusion

The GitHub REST API Handler provides a convenient way to interact with the GitHub API and perform various operations on repositories and pull requests. By following the installation instructions and running the application, users can manage repositories, view pull requests, post comments, merge pull requests, and close pull requests through an intuitive user interface.
