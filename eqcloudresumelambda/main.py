import boto3

# declaring the table name variable
table_name = "eq-visitorcounter"


# creating the DynamoDB table resource
def get_table():
    dynamodb = boto3.resource('dynamodb', region_name="eu-west-1")
    return dynamodb.Table(table_name)


def handler(event, context):
    table = get_table()
    response = table.update_item(
        Key={
            "visitor-info": "total-visitors",
        },
        UpdateExpression="ADD #vc :val",
        ExpressionAttributeNames={
            "#vc": "view-counter"
        },
        ExpressionAttributeValues={
            ":val": 1
        },
        ReturnValues="UPDATED_NEW"
    )

    total_visitors = int(response["Attributes"]["view-counter"])

    return {
        "isBase64Encoded": False,
        "statusCode": 200,
        "headers": {"Access-Control-Allow-Origin": "*"},
        "body": total_visitors
    }
