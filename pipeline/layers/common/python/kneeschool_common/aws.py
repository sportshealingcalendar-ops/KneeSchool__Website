"""Shared helpers. Imported by every handler; deliberately dependency free
apart from boto3, which the Lambda runtime provides."""

import json
import os

import boto3

BUCKET = os.environ.get("CONTENT_BUCKET", "kneeschool-content")
TRACKER = os.environ.get("TRACKER_TABLE", "kneeschool-article-tracker")
REVIEW_TOPIC = os.environ.get("REVIEW_TOPIC_ARN", "")
EDITOR_TOPIC = os.environ.get("EDITOR_TOPIC_ARN", "")

_s3 = None
_ddb = None
_sns = None


def s3():
    global _s3
    if _s3 is None:
        _s3 = boto3.client("s3")
    return _s3


def tracker():
    global _ddb
    if _ddb is None:
        _ddb = boto3.resource("dynamodb").Table(TRACKER)
    return _ddb


def sns():
    global _sns
    if _sns is None:
        _sns = boto3.client("sns")
    return _sns


def prefix(page_id):
    return "pipeline/%s/" % page_id


def get_json(key):
    body = s3().get_object(Bucket=BUCKET, Key=key)["Body"].read()
    return json.loads(body.decode("utf-8"))


def get_text(key):
    return s3().get_object(Bucket=BUCKET, Key=key)["Body"].read().decode("utf-8")


def put_json(key, obj):
    s3().put_object(Bucket=BUCKET, Key=key,
                    Body=json.dumps(obj, indent=2).encode("utf-8"),
                    ContentType="application/json")
    return key


def put_text(key, text, content_type="text/markdown; charset=utf-8"):
    s3().put_object(Bucket=BUCKET, Key=key, Body=text.encode("utf-8"),
                    ContentType=content_type)
    return key


def update_tracker(page_id, fields):
    """Merge fields onto the tracker item. The tracker is the single source of
    truth for status, so every stage writes to it."""
    if not fields:
        return
    names, values, sets = {}, {}, []
    for i, (k, v) in enumerate(sorted(fields.items())):
        names["#f%d" % i] = k
        values[":v%d" % i] = v
        sets.append("#f%d = :v%d" % (i, i))
    tracker().update_item(
        Key={"page_id": page_id},
        UpdateExpression="SET " + ", ".join(sets),
        ExpressionAttributeNames=names,
        ExpressionAttributeValues=values,
    )


def publish(topic_arn, subject, message):
    if not topic_arn:
        return None
    return sns().publish(TopicArn=topic_arn, Subject=subject[:100],
                         Message=json.dumps(message, indent=2))
