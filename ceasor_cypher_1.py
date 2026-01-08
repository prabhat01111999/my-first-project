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





l = [2, 5, 3, 7, 4]

def two_sum(l, target):
    result=[]
    for i in range(len(l)):
        for j in range(len(l)):
            if i == j:
                pass
            else:
                if l[i] + l[j] == target:
                    result.append(i)
                else:
                    pass
    return result




class Cards(object):
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def get_value(self):
        return self.value

    def get_suit(self):
        return self.suit

    def __str__(self):
        return str(self.value) + " of " + str(self.suit)
