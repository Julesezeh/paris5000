from flask import Flask
from extensions import api,db

def create_app():
    app = Flask(__name__)
    
    api.init_app(app)
    db.init_app(db)
    


    return app