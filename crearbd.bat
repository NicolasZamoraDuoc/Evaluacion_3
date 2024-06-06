call C:\Users\CETECOM\Documents\GitHub\Evaluacion_3\.venv\Scripts\activate.bat
call python manage.py runscript -v3 eliminar_tablas
call C:\Users\CETECOM\Documents\GitHub\Evaluacion_3\core\migrations
call python manage.py makemigrations
call python manage.py makemigrations core
call python manage.py migrate
call python manage.py migrate core
