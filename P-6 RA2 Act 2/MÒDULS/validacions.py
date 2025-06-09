import re

def es_email_valid(email):
    return bool(re.match(r"[^@]+@[^@]+\.[^@]+", email))

def es_telefon_valid(telefon):
    return telefon.isdigit() and len(telefon) in [9, 10]
