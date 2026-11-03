import gzip
import json
import glob

f = glob.glob('data/raw/**/*.json.gz', recursive=True)[0]

records = json.load(gzip.open(f, 'rt'))['Records']

for r in records[:5]:
    print(
        r['eventTime'],
        r['eventName'],
        r['userIdentity'].get('arn'),
        r['sourceIPAddress']
    )