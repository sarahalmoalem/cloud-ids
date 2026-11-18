import boto3
import json
import os

BUCKET = os.environ["TRAIL_BUCKET"]
PREFIX = os.environ["TRAIL_PREFIX"]

STATE = "data/state.json"
RAW = "data/raw"


def collect():
    os.makedirs(RAW, exist_ok=True)

    if os.path.exists(STATE):
        with open(STATE, "r") as f:
            done = set(json.load(f))
    else:
        done = set()

    s3 = boto3.client("s3")
    new = []

    paginator = s3.get_paginator("list_objects_v2")

    for page in paginator.paginate(
        Bucket=BUCKET,
        Prefix=PREFIX
    ):
        for obj in page.get("Contents", []):
            key = obj["Key"]

            if key.endswith(".json.gz") and key not in done:
                path = os.path.join(
                    RAW,
                    key.replace("/", "_")
                )

                print(f"Downloading: {key}")

                s3.download_file(
                    BUCKET,
                    key,
                    path
                )

                done.add(key)
                new.append(path)

    with open(STATE, "w") as f:
        json.dump(sorted(done), f)

    return new