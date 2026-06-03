def validate_age(age: int):

    if age < 18:

        raise ValueError(
            "Employee age must be at least 18"
        )

    return True