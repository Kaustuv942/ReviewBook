# ReviewBook

![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)<br>

A social media app for movies, games and tv series reviews

> The app allows you to review movies, games and tv shows. It allows you to follow users and your feed shows the latest reviews by users.It has a login feature.

##  Starting the Project


1. Create a **virtual environment** with venv (install virtualenv, if its not installed).

    ```
    venv reviewbook

    ```

2. Clone the project in the virtual environment directory.

    ```
    cd freemex
    git clone https://github.com/lugnitdgp/ReviewBook.git

    ```

3. Activate the virtual environemnt.

    #### For Linux/Mac OSX   
    ```
    source bin/activate

    ```

    #### For Windows
    ```
    .\Scripts\activate

    ```

4. Install the requirements.

    ```
    cd reviewbook
    pip install -r requirements.txt

    ```


5. Run the Migrations
    ```
    python manage.py makemigrations

    python manage.py migrate

    ```
6. Run the development server
    ```
    python manage.py runserver

    ```
7. Head to server http://localhost:8000
#avik was here

8. Add Few Movies, Games and Tv shows in their respective models to display them. Enjoy!

## For contributors

ReviewBook uses the following technologies:

+ HTML/CSS/JavaScript
+ Pyhton(Django)

If you want to contribute to this project, then have a look [here](https://github.com/lugnitdgp/ReviewBook/blob/master/CONTRIBUTING.md)
