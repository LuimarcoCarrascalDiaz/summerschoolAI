import secrets  # Use secrets module for cryptographically secure random numbers

def generate_uuid():
    base_string = "".join([str(secrets.randbelow(10)) for _ in range(32)])  # Generate 32 random digits
    uuid_string = ""
    for i, char in enumerate(base_string):
        if i in [8, 13, 18, 23]:
            uuid_string += "-"
        else:
            uuid_string += char
    return uuid_string

print(generate_uuid())
