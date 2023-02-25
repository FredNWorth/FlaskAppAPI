# API = Application Programming Interface
# Allows two applications to communicate
# Doesn't need to know how either application works
# Returns data as JSON
# Web based APIs most common

from flask import Flask
from flask import request
import json

with open('customer_db.json', 'r') as db:
    customer_records = json.load(db)

app = Flask(__name__)


def add_customer():
    max_id = 0
    for c in customer_records:
        if int(c['id']) > max_id:
            max_id = int(c['id'])

    customer_name = request.args.get('name')
    customer_age = request.args.get('age')
    customer_records.append({'id': str(max_id + 1), 'name': customer_name, 'age': customer_age})
    with open('customer_db.json', 'w') as json_file:
        json.dump(customer_records, json_file)

    return customer_records


def view_customer():

    if request.args.get('id'):
        customer = [c for c in customer_records if c['id'] == request.args.get('id')]
        try:
            return customer_records[customer_records.index(customer[0])]
        except IndexError:
            return "No such customer"
    return customer_records


def update_customer():
    new_name = request.args.get('name')
    new_age = request.args.get('age')
    try:
        customer = [c for c in customer_records if c['id'] == request.args.get('id')]
        if new_name:
            customer_records[customer_records.index(customer[0])].update(name=new_name)
        if new_age:
            customer_records[customer_records.index(customer[0])].update(age=new_age)
        if not new_name and not new_age:
            return "No updates made"

        with open('customer_db.json', 'w') as json_file:
            json.dump(customer_records, json_file)
        return f'customer id {request.args.get("id")} updated'
    except IndexError:
        return "No such customer"


def delete_customer():
    try:
        customer = [c for c in customer_records if c['id'] == request.args.get('id')]
        customer_records.remove(customer_records[customer_records.index(customer[0])])
        with open('customer_db.json', 'w') as json_file:
            json.dump(customer_records, json_file)
        return f'{request.args.get("id")} deleted'
    except IndexError:
        try:
            customer = [c for c in customer_records if c['name'] == request.args.get('name')]
            customer_records.remove(customer_records[customer_records.index(customer[0])])
            with open('customer_db.json', 'w') as json_file:
                json.dump(customer_records, json_file)
            return f'{request.args.get("name")} deleted'
        except IndexError:
            return "No such customer"


@app.route('/', methods=["GET", "PUT", "DELETE", "UPDATE"])
def call_api():
    if request.method == 'PUT':
        if request.args.get("action") == "update":
            return update_customer()
        else:
            return add_customer()
    elif request.method == 'DELETE':
        return delete_customer()
    elif request.method == 'GET':
        return view_customer()
    else:
        return "No Query"


@app.route('/easter')
def easter_egg():
    return "This is an easter egg"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
