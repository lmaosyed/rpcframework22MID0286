from rpc import RPCServer

def calculate_grade_average(profile: dict) -> float:
    grades = profile["grades"]
    return sum(grades) / len(grades)

server = RPCServer()

student_schema = {
    "name": str,
    "id": int,
    "grades": [int]
}

server.register_method(
    "calculate_grade_average",
    calculate_grade_average,
    student_schema
)

if __name__ == "__main__":
    import json

    request = json.dumps({
        "method": "calculate_grade_average",
        "params": {
            "name": "Alice",
            "id": 101,
            "grades": [80, 90, 85]
        }
    })

    response = server.handle_request(request)
    print(response)
