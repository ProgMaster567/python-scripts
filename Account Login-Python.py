a=['Arun','Mani']
b=['123','135']
def login():
    while True:
        c=str(input('Username:'))
        if c in a:
            print('Username Exists')
            cp = b[a.index(c)]
            e=4
            while e>0:
                d=str(input('Password:'))
                if (d==cp):
                    print('Login Successful')
                    break
                else:
                    e=e-1
                    print('Login Error:Incorrect Password')
                    if e>0:
                        print(f'You have {e} attempts left')
                    else:
                        print(f"{c}'s Account LOcked")
                        
            if (d==cp):
                continue
        else:
            print('Invalid Username')
login()
        
        
