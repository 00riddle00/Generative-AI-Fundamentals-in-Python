def validate_user_id(user_id):
    if not isinstance(user_id, int):
        raise TypeError("User ID must be an integer.")
    if user_id <= 0:
        raise ValueError("User ID must be a positive integer.")
    print("User ID", user_id, "is valid!")


test_case = "sampleID"
validate_user_id(test_case)
