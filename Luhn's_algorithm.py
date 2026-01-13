credit_card = '371449635398431'


def cc_valid(credit_card):
    s = 0
    s1 = 0
    s2 = 0
    for i in range(len(credit_card) - 2, -1, -2):    
        # print(credit_card[i])
        for j in str(2*int(credit_card[i])):
            s1+=int(j)
            
    for t in range(len(credit_card) - 1, -1, -2): 
        # print(int(credit_card[t]))
        s2 += int(credit_card[t])
        
    s =  s1+s2
    if s%10 == 0:
        return 'Valid'
    else:
        return 'InValid'

print(cc_valid('371449635398431'))
print(cc_valid('5610591081018250'))
print(cc_valid('4222222222222'))
print(cc_valid('30569309026904'))
