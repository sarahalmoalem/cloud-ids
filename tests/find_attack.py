import gzip
import json
import glob

for f in glob.glob('data/raw/**/*.json.gz', recursive=True):
    for r in json.load(gzip.open(f, 'rt'))['Records']:
        if r['eventName'] in ('StopLogging', 'DeleteTrail'):
            print(
                f,
                r['eventTime'],
                r['userIdentity']['arn'],
                r['sourceIPAddress']
            )