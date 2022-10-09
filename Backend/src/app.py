from flask import Flask
from flask_cors import CORS
from web_scraping.web_request import ArticleReader
from db_script import DB

# Contains all the initilization and config necessary for the app
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'codnity_articles'

CORS(app)

ar = ArticleReader(DB(app))
