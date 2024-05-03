# Django Food Recipe Project

This is a Django-based web application for managing and sharing food recipes. Users can create, view, edit, and delete recipes, as well as interact with other users through comments and ratings.

## Features

- **User Authentication**: Users can sign up, log in, and log out securely.
- **Recipe CRUD Operations**: Users can create, read, update, and delete their own recipes.
- **Search and Filter**: Users can search for recipes by name, ingredient, or category. They can also filter recipes based on various criteria.

## Technologies Used

- **Django**: Python-based web framework for building the backend.
- **HTML/CSS**: For the frontend templates and styling.
- **Bootstrap**: Frontend framework for responsive design.
- **SQLite**: Database management system for storing recipe data.

## Setup Instructions

1. Clone the repository:

git clone https://github.com/Vansh2693/Food_Recipe-App.git

2. Navigate to the project directory:

cd core

3. Install dependencies:

pip install -r requirements.txt

4. Create a virtual environment (optional but recommended):

5. Activate the virtual environment:

->cd Scripts
->Activate

6. Apply migrations:

python manage.py migrate

7. Run the development server:

python manage.py runserver
