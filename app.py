from flask import Flask, jsonify
import boto3

app = Flask(__name__)

# Replace with your IAM user's access keys
aws_access_key_id = 'AKIAS2RBT7PDHMNDZPUA'
aws_secret_access_key = 'X2mAMmNkWTRihDpeFTt46HgKcB71QeJMEv7tmX7+'
region_name = 'us-east-1'  # Replace with your region
table_name = 'ThreadTensionData'  # Replace with your table name

# Initialize DynamoDB connection
dynamodb = boto3.resource(
    'dynamodb',
    region_name=region_name,
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)

table = dynamodb.Table(table_name)

@app.route('/', methods=['GET'])
def get_tension_data():
    
    try:
        response = table.scan()
        items = response.get('Items', [])
        return jsonify(items)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5002)
