import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# SQLALCHEMY_DATABASE_URI = 'postgres://postgres@localhost:5432/some'
# SQLALCHEMY_DATABASE_URI = 'postgres://USER:PASSWORD@HOST:5432/DB'
SQLALCHEMY_DATABASE_URI ='postgres://vblcedtgwezjrc:6fa5c70107ed0e16a21e603e53d1e3afb282c6f6c21f63b1f30fba91522dff7d@ec2-54-83-33-14.compute-1.amazonaws.com:5432/d5s8qdsgv37ekq'

