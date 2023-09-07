# AOT_SITE README

## Introduction

A dockerised django project with sphinx documentation. The site features login/sign-up, a polls app and a non-functional online store. It comes with a Dockerfile for containerization, a requirements.txt file for managing dependencies, and a docs folder for Sphinx documentation. This README file will guide you through setting up, running, and using the app.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Dockerization](#dockerization)
5. [Documentation](#documentation)
6. [Contributing](#contributing)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- [Python](https://www.python.org/downloads/) (version 3.11.4 or higher)
- [Django](https://www.djangoproject.com/download/) (version 4.2.2 or higher)
- [Docker](https://docs.docker.com/get-docker/) (for containerization)
- [Docker Compose](https://docs.docker.com/compose/install/) (for running with Docker)

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/mmolefe/django-docker-sphinx.git
   ```

2. Navigate to the project directory:

   ```bash
   cd aot_site
   ```

3. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:

   - Windows:

     ```bash
     venv\Scripts\activate
     ```

   - macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

5. Install the project dependencies from `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

6. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

7. Create a superuser (admin) account:

   ```bash
   python manage.py createsuperuser
   ```

8. Start the development server:

   ```bash
   python manage.py runserver
   ```

The Django app should now be running locally. You can access it at [http://localhost:8000](http://localhost:8000) in your web browser.

## Usage

[Provide instructions on how to use your Django app, including any specific workflows, features, or functionalities that users should be aware of.]

## Dockerization

### Locally
If you prefer running the app within a Docker container, follow these steps:

1. Build the Docker image from the project directory:

   ```bash
   docker build --tag aot-app:latest ./
   ```

2. Run the Docker container:

   ```bash
   docker run -p 8000:8000 aot-app
   ```


The Django app will be accessible at [http://localhost:8000](http://localhost:8000) within the Docker container.

### Docker Playground
Once logged into docker playground, create a new instance. Then type the following:

1. Pull Django:
   ```bash
   docker pull django
   ```
   
2. Run the docker container:
   ```bash
   docker run -p 8000:8000 mmolefe/aot-django
   ```

Click on the underlined 8000 next to the "OPEN PORT" button to run. 

NOTE: If the host is disallowed, modify the settings.py file so that ALLOWED_HOSTS = ['*'] instead of []


## Documentation

You can find the documentation for this Django app in the `docs` folder. To build and view the documentation locally, follow these steps:

1. Install Sphinx and other required dependencies:

   ```bash
   pip install -r docs/requirements.txt
   ```

2. Generate the documentation:

   ```bash
   cd docs
   make html
   ```

3. Open the generated documentation in your web browser:

   ```bash
   open _build/html/index.html
   ```

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these guidelines:

- Fork the repository on GitHub.
- Create a new branch from the main branch for your changes.
- Make your changes and commit them with clear and concise messages.
- Create a pull request and describe your changes in detail.
