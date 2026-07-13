unifi@unified:/usr/lib/unifi/logs$ mongo --port 27117 --shell
mongo --port 27117 --shell
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27117/
MongoDB server version: 3.6.3
type "help" for help
Welcome to the MongoDB shell.
For interactive help, type "help".
For more comprehensive documentation, see
        http://docs.mongodb.org/
Questions? Try the support group
        http://groups.google.com/group/mongodb-user
2026-07-13T03:04:41.406+0100 I STORAGE  [main] In File::open(), ::open for '/home/unifi/.mongorc.js' failed with No such file or directory
Server has startup warnings:
2026-07-13T01:50:59.482+0100 I STORAGE  [initandlisten]
2026-07-13T01:50:59.482+0100 I STORAGE  [initandlisten] ** WARNING: Using the XFS filesystem is strongly recommended with the WiredTiger storage engine
2026-07-13T01:50:59.482+0100 I STORAGE  [initandlisten] **          See http://dochub.mongodb.org/core/prodnotes-filesystem
2026-07-13T01:51:00.189+0100 I CONTROL  [initandlisten]
2026-07-13T01:51:00.189+0100 I CONTROL  [initandlisten] ** WARNING: Access control is not enabled for the database.
2026-07-13T01:51:00.189+0100 I CONTROL  [initandlisten] **          Read and write access to data and configuration is unrestricted.
2026-07-13T01:51:00.189+0100 I CONTROL  [initandlisten]
> ls
lsls
[native code]
> databases
dadatabases
2026-07-13T03:04:48.589+0100 E QUERY    [thread1] ReferenceError: databases is not defined :
@(shell):1:1
> get databases
geget databases
2026-07-13T03:04:54.904+0100 E QUERY    [thread1] SyntaxError: missing ; before statement @(shell):1:4
> show dbs
shshow dbs
ace       0.002GB
ace_stat  0.000GB
admin     0.000GB
config    0.000GB
local     0.000GB
