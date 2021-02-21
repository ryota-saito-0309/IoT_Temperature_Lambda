import json
import boto3

def lambda_handler(event, context):
    # 参考にしたコードのURL
    # https://qiita.com/is_ryo/items/74f3fc70b7602888a2ac
    try:
        dynamoDB = boto3.resource("dynamodb")
        table = dynamoDB.Table("table-name") # DynamoDBのテーブル名

        # DynamoDBへのPut処理実行
        table.put_item(
            Item = {
                "PartitionKey": "your-partition-key-data", # Partition Keyのデータ
                "SortKey": "your-sort-key-data", # Sort Keyのデータ
                "OtherKey": "your-other-data"  # その他のデータ
            }
        )
    except Exception as e:
        print e

    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": "hello world",
            }
        ),
    }
