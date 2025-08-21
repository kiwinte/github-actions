import json

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda - github actions workflow with update-function for two functions. Add versioning to workflow!')
    }
