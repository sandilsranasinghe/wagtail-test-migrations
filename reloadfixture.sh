rm -f "db.sqlite3"
python manage.py migrate
python manage.py migrate --fake blog 0006
python manage.py migrate 
python manage.py migrate blog 0005
python manage.py loaddata fixtures/fixture-v4-2