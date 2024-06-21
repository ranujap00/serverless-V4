import json

def hello(event, context):
    # Extract the name from path parameters
    name = event['pathParameters']['name'] if 'pathParameters' in event and 'name' in event['pathParameters'] else 'World'
    
    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token",
            "Access-Control-Allow-Methods": "OPTIONS,GET"
        },
        "body": json.dumps({
            "message": f"Hello, {name}! Go Serverless v4! Your function executed successfully!"
        })
    }
