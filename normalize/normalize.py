import gzip
import json


def normalize(r):
    ui = r.get('userIdentity', {})
    arn = ui.get('arn') or ''

    return {
        'event_id': r.get('eventID'),
        'time': r.get('eventTime'),
        'account_id': ui.get('accountId') or r.get('recipientAccountId'),
        'region': r.get('awsRegion'),
        'event_source': r.get('eventSource'),
        'event_name': r.get('eventName'),
        'actor_type': ui.get('type'),
        'actor_arn': arn,
        'actor_name': ui.get('userName') or arn.split('/')[-1],
        'source_ip': r.get('sourceIPAddress'),
        'user_agent': r.get('userAgent'),
        'error_code': r.get('errorCode'),
        'read_only': r.get('readOnly'),
        'mfa_used': (r.get('additionalEventData') or {}).get('MFAUsed'),
        'console_login': (r.get('responseElements') or {}).get('ConsoleLogin'),
        'request': json.dumps(r.get('requestParameters')),
    }


def read_file(path):
    return [
        normalize(r)
        for r in json.load(gzip.open(path, 'rt')).get('Records', [])
    ]