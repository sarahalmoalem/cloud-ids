def detect_logging_disabled(records):
    alerts = []

    for r in records:
        if r.get('eventName') in ('StopLogging', 'DeleteTrail'):
            alerts.append({
                'rule': 'CloudTrail logging disabled',
                'attack': 'T1562.008',
                'severity': 'high',
                'actor': r['userIdentity'].get('arn'),
                'ip': r.get('sourceIPAddress'),
                'time': r['eventTime'],
            })

    return alerts