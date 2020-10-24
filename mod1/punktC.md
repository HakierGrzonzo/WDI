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
        # nie trzeba sortować zbiorów pustych oraz jednoelementowych
        return zbiór
    else:
        element_rozdzielający = zbiór[0]
        a = list() # większe
        b = list() # równe
        c = list() # mniejsze
        for element in zbiór:
            if element < element_rozdzielający:
                a.append(element)
            elif element > element_rozdzielający:
                c.append(element)
            else:
                b.append(element)
        a = quicksort(a)
        c = quicksort(c)
        return a + b + c
```

