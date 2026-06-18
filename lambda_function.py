import json
import pymysql

def lambda_handler(event, context):

    connection = pymysql.connect(
        host="mydb.cqncy2ku2xgs.us-east-1.rds.amazonaws.com",
        user="shashi",
        password="shashi12345",
        database="project9",
        cursorclass=pymysql.cursors.DictCursor
    )

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM students")

    rows = cursor.fetchall()

    #  convert datetime to string
    for row in rows:
        if "created_At" in row and row["created_At"] is not None:
            row["created_At"] = str(row["created_At"])

    connection.close()

    return {
        "statusCode": 200,
        "body": json.dumps({
            "students": rows
        })
    }
