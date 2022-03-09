
for i in range(1, 33522128640): #33522128640 is the largest possible product (ignoring 20 factorial)
    if i % 20 == 0:
        if i % 19 == 0:
            if i % 18 == 0:
                if i % 17 == 0:
                    if i % 16 == 0:
                        if i % 15 == 0:
                            if i % 14 == 0:
                                if i % 13 == 0:
                                    if i % 12 == 0:
                                        if i % 11 == 0:
                                            print(i)
                                            break

# DONE (maybe a little long?)