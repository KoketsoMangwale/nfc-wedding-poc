import os
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])
CLOUDFRONT_URL = f"https://{os.environ['CLOUDFRONT_URL']}"

def lambda_handler(event, context):
    guest_id = event['queryStringParameters'].get('guest_id')
    if not guest_id:
        return {'statusCode': 400, 'body': 'guest_id missing'}

    resp = table.get_item(Key={'GuestID': guest_id})
    guest = resp.get('Item')
    if not guest:
        return {'statusCode': 404, 'body': 'Guest not found'}

    # Redirect to personalized content hosted on CloudFront/S3
    # Example assumes 'thank_you.mp4' is in CloudFront bucket
    redirect_url = f"{CLOUDFRONT_URL}/{guest['ContentLinks']['thank_you']}"

    # Log tap count
    table.update_item(
        Key={'GuestID': guest_id},
        UpdateExpression="SET TapCount = if_not_exists(TapCount, :start) + :inc",
        ExpressionAttributeValues={':inc': 1, ':start': 0}
    )

    return {
        'statusCode': 302,
        'headers': {'Location': redirect_url}
    }
