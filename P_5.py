text = "Once upon"

def encryption(text,n):
    up_alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lo_alp  ="abcdefghijklmnopqrstuvwxyz"
    n  = n % 26
    encrypted_text = ""
    for char in text:
        if char in up_alp:
            encrypted_text += up_alp[(up_alp.index(char) + n) % len(up_alp)]
        elif char in lo_alp:
            encrypted_text += lo_alp[(lo_alp.index(char) + n) % len(lo_alp)]
        else:
            encrypted_text += char
    return encrypted_text



