import secrets

# Generate a secure secret key
secret_key = secrets.token_hex(24)
print(f"Your new SECRET_KEY: {secret_key}") 