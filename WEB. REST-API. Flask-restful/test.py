import requests


API_URL = "http://127.0.0.1:5000/api/v2/"


# All jobs:
print(requests.get(API_URL + "jobs").json())

# Correct create job:
print(requests.post(API_URL + "jobs", json={
    "team_leader": 1,
    "job": "correct",
    "work_size": 1,
}).json())

# Invalid create job (not team_leader):
print(requests.post(API_URL + "jobs", json={
    "job": "empty",
    "work_size": 0.2,
}).json())

# All jobs:
print(requests.get(API_URL + "jobs").json())

# One job with correct id:
print(requests.get(API_URL + "jobs/1").json())

# One job with int invalid id:
print(requests.get(API_URL + "jobs/1000").json())

# Delete job with correct id:
print(requests.delete(API_URL + "jobs/2").json())

# Delete job with invalid id:
print(requests.delete(API_URL + "jobs/2020").json())

# All jobs:
print(requests.get(API_URL + "jobs").json())
