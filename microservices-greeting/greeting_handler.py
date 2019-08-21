"""This function returns the greetings phrase."""
BASE_PATH = '/resources/'

def name_handler(event, context):
    """Return the greeting"""
    if event['path'].startswith(BASE_PATH):
        processed_path = event['path'][len(BASE_PATH):]
        if processed_path in ('greeting', 'greeting/'):
            return {
                "statusCode": 200,
                "body": 'Hello'
            }
    print(event)
    print(context)
    return {
        "statusCode": 500,
        "body": 'Provided URL path is invalid.'
        }
