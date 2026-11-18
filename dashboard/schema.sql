create table if not exists alerts (
  id serial primary key,

  time timestamptz not null,

  rule_id text,
  title text,
  attack text,
  severity text,

  actor text,
  ip text,

  event_id text unique,

  risk_score int default 0,
  ti_score int default 0,

  status text default 'new'
);