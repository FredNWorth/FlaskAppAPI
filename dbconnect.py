import boto3
import os

dynamodb = boto3.resource('dynamodb', aws_access_key_id='AKIAXCE3IPJUCKTRIKXU',
                          aws_secret_access_key='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',
                          region_name='eu-west-2')

table = dynamodb.Table('unboxed_stock')


def get_stock():
    response = table.get_item(Key={
        'category': {'SS': 'pokemon'}
    })

    return response['Item']


print(get_stock())
