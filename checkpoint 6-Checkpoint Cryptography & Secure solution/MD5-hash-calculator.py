import hashlib

def calculate_md5_hash(input_string):
    md5_hash = hashlib.md5(input_string.encode()).hexdigest()
    return md5_hash