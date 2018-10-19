import os

from app import create_app

app = create_app(os.getenv('APP_SETTINGS'))

@app.route('/')
def welcome():
    return "<h1>Welcome to Store Manager Application</h>"


if __name__ == "__main__":
    app.run()
