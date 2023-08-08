adad = int(input("enter your number: "))
ad = str(adad)
a = 0 
b = 0
if adad.count("0") !=0:
    a += adad.count("0")
    if adad.count("2") !=0:
        a += adad.count("2")
        if adad.count("4") !=0:
            a += adad.count("4")
            if adad.count("6") !=0:
                a += adad.count("6")
                if adad.count("8") !=0:
                    a += adad.count("8")
                    if  adad.count("1") !=0:
                        b += adad.count("1")
                        if adad.count("3") !=0:
                            b += adad.count("3")
                            if adad.count("5") !=0:
                                b += adad.count("5")
                                if adad.count("7") !=0:
                                    b += adad.count("7")
                                    if adad.count("9") !=0:
                                        b += adad.count("9")
                                        if a > b:
                                            print("adad shoma zoj ast")
                                        elif b > a:
                                            print("adad shoma fard ast")
                                        else:
                                            print("adad ba ham mosavi ast")

