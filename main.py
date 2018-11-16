import pymysql
from app import app
from db_config import mysql
from flask import jsonify, request

@app.route('/create', methods=['POST'])
def create_query():
    try:
        _json = request.json
        _order_id = _json['order_id']
        _product_id = _json['product_id']
        _user_id = _json['user_id']
        _rating = _json['rating']
        _review = _json['review']
        if request.method == 'POST':
            sql = 'INSERT INTO user_review (order_id, product_id, user_id, rating, review) VALUES (%s, %s, %s, %s, %s)'
            data = (_order_id, _product_id, _user_id, _rating, _review)
            connection = mysql.connect()
            cursor = connection.cursor()
            cursor.execute(sql, data)
            connection.commit()
            resp = jsonify('Query added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
            print(e)

    finally:
        cursor.close()
        connection.close()


@app.route('/read')
def read_query():
    try:
        connection = mysql.connect()
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        sql = 'SELECT * FROM user_review'
        cursor.execute(sql)
        result = cursor.fetchall()
        resp = jsonify(result)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        connection.close()

@app.route('/update', methods=['POST'])
def update_query():
    try:
        _json = request.json
        _id = _json['id']
        _order_id = _json['order_id']
        _product_id = _json['product_id']
        _user_id = _json['user_id']
        _rating = _json['rating']
        _review = _json['review']
        if request.method == 'POST':
            sql = 'UPDATE user_review SET order_id=%s, product_id=%s, user_id=%s, rating=%s, review=%s WHERE id=%s'
            data = (_order_id, _product_id, _user_id, _rating, _review, _id)
            connection = mysql.connect()
            cursor = connection.cursor()
            cursor.execute(sql, data)
            connection.commit()
            resp = jsonify('Query updated successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found()

    except Exception as e:
        print(e)
    finally:
        cursor.close()
        connection.close()


@app.route('/delete/<id>')
def delete_query(id):
    try:
        connection = mysql.connect()
        cursor = connection.cursor()
        sql = 'DELETE FROM user_review WHERE id=%s'
        cursor.execute(sql, (id,))
        connection.commit()
        resp = jsonify('Query deleted successfully!')
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        connection.close()


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }

    resp = jsonify(message)
    resp.status_code = 404

    return resp

if __name__ == "__main__":
    app.run()