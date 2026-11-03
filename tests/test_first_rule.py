import json
import sys
import os

sys.path.append(os.path.abspath("."))

from detections.first_rule import detect_logging_disabled


def test_malicious_sample():
    with open('tests/sample_logs/malicious.json', 'r') as f:
        records = json.load(f)

    alerts = detect_logging_disabled(records)

    assert len(alerts) == 1


def test_benign_sample():
    with open('tests/sample_logs/benign.json', 'r') as f:
        records = json.load(f)

    alerts = detect_logging_disabled(records)

    assert len(alerts) == 0