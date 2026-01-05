import psycopg2
from flask import Flask
app = Flask(__name__)
def get_db_connection():
    conn = psycopg2.connect(host='db',
                            database='postgres',
                            user='postgres',
                            password='Nithish@2699')
    return conn
@app.route('/')
def home():
    conn = get_db_connection()
    return 'Hello, World! Connected to the database successfully.'
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

    