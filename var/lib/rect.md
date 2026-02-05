
1: Oh my god.

0: I know.

1: This is a fucking abomination!

0: I think some sympathy might be called fo---

1: What the hell is this?

## /var/lib/mysql

```
/var/lib/mysql
├── .rocksdb
│   ├── LOG
│   ├── MANIFEST-000002
│   └── OPTIONS-000001
├── #innodb_temp
│   ├── temp_1.ibd
│   └── temp_2.ibd
├── analytics
│   ├── daily_rollups.ibd
│   ├── db.opt
│   ├── events_2025_09.ibd
│   ├── events_2025_10.ibd
│   └── session_facts.ibd
├── auto.cnf
├── binlog.000001
├── binlog.000002
├── binlog.000003
├── binlog.index
├── ca.pem
├── client-cert.pem
├── client-key.pem
├── ib_logfile0
├── ib_logfile1
├── ibdata1
├── ibtmp1
├── myapp
│   ├── customers.ibd
│   ├── customers_cfg.bin
│   ├── db.opt
│   ├── indexeS
│   │   ├── customers_name.idx
│   │   ├── orders_created_at.idx
│   │   └── products_sku.idx
│   ├── inventory.ibd
│   ├── inventory_cfg.bin
│   ├── order_items.ibd
│   ├── order_items_cfg.bin
│   ├── orders.ibd
│   ├── orders_cfg.bin
│   ├── products.ibd
│   └── products_cfg.bin
├── mysql
│   ├── columns_priv.ibd
│   ├── db.ibd
│   ├── db.opt
│   ├── gtid_executed.ibd
│   ├── help_category.ibd
│   ├── help_keyword.ibd
│   ├── help_relation.ibd
│   ├── help_topic.ibd
│   ├── innodb_index_stats.ibd
│   ├── innodb_table_stats.ibd
│   ├── plugin.ibd
│   ├── procs_priv.ibd
│   ├── roles_mapping.ibd
│   ├── tables_priv.ibd
│   ├── time_zone.ibd
│   ├── time_zone_leap_second.ibd
│   ├── time_zone_name.ibd
│   ├── time_zone_transition.ibd
│   ├── time_zone_transition_type.ibd
│   └── user.ibd
├── performance_schema
│   ├── db.opt
│   ├── events_stages_current.ibd
│   ├── events_stages_history.ibd
│   ├── events_stages_history_long.ibd
│   ├── events_statements_current.ibd
│   ├── events_statements_history.ibd
│   ├── events_statements_history_long.ibd
│   ├── events_waits_current.ibd
│   ├── events_waits_history.ibd
│   ├── events_waits_history_long.ibd
│   ├── host_cache.ibd
│   ├── memory_summary_global_by_event_name.ibd
│   ├── session_connect_attrs.ibd
│   ├── setup_actors.ibd
│   ├── setup_consumers.ibd
│   ├── setup_instruments.ibd
│   ├── setup_objects.ibd
│   ├── setup_timers.ibd
│   └── users.ibd
├── private_key.pem
├── public_key.pem
├── replication
│   ├── relay-log.000001
│   ├── relay-log.000002
│   ├── relay-log.000003
│   └── relay-log.index
├── server-cert.pem
├── server-key.pem
├── sys
│   ├── db.opt
│   └── sys_config.ibd
├── tmp
│   ├── ibtmp2
│   └── qs_12345.tmp
├── undo_001
└── undo_002

```

0: It's a database.

1: THIS is a database?

0: Yeah.

1: Who did this to our filesystem?!

0: Must be the previous owners.

1: Who wants to live like this?

0: They don't visit. I mean, the database people. They don't come here often. To the filesystem, to see what happens on the ground when the relationals move in.

1: This is the most abhorrent---

0: Look, it's not their fault. At least not always. And don't linger. It's not safe.

## /var/lib/postgresql

```
/var/lib/postgres
├── backups
│   └── .keep
├── data
│   ├── PG_VERSION
│   ├── base
│   │   ├── 1
│   │   │   ├── 1247
│   │   │   ├── 1247_fsm
│   │   │   ├── 1247_vm
│   │   │   ├── 2600
│   │   │   ├── 2601
│   │   │   ├── 2602
│   │   │   ├── 2603
│   │   │   ├── 2604
│   │   │   ├── 2605
│   │   │   ├── 2606
│   │   │   ├── 2607
│   │   │   ├── 2608
│   │   │   ├── 2609
│   │   │   ├── 2610
│   │   │   └── 2611
│   │   ├── 16384
│   │   │   ├── 1255
│   │   │   ├── 1259
│   │   │   ├── 2618
│   │   │   ├── 2619
│   │   │   ├── 2619_fsm
│   │   │   ├── 2619_vm
│   │   │   ├── 2662
│   │   │   ├── PG_VERSION
│   │   │   └── pg_toast
│   │   │       ├── 2619
│   │   │       ├── 2619_fsm
│   │   │       └── 2619_vm
│   │   ├── 24576
│   │   │   ├── 34567
│   │   │   ├── 34567_fsm
│   │   │   ├── 34567_vm
│   │   │   ├── 34568
│   │   │   ├── 34569
│   │   │   ├── 34570
│   │   │   ├── PG_VERSION
│   │   │   └── pg_toast
│   │   │       ├── 34569
│   │   │       ├── 34569_fsm
│   │   │       └── 34569_vm
│   ├── current_logfiles
│   ├── global
│   │   ├── pg_control
│   │   ├── pg_filenode.map
│   │   ├── pg_internal.init
│   │   └── pg_stat
│   │       └── global.stat
│   ├── log
│   │   └── postgresql-2025-10-01_000000.log
│   ├── pg_commit_ts
│   │   └── 0000
│   ├── pg_hba.conf
│   ├── pg_ident.conf
│   ├── pg_logical
│   │   ├── mappings
│   │   │   └── 00000000000000000000
│   │   ├── replorigin_checkpoint
│   │   └── snapshots
│   │       └── 00000000000000000000.snap
│   ├── pg_multixact
│   │   ├── members
│   │   │   └── 0000
│   │   └── offsets
│   │       └── 0000
│   ├── pg_notify
│   │   └── 0000
│   ├── pg_replslot
│   │   └── .keep
│   ├── pg_serial
│   │   └── 0000
│   ├── pg_snapshots
│   │   └── .keep
│   ├── pg_stat
│   │   ├── DB_0.stat
│   │   ├── DB_16384.stat
│   │   └── DB_24576.stat
│   ├── pg_stat_tmp
│   │   └── global.tmp
│   ├── pg_subtrans
│   │   └── 0000
│   ├── pg_tblspc
│   │   └── 16700
│   │       ├── LOG
│   │       │   └── 000000010000000000000001
│   │       └── PG_VERSION
│   ├── pg_twophase
│   │   └── .keep
│   ├── pg_wal
│   │   ├── 000000010000000000000001
│   │   ├── 000000010000000000000002
│   │   ├── 000000010000000000000003
│   │   ├── 000000010000000000000004
│   │   ├── 000000010000000000000005
│   │   └── archive_status
│   ├── pg_xact
│   │   └── 0000
│   ├── postgresql.conf
│   ├── postmaster.opts
│   └── postmaster.pid
└── tblspc
    └── ts_appdata
        └── 24576
            ├── 60000
            ├── 60000_fsm
            └── 60000_vm

```

1: That's was fu---

0: Ok look, the most extreme cases of the rectangle degeneration aren't the same as the others.

1: What are the others?

0: Remember in /etc/group when we met "The Rows."

1: The Rhos?

0: Exactly.

1: Ooooooh. So what's the deal with them?

0: Follow me.

## Lonely, Seeking Relations

0: They're lost logicians.

1: What?!

0: At least in my opinion. Look there's no consensus on what's going on with the most extreme variants of the Rectangle disorder, but personally I think it's a different thing entirely.

1: Different how?

0: Different underlying cause from the others. Here, I'll show you.

![[limbo.jpg]]


1: What's that?

0: Sorry. Mistake. Had it in the same folder with the database stuff for some reason.

1: What is it?

0: Limbo. A place where lost souls go, in an old mythology.

1: Ok so what did you want to show me?

0: Here.

![[relational-model-and-lost-logicians-01.png]]

1: I'm getting tired.

0: Common symptom. Here, take this.

_(Narrator: 0 hands 1 a small tablet that reads ADXR 30mg.)_

1: What's this?

0: Anti-Database salts, Extended Release.

_(Narrator: 1 swallows the capsule.)_

1: What's it for?

0 It's not safe to be exposed to the things we're about to read for more than a few minutes without a sizable dose of this stuff. You could lose consciousness and I'd have to carry you back /home.

1: What about you?

0: Already took mine this morning.

1: Did you know we'd be coming here today?

0: No. But I take it regularly just in case. You can never be too safe when it comes to these things.

1: What things?

## The Labyrinth of Lost Logicians

0: Read this.

![[relational-model-and-lost-logicians-02.png]]

1: Why is it so boring?

0: Wait for the medicine to kick in.

1: How long will that---

0: As long as it takes...

_(Narrator: 0 and 1 wait for an undefined amount of time.)_

1: Wow I feel amazing!

0: Now read the picture up there again.

1: Hey cardinality! Like Cantor right?

0: There ya go.

![[relational-model-and-lost-logicians-03.png]]

1: Consistent. Inconsistent. Subset. Wait a minute, this feels like foundation stuff!

0: Keep reading.

![[relational-model-and-lost-logicians-04.png]]

1: Cartesian product.

![[relational-model-and-lost-logicians-05.png]]

1: First normal form. This feels like Kleene!

0: Don't linger. Keep reading.

![[relational-model-and-lost-logicians-06.png]]

1: Wow it lets you do things the designers didn't anticipate!

0: That's every programming language! Don't trust the marketing.

1: What marketing?

0: See the highlighted part? These things are popular with businesses. Anything popular with businesses has a massive amount of marketing energy trying to sell you services and support and all other sorts of fluff. Don't trust your feelings on anything until you divide by the size of the marketing team.

1: Divide by the---

0: Christ, we didn't do that principle yet? I've been neglecting the principles side of this. Ok noted. We'll get there soon.

![[relational-model-and-lost-logicians-07.png]]

1: Zero look at this! _A relational model is a formal system... define a set of logical propositions... validly infer._ This is logic!

0: You wouldn't be the first of our people to feel that way. Don't linger.

![[relational-model-and-lost-logicians-08.png]]

1: Mathematical sets. Ooh there's something called the Information Principle.

0: _(Grabs 1's arm firmly but gently, leading the two of them ahead.)_

![[relational-model-and-lost-logicians-09.png]]

1: Predicate. First order logic. Projection. Relation Universe. Schema. There were foundational people here weren't there?

0: Yes... In a sense.

![[relational-model-and-lost-logicians-10.png]]

1: Look they even have axioms! And theorems! Closure. Completion. This feels like home! How the hell did I never see this stu---

goto: [[daemon.out|/var/lock/daemon.out]]