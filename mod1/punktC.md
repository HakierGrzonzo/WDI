# Charakterystyka Quicksort



**Quicksort** działa poprzez dzielenie zbioru na coraz mniejsze zbiory, jest zatem algorytmem rekurencyjnym.

## Działanie:

1. Wybierz element z zbioru, zwany *elementem rozdzielającym* 

2. Elementy mniejsze przenieś do zbioru A, większe do zbioru B

3. Posortuj (tym algorytmem) zbiór A oraz B

4. Połącz posortowane zbiory, otrzymany zbiór jest finalnym posortowanym zbiorem

   

```python
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
```

