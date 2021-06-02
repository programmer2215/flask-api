import requests as rq

base = 'http://127.0.0.1:5000/krypton/'


a = rq.put(base + "launches/1",  {
    "launch_date": "2021-03-30 18:30:00", 
    "vehicle_name": "Starship SN11", 
    "mission_status" : "FAILED"
})
print(a.json())

a = rq.put(base + "launches/2",  {
    "launch_date": "2021-03-30 18:30:00", 
    "vehicle_name": "Starship SN11", 
    "mission_status" : "FAILED"
})

input()

a = rq.get(base + "launches/1")
print(a.json())
input()
a = rq.get(base + "launches/2")
print(a.json())
