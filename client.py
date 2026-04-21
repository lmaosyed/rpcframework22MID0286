import json
from server import server 

request = json.dumps({
    "method": "calculate_grade_average",
    "params": {
        "name": "Bob",
        "id": 202,
        "grades": [70, 75, 80]
    }
})

response = server.handle_request(request)
print(response)
