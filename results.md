
Implemented an RPC framework in Python supporting object-based remote
procedure calls with strict type validation on the server side.

- Remote invocation of `calculate_grade_average(StudentProfile profile)`
- Object marshalling using JSON
- Server-side `validate_types()` function
- Type mismatch detection with descriptive TypeErrors

If a client sends:
- A string instead of an integer for `id`
- A non-integer inside `grades`

The server raises a `TypeError` and rejects the request.

The framework ensures strong runtime safety and prevents malformed
client data from being processed on the server.
