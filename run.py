from flask import Flask, render_template
from app.routes import create_routes
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Configuring static and template folders
app.static_folder = 'app/static'
app.template_folder = 'app/templates'

# Initializing routes
create_routes(app)

if __name__ == '__main__':
    app.run(port=3000)