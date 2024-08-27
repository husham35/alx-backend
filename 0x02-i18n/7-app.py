#!/usr/bin/env python3
"""
Infer appropriate time zone
"""
from flask import Flask
from flask_babel import Babel
from flask import render_template, request, g
from typing import Union, Dict
import pytz


class Config:
    """
    Create a Config class that has a LANGUAGES class attribute
    equal to ["en", "fr"].
    """
    LANGUAGES = ["en", "fr" ]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user () -> Union[Dict, None]:
    """
    Retrieves a user based on current user id.
    """
    login_id = request.args.get('login_as', '')
    if login_id:
        return users.get(int(login_id), None)
    return None


@app.before_request
def before_request() -> None:
    """
    Gets user details before each request's resolution.
    """
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale() -> str:
    """
    Retrieves the locale for the web page.
    """
    queries = request.query_string.decode('utf-8').split('&')
    query_table = dict(map(
        lambda x: (x if '=' in x else '{}='.format(x)).split('='),
        queries,
    ))
    locale = request.args.get('locale', '')
    if locale in app.config["LANGUAGES"]:
        return locale
    if g.user and g.user['locale'] in app.config["LANGUAGES"]:
        return g.user['locale']
    header_locale = request.headers.get('locale', '')
    if header_locale in app.config["LANGUAGES"]:
        return header_locale
    return app.config['BABEL_DEFAULT_LOCALE']


@babel.timezoneselector
def get_timezone() -> str:
    """
    Gets user timezone.
    """
    timezone = request.args.get('timezone', '').strip()
    if not timezone and g.user:
        timezone = g.user['timezone']
    try:
        return pytz.timezone(timezone).zone
    except pytz.exceptions.UnknownTimeZoneError:
        return app.config['BABEL_DEFAULT_LOCALE']


@app.route('/')
def get_index() -> str:
    """
    The home page/index page.
    """
    return render_template('7-index.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)