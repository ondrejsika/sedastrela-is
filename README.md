# sedastrela-is

Informacni system Sede Strely

- author: __Ondrej Sika__ <ondrej@ondrejsika.com>
- license: __MIT__ <https://ondrejsika.com/license/mit.txt>

## Installation for development

```
git clone git@github.com:ondrejsika/sedastrela-is.git
cd sedastrela-is
virtualenv .env
. .env/bin/activate
pip install -U pip
pip install -r requirements.txt
cp conf/secrets--template conf/secrets
# Update secets
# vim conf/secrets
```

Create first user

```
. conf/dev && . conf/secrets && ./manage.py createsuperuser
```

## Run

### Development mode

```
. .env/bin/activate
. conf/dev && . conf/secrets && ./manage.py runserver
```

### Production

Run in [DWH](https://github.com/ondrejsika/dwh) or by hand:

```
. conf/prod && EXTERNAL_PORT=8001 docker-compose up
```
