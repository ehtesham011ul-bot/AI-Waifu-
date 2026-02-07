# Configuration settings for Flask application

import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_default_secret_key'
    DEBUG = os.environ.get('DEBUG') or False
    HOST = os.environ.get('HOST') or 'localhost'
    PORT = os.environ.get('PORT') or 5000

    @staticmethod
    def init_app(app):
        pass
