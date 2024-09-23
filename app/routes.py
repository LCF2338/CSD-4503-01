from app import flask_app

@flask_app.route('/')
@flask_app.route('/index')
def index():
    return "This is the index page."

@flask_app.route('/dashboard')
def dashboard():
    return "This is the dashboard page."