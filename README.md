# Flask-Based Exam Result Checker

## Description
This is my first project using Flask, created for practice purposes. The website allows users to input marks for four subjects (Science, Maths, English and Hindi) and calculates the overall percentage to determine if the student has passed the exam.

## Running the Project Locally

To run this Flask-based Exam Result Checker locally, follow these steps:

### Prerequisites

- **Python 3.x** installed on your system.
- **pip** (Python package installer) installed.
- **Virtualenv** installed (optional but recommended).

### Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/anubagre/Flask-Based-Exam-Result-Checker.git
   cd Flask-Based-Exam-Result-Checker

2. **Create a Virtual Environment:** It’s a good practice to use a virtual environment to manage dependencies.
    ```bash
    python -m venv venv

3. **Activate the Virtual Environment:**  
   On Windows:
   ```bash
   venv\Scripts\activate

4. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt

5. **Running the Application:** Set the FLASK_APP Environment Variable

    On Windows:
    ```bash
    set FLASK_APP=app.py

6. **Run the Flask Development Server:**

    ```bash
    flask run

Access the Application: Open your web browser and go to http://127.0.0.1:5000.
