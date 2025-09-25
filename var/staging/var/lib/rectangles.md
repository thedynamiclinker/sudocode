TODO:
- The "rectangle people" dialogue.
- Tl;dr: "This is a fucking abomination."

## /var/lib/mysql

```
├── ibdata1                # InnoDB system tablespace (metadata, older versions also user data)
├── ib_logfile0            # InnoDB redo log
├── ib_logfile1
├── ibtmp1                 # InnoDB temp tablespace
├── mysql/                 # system database (users, privileges, etc.)
│   ├── user.frm
│   ├── user.MYD
│   ├── user.MYI
│   └── ...
├── performance_schema/    # memory engine, but has metadata
├── testdb/                # your own database "testdb"
│   ├── table1.frm         # table definition (pre-8.0; gone in 8.0+)
│   ├── table1.ibd         # InnoDB table tablespace (if file-per-table enabled)
│   ├── table2.MYD         # MyISAM table data
│   ├── table2.MYI         # MyISAM table index
│   └── db.opt             # db charset/collation options
└── auto.cnf               # server UUID
```

## /var/lib/postgresql

```
/var/lib/postgresql/15/main/
├── base/                     # per-database directories
│   ├── 1/                     # template1 database (OID = 1)
│   │   ├── 1247               # pg_class table heap
│   │   ├── 1247_fsm           # free space map
│   │   ├── 1247_vm            # visibility map
│   │   ├── ...
│   └── 16384/                 # your db (OID 16384)
│       ├── 2619               # your table data file (heap)
│       ├── 2619_fsm           # free space map
│       ├── 2619_vm            # visibility map
│       ├── 2619_index         # index (if created)
│       └── ...
├── global/                   # cluster-wide tables (pg_database, users, etc.)
├── pg_wal/                   # write-ahead log (formerly pg_xlog)
├── pg_commit_ts/             # commit timestamps
├── pg_multixact/             # multixact (row locking info)
├── pg_tblspc/                # symlinks to tablespaces elsewhere
├── pg_stat/                  # stats snapshots
├── pg_stat_tmp/              # transient stats
├── postgresql.conf
├── pg_hba.conf
└── pg_ident.conf
```