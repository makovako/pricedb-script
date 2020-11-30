#!/usr/bin/env python3

import os
import boto3
import json
from dotenv import find_dotenv, load_dotenv

def main(login, password):
    session = boto3.Session(
        aws_access_key_id=login,
        aws_secret_access_key=password,
        region_name="eu-central-1"
    )
    dynamodb = session.resource('dynamodb')
    table = dynamodb.Table('pricedb-item')
    done = False
    start_key = None
    scan_kwargs = {}
    items = []
    while not done:
        if start_key:
            scan_kwargs['ExclusiveStartKey'] = start_key
        response = table.scan(**scan_kwargs)
        items.extend(response.get('Items',[]))
        start_key = response.get('LastEvaluatedKey',None)
        done = start_key is None
    print(json.dumps(items, indent=2))


if __name__ == "__main__":
    load_dotenv(find_dotenv())
    main(os.environ.get("DB_ACCESS_KEY_ID"), os.environ.get("DB_SECRET_ACCESS_KEY"))