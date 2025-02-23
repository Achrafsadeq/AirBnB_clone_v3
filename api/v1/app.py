#!/usr/bin/python3
'''Defines a RESTful API using Flask for managing resources.
'''
import os
from flask import Flask, jsonify
from flask_cors import CORS
from models import storage
from api.v1.views import app_views


app = Flask(__name__)
'''The main Flask application instance for the API.'''

app_host = os.getenv('HBNB_API_HOST', '0.0.0.0')
app_port = int(os.getenv('HBNB_API_PORT', '5000'))

app.url_map.strict_slashes = False

app.register_blueprint(app_views)

CORS(app, resources={'/*': {'origins': app_host}})


@app.teardown_appcontext
def cleanup_resources(exception):
    '''Cleans up resources and closes
        the storage connection after each request.'''
    # Uncomment for debugging: print(exception)
    storage.close()


@app.errorhandler(404)
def handle_not_found(error):
    '''Returns a JSON response for 404 errors (Resource Not Found).'''
    return jsonify(error='Resource not found'), 404


@app.errorhandler(400)
def handle_bad_request(error):
    '''Returns a JSON response for 400 errors (Bad Request).'''
    message = 'Invalid request'
    if isinstance(error, Exception) and hasattr(error, 'description'):
        message = error.description
    return jsonify(error=message), 400


# Entry point for running the Flask application
if __name__ == '__main__':
    # Re-fetch host and port for runtime configuration
    app_host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    app_port = int(os.getenv('HBNB_API_PORT', '5000'))

    # Start the Flask app with threading enabled
    app.run(
        host=app_host,
        port=app_port,
        threaded=True
    )
