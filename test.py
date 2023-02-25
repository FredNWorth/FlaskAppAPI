from flask import Flask, request, jsonify

records = []

app = Flask(__name__)

# Create a new record
@app.route('/records', methods=['POST'])
def create_record():
        data = request.get_json()
        data['id'] = len(records) + 1 # Assign a unique ID to the record
        records.append(data)
        return jsonify(data)


# Get record by ID
@app.route('/records/<int:record_id>', methods=['GET'])
def get_record(record_id):
        for record in records:
                if record['id'] == record_id:
                        return jsonify(record)
        return 'Record not found', 404


# Get all records by a query
@app.route('/records', methods=['GET'])
def get_records():
        query = request.args.get('query')
        if query:
                filtered_records = [record for record in records if query in record.values()]
                return jsonify(filtered_records)
        return jsonify(records)

# Delete a record by name
@app.route('/records', methods=['DELETE'])
def delete_record():
        name = request.args.get('name')
        if name:
                for record in records:
                        if record['name'] == name:
                                records.remove(record)
                                return 'Record deleted', 200
                return 'Record not found', 404
        return 'Missing name parameter', 400

@app.route('/records/<int:id>', methods=['PUT'])
def update_record(id):
    record = next((record for record in records if record['id'] == id), None)
    if record is None:
        return jsonify({'error': 'Record not found'}), 404

    data = request.get_json()
    record.update(data)
    return jsonify(record)


if __name__=='__main__':
        app.run(debug=True, host='0.0.0.0', port=5000)
