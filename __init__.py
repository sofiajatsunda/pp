from flask import Flask
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine
from flask_bcrypt import Bcrypt
from flask_httpauth import HTTPBasicAuth
from flask_restful import Api

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pp.db'
api=Api(app)
bcrypt = Bcrypt(app)
auth = HTTPBasicAuth()
engine = create_engine('sqlite:///pp.db', echo=True)
Session = sessionmaker(bind=engine)
Session = scoped_session(Session)



