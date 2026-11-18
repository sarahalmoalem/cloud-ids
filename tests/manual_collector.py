import sys
import os

sys.path.append(os.path.abspath("."))

from ingest.collector import collect

files = collect()

print(f"Downloaded: {len(files)} files")

for f in files:
    print(f)