def validate_types(data: dict, schema: dict):
    """
    data   : incoming dictionary from client
    schema : expected type definition
    """
    for field, expected_type in schema.items():
        if field not in data:
            raise TypeError(f"Missing field: {field}")

        value = data[field]

        if isinstance(expected_type, list):
            if not isinstance(value, list):
                raise TypeError(
                    f"Field '{field}' expected list, got {type(value).__name__}"
                )
            element_type = expected_type[0]
            for item in value:
                if not isinstance(item, element_type):
                    raise TypeError(
                        f"Field '{field}' expected list of {element_type.__name__}, "
                        f"got {type(item).__name__}"
                    )
        else:
            if not isinstance(value, expected_type):
                raise TypeError(
                    f"Field '{field}' expected {expected_type.__name__}, "
                    f"got {type(value).__name__}"
                )
