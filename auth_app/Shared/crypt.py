from bcrypt import hashpw, gensalt

def gen_password(text: str, rounds=12) -> bytes:
    salt = gensalt(rounds)
    btext = text.encode('utf-8')
    return hashpw(btext, salt)
