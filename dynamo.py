import boto3
import key_config as key
# boto3 is the AWS SDK library for Python.
# We can use the low-level client to make API calls to DynamoDB.


client = boto3.client('dynamodb', region_name='ca-central-1')
# table = client.table('Students')
db = boto3.resource('dynamodb', aws_access_key_id = key.ACCESS_KEY_ID,
                    aws_secret_access_key = key.ACCESS_SECRET_KEY)
table = db.Table('Students')


# def InsertBook(title, author):
#     prep_statement = "INSERT INTO 'BOOKS' value {'Author':{0},'Title':{1}}".format(author,title)
#     resp = client.execute_statement(Statement = prep_statement)
#     return resp['Items']


def GetAll():
    resp = table.scan()
    return resp['Items']


def SelectBook(name):
    if name:
        resp = table.get_item(
            Key={
                "FirstName": name
            }
        )
        return resp['Item']
    return None


# def UpdateBook(id,title,author):
#     prep_statement = "UPDATE Books SET Title = {0} AND Author = {1} WHERE Id = {2}".format(title,author,id)
#     resp = client.execute_statement(Statement = prep_statement)
#     return resp['Items']
#
#
# def RemoveBook(id):
#     prep_statement = "UPDATE Books REMOVE * WHERE Id = {0}".format(id)
#     resp = client.execute_statement(Statement = prep_statement)
#     return resp['Items']
#
