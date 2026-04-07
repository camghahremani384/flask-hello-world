from flask import Flask
import psycopg2 

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Cameron Ghahremani in 3308'

@app.route('/db_test')
def testing(): 
    conn = psycopg2.connect("postgresql://labdb384_user:maLFyL59ww9g1kZSa4HXIPI8fLiMIhvK@dpg-d7ahobmuk2gs73cfvh9g-a/labdb384")
    conn.close()
    return "Database Connection Successful"

