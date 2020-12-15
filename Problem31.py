coin_worth = [1, 2, 5, 10, 20, 50, 100, 200]


def amount_of_sums(x):
    sums = 0

    for pound2 in range(0, 1+1):
        total1 = pound2*coin_worth[7]
        if total1 == x:
            sums += 1
            break

        for pound1 in range(0, 2+1):
            total2 = total1 + pound1*coin_worth[6]
            if total2 == x:
                sums += 1
                break

            for pence50 in range(0, 4+1):
                total3 = total2 + pence50*coin_worth[5]
                if total3 == x:
                    sums += 1
                    break

                for pence20 in range(0, 10+1):
                    total4 = total3 + pence20*coin_worth[4]
                    if total4 == x:
                        sums += 1
                        break

                    for pence10 in range(0, 20+1):
                        total5 = total4 + pence10*coin_worth[3]
                        if total5 == x:
                            sums += 1
                            break

                        for pence5 in range(0, 40+1):
                            total6 = total5 + pence5*coin_worth[2]
                            if total6 == x:
                                sums += 1
                                break

                            for pence2 in range(0, 100+1):
                                total7 = total6 + pence2*coin_worth[1]
                                if total7 == x:
                                    sums += 1
                                    break

                                for pence1 in range(0, 200+1):
                                    total8 = total7 + pence1*coin_worth[0]
                                    if total8 == x:
                                        sums += 1
                                        break
    return sums


print(amount_of_sums(200))
