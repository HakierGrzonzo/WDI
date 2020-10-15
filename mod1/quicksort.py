def quicksort(zbiór):
    if len(zbiór) <= 1:
        return zbiór
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
        A = quicksort(A)
        B = quicksort(B)
        return A + divs + B

print(quicksort("ok, Boomer"))
