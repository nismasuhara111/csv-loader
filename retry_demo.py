from decorators import retry


attempts = 0


@retry(max_attempts=3)
def unreliable_function():
    global attempts

    attempts += 1

    if attempts < 3:
        raise ValueError("Temporary failure")

    return "Success after retry"


result = unreliable_function()

print("Result:")
print(result)