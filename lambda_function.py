import json

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('github actions workflow - update code, publish version, update alias!')
    }
