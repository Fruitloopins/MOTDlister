from mcstatus import JavaServer
from tinydb import TinyDB

db = TinyDB("statuses.json")
server = JavaServer.lookup("earthmc.net")

statuses = []
while True:
    serverstatus = server.status()
    status = serverstatus.description
    if status not in statuses:
        db.insert({"status":status})
        statuses.append(status)
        print(statuses)
        print(len(statuses))
    else:
        pass