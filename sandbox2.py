def check_secure (inp):
    forbidden_module = [
        'import',
        'os',
        'sys',
        'eval'
        # add any module will be blocked
    ]
    
    for module in forbidden_module:
        if module in inp:
            raise Exception("Sorry, '"+ module +"' is not allowed.")

while True:
    try:
        ## Python 3.x
        inp = input ("> ")
        if (inp == ""):
            continue

        check_secure (inp)
        exec (inp)
    except Exception as e:
        print ('Exception:', e)
