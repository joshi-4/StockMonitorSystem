# StockMonitor    ![Status active](https://img.shields.io/badge/Status-active%20development-2eb3c1.svg) ![Django 2.1.5](https://img.shields.io/badge/Django-2.1.5-green.svg) ![Python 3.6](https://img.shields.io/badge/Python-3.6-blue.svg)

## A Webapp to monitor the prices of Stocks.

### Installation :
Requirements :
- Python 3.6 [runtime]
- Django 2.1
- Other requirements in Requirements.txt

### Procedure :
- Create a new Virtual environment and activate it.
    ```
    sudo apt-get install -y python3-venv
    python3 -m venv stockenv
    source stockenv/bin/activate
    ```
- Use PIP to install all other dependencies.
    ```
    pip install -r requirements.txt
    ```
- Create a Super User.
    ```
    python3 manage.py createsuperuser
    ```
- Run Development Server on localhost.
    ```
    python3 manage.py runserver
    ```

## Enjoy Monitoring Stocks.
