import boto3

dynamodb = boto3.client('dynamodb', aws_access_key_id='',
                        aws_secret_access_key='',
                        region_name='eu-west-2')

table_name = 'unboxed_stock'
category_value = 'pokemon'
query_params = {
    'TableName': table_name,
    'KeyConditionExpression': 'category = :category',
    'ExpressionAttributeValues': {
        ':category': {'S': category_value}
    }
}
response = dynamodb.query(**query_params)

# print the items returned by the query
for item in response['Items']:
    print(item)
