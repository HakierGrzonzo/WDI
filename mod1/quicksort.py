def quicksort(zbiór):
    if len(zbiór) <= 1:
        return zbiór, None
    else:
        element_rozdzielający = zbiór[0]
        A = list()
        B = list()
        divs = list() # jeśli się powtażają
        for element in zbiór:
            if element < element_rozdzielający:
                A.append(element)
            elif element > element_rozdzielający:
                B.append(element)
            else:
                divs.append(element)
        Anew, msgA = quicksort(A)
        Bnew, msgB = quicksort(B)
        msg = {
                "div" : element_rozdzielający,
                "A" : A,
                "B" : B,
                "msgA" :  msgA,
                "msgB" :  msgB
                }
        return Anew + divs + Bnew, msg

print(quicksort("ok, Boomer")[1])
