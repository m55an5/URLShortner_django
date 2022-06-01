python -m venv drf_env
source drf_env/bin/activate
python -m pip install -r requirements.txt

/Users/manjotssandhu/work/URLShortner
python -m pip install --upgrade pip      
python -m pip install -r requirements.txt

python -m pytest urlshortner/ --cache-clear -v
python manage.py runserver