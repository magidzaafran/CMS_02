"""
This script runs the FlaskWebProject application using a development server.
"""
import os
from os import environ
from FlaskWebProject import app
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5000'))
    except ValueError:
        PORT = 5000

    app.run(host=HOST, port=PORT, debug=True)
