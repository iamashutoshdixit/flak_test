import bcrypt


def get_password_hashed(plain_password):
    salt = b'$2b$12$jt8g2FpYl3KxGf7VytbyB.'
    byte_pass = plain_password.encode("utf-8")

    hashed_pass = bcrypt.hashpw(byte_pass, salt)

    return hashed_pass

def get_password_verify(hashed_password, request_password):
    request_password = request_password.encode("utf-8")

    return bcrypt.checkpw(request_password, hashed_password)

def get_jwt_token(payload):
    pass