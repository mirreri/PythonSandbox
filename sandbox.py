while True:
    try:
        ## Python 3.x
        inp = input ("> ")
        if (inp == ""):
            continue

        exec (inp)
    except Exception as e:
        print ('Exception:', e)
