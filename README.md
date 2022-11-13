# Coupon Manager

## Project Architecture
* apps: Contains created apps such as **accounts** and **coupon**
  * accounts: Handles user management and authentication
  * coupons: Manages coupons and usage of them
  * shared: Contains shared models and services
* config: Configuration (setting) files for different environments
  * base: Basic config file to import and modify
  * local: For local developments
  * production: For production environments
* coupon_manager: main app

## Available APIs
* /auth
  * /login/: In order to login (get access and refresh tokens)
  * /accounts/[pk]/: Get list of accounts or detailed view for one
  * /profile/: Get your profile
* /coupons
  * /: Get list of available coupons
  * /use/: Use a coupon

## Dependencies
* PostgresSQL

## Local Development & run

Create a virtual environment
```shell
python -m venv coupon_manager
```
Then install requirements
```shell
pip install -r requirements.txt
```
Then create a file name _.env_ and enter required variables. Find a sample in _example.env_.
Fire up a **Postgres** db then
```shell
python ./manage.py runserver
```