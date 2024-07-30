import json

def lambda_handler(event, context):
    method = event['httpMethod']
    
    if method == 'GET':
        return {
            'statusCode': 200,
            'body': json.dumps('GET method called')
        }
    elif method == 'POST':
        return {
            'statusCode': 200,
            'body': json.dumps('POST method called')
        }
    else:
        return {
            'statusCode': 400,
            'body': json.dumps(f'Unsupported method: {method}')
        }
