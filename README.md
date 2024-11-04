## Setup

#### - Create Virtual Environment
###### # Mac
```
python3 -m venv venv
source venv/bin/activate
```

###### # Windows
```
python3 -m venv venv
.\venv\Scripts\activate.bat
```

<br>

#### - Install dependencies
```
pip install --upgrade pip
pip install -r requirements.txt
```

<br>

#### - Migrate to database
```
python manage.py migrate
python manage.py createsuperuser
```

<br>

#### - Run application
```
python manage.py runserver
```

<br>

#### - Generate Secret Key ( ! Important for deployment ! )
```
python manage.py shell
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
exit()
```

### Launch redis
```bash
redis-server
```
```bash
brew services start redis
```
```bash
brew services info redis
```
```bash
brew services stop redis
```
```bash
redis-cli
```
### Celery
--- Windows
```bash
celery -A a_core worker -P solo
celery -A a_core worker -P threads
celery -A a_core worker -P gevent
```
### Celery
--- MacOS
```bash
celery -A a_core worker
```
### Launch celery
```bash
celery -A a_core worker -E -l info
```
### Launch flower
```bash
celery -A a_core.celery_app flower
```
```bash
celery -A a_core.celery_app flower --basic_auth=jortega:admin
```
### Enviar boletín
```bash
celery -A a_core beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
```
