import sys
import os

sys.path.append(os.path.abspath("."))

from normalize.normalize import normalize


def test_normal_event():
    event = {
        "eventID": "123",
        "eventTime": "2026-11-01T10:00:00Z",
        "eventName": "CreateAccessKey",
        "eventSource": "iam.amazonaws.com",
        "awsRegion": "eu-north-1",
        "sourceIPAddress": "1.2.3.4",
        "userIdentity": {
            "accountId": "003720987747",
            "arn": "arn:aws:iam::003720987747:user/sara-admin",
            "userName": "sara-admin",
            "type": "IAMUser"
        }
    }

    result = normalize(event)

    assert result["event_id"] == "123"
    assert result["event_name"] == "CreateAccessKey"
    assert result["actor_name"] == "sara-admin"


def test_missing_arn():
    event = {
        "eventID": "124",
        "eventName": "ListUsers",
        "userIdentity": {
            "accountId": "003720987747"
        }
    }

    result = normalize(event)

    assert result["actor_arn"] == ""
    assert result["actor_name"] == ""


def test_error_event():
    event = {
        "eventID": "125",
        "eventName": "DeleteTrail",
        "errorCode": "AccessDenied",
        "userIdentity": {
            "accountId": "003720987747"
        }
    }

    result = normalize(event)

    assert result["error_code"] == "AccessDenied"