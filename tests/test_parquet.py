import sys
import os

sys.path.append(os.path.abspath("."))

from normalize.parquet_store import save_parquet, query_events


rows = [
    {
        "event_id": "1",
        "time": "2026-11-03T10:00:00Z",
        "event_name": "CreateBucket"
    },
    {
        "event_id": "2",
        "time": "2026-11-03T10:01:00Z",
        "event_name": "CreateBucket"
    },
    {
        "event_id": "3",
        "time": "2026-11-03T10:02:00Z",
        "event_name": "DeleteBucket"
    }
]

save_parquet(rows)

print(query_events())
