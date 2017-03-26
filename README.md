# sedastrela-is

Informacni system Sede Strely

- author: __Ondrej Sika__ <ondrej@ondrejsika.com>
- license: __MIT__ <https://ondrejsika.com/license/mit.txt>

## Installation

```
git clone git@github.com:ondrejsika/sedastrela-is.git
cd sedastrela-is
virtualenv .env
. .env/bin/activate
pip install -U pip
pip install -r requirements.txt
cp settings_local--template.py settings_local.py
# Update local config
# vim settings_local.py
```

Create first user

```
./manage.py createsuperuser
```

## Run

### Development mode

```
. .env/bin/activate
./manage.py runserver
```