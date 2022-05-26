import sys

while True:
    try: 
        a = int(sys.stdin.readline())
        n = "1" 
        while True: 
            if int(n) % a == 0:
                print(len(n))
                break
            n += "1"

            '''
            n = str(n)
            n = n + "1" 
            n = int(n)

        print(len(str(n)))
'''
    except:
        break