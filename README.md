# Horne Converter

## Background
https://horne-converter.fly.dev/
The Horne Converter allows users to  convert a value from a standard unit of 
measurement to a silly unit of measurement. This converter was inspired by 
Alex Horne from the Taskmaster UK TV show. 

## Instructions

### Install packages
Assumes that node.js and npm are installed


- Install front end tooling 
  - Tailwind
    ~~~~ 
    npm install -D tailwindcss
    ~~~~

- Set up backend
1. install pip
     ~~~~
     python.exe -m pip install --upgrade pip –user
     ~~~~
2. install venv
     ~~~
     pip install virtualenv –user
     ~~~
3. Create new virtual environment
     ~~~~
     python -m virtualenv venv
     ~~~~
4. Activate virtual environment
     ~~~~
     .\venv\Scripts\activate
     ~~~~
5. Install Django
     ~~~~
     pip install Django
     ~~~~
6. Install Humanize (https://pypi.org/project/humanize/)
     ~~~~
     python -m pip install --upgrade humanize
     ~~~~
7. Install environs package
    ~~~~
   python -m pip install django-environ==0.9.0
   ~~~~
8. Install psycopg package
    ~~~~
    python -m pip install psycopg2==2.9.5
    ~~~~
9. Install WhiteNoise package
    ~~~~
    python -m pip install whitenoise==6.3.0
    ~~~~

[//]: # (## TODO)

[//]: # (- Add instructions for setup / running including copy/pasteable commands)

[//]: # (- Remove .idea directory &#40;google how to remove items from .git&#41;)

[//]: # (- Remove the extra .sqlite3 file)

[//]: # (- remove .venv from the app &#40;in .git&#41;)

[//]: # (- google other common .gitignore rules for django / python projects)

[//]: # (- Reset migrations to get rid of ones for models that were for another project.)