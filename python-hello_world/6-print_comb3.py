#!/urs/bin/python3
for i in range(100):
    if i > 9:
        i += 2
        if i > 19:
            i += 3
            if i > 29:
                i += 4
                if i > 39:
                    i += 5
                    if i > 49:
                        i += 6
                        if i > 59:
                            i += 7
                            if i > 69:
                                i += 8
                                if i > 79:
                                    i += 9
                                    if i == 89:
                                        print(i)
                                        break

    print(i, end=", ")
