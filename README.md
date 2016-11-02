# Purchaes

 - [info](docs/info.md)
 - [references](docs/references.md)
 
## contributor

 - [@benwrk](https://github.com/benwrk)
 - [@wit543](https://github.com/wit543)
 - [@pranger54](https://github.com/pranger54)
 - [@chinatip](https://github.com/chinatip)
 - [@moopiing](https://github.com/moopiing)

## Don't forget
 - One person makemigration
 - other only migrate
 
## Get start
 install requirment:
```
 pip install -r requirements.txt
```
 change DATABASE in the setting:
  [backend/Purchaes/setting](https://github.com/benwrk/Purchaes/blob/development/backend/Purchaes/settings.py)
 ```
 DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'wsplab',
        'USER': 'wsp',
        'PASSWORD':'123456789',
        'HOST':'localhost',
        'PORT':'',
    }
}
```
 to
 ```
  DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.sqlite3',
         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
     }
 }
 ```
 migrate
 ```
 python manage.py migrate
 ```
