import random
import os
import psycopg2
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database=os.getenv("database"),
                            user=os.getenv('user'),
                            password=os.getenv('password'))
    return conn


@app.route('/questions')
def questions():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT id FROM questions;')
    result = cur.fetchall()
    cur.close()
    conn.close()
    temp = []
    for res in result:
        temp.append(res[0])
    random.shuffle(temp)
    return jsonify(questions=temp), 200


@app.route('/question/<id>')
def get_question(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM questions WHERE id=%(value)s', {"value": id})
    result = cur.fetchall()
    cur.close()
    conn.close()
    if len(result) > 0:
        return jsonify(question=result[0][1], a=result[0][2], b=result[0][3], c=result[0][4], answer=result[0][5]), 200
    else:
        return {'error': 'not found'}, 404
