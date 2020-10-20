# Wyszukiwanie binarne - charakterystyka
**Wyszukiwanie binarne** *(ang. binarny search)* - algorytm stosowany do wyszukiwania
elementów w posegregowanych zbiorach. Cechuje się złożonością czasową ***O*(log<sub>2</sub>n)**,
podczas gdy wyszukiwanie liniowe (element po elemencie), ma złożoność *O*(n).
>*Prosty wykres ukazujący zależność czasu wyszukiwania od ilości elementów w danym zbiorze
dla wyszkiwania liniowego (czerwony) oraz binarnego (niebieski)*
![Image](https://cdn.kastatic.org/ka-perseus-graphie/3d79e6ce2ddfed0d66917d585511f807797652fe.svg)
>
## Zasada działania
Główną ideą wyszukiwania binarnego jest podział elementów w przeszukiwanym uporządkowanym zbiorze danych
(np. tablicy) na coraz to mniejsze zbiory, tak by optymalnie ograniczyć zakres poszukiwania.
Należy zaznaczyć, że elementy muszą być ze sobą **porównywalne**, tzn. spośrod dowolnych dwóch elementów
da się wyłonić większy i mniejszy (np. po wartości lub nazwie).

Algorytm znajduje środkowy element tablicy (lub pierwszy z pary środkowych elementów)
i porównuje go z poszukiwanym. Jeżeli są sobie równe, to poszukiwanie zostaje zakończone,
w przeciwnym wypadku obszar poszukiwania zostaje odpowiednio zawężony:
- gdy środkowy element jest mniejszy od szukanej, za dolną granicę uznaje się kolejny element,
a górna pozostaje bez zmian
- gdy środkowy element jest większy od szukanej, za górną granicę uznaje się poprzedni element,
a dolna pozostaje bez zmian

Następnie powyższe kroki zostają powtórzone. Jeżeli element nie zostanie znaleziony,
zwracana jest odpowiednia wartość wskazująca na błąd (np. *-1* lub *null*).

*Poniżej przedstawiona jest implementacja algorytmu w języku python:*
```python
# searches for specified item in chosen collection
def binary_search(item, collection):
    lower_bound = 0
    upper_bound = len(collection) - 1

    while lower_bound <= upper_bound:
        mid = (lower_bound + upper_bound) // 2

        if collection[mid] == item:
            return mid

        if collection[mid] < item:
            lower_bound = mid + 1
        else:
            upper_bound = mid - 1

    # if item not found
    return -1
```
## Przykład
Dana jest struktura *tuple* przechowująca 13 pierwszych liczb Fibonacciego:
```python
fib = (1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233)
```
Naszym zadaniem jest znalezienie indeksu liczby 144.

Za dolną granicę uznajemy liczbę 1 o indeksie *0*, natomiast za górną liczbę 233 o indeksie *12*

1. W pierwszym kroku znadujemy indeks środkowego elementu: `mid = (0 + 12) / 2 = 6`.
2. Pod indeksem *6* kryje się liczba 13, która jest mniejsza od naszej szukanej,
dlatego zmieniamy dolną granicę na `mid + 1 = 7`, a górna nadal wynosi *12*.
3. Powtarzamy kroki od **1.** - szukamy indeksu środkowego elementu: `mid = (7 + 12) / 2 = 9.5`.
Niecałkowitą wartość zaokrągamy w dół.
4. Liczba pod indeksem *9* (55) jest mniejsza od szukanej, dlatego zmnieniamy dolną granicę na
`mid + 1 = 10`
5. Ponownie sprawdzamy liczbę pod indeksem `mid = (10 + 12) / 2 = 11`
i tym razem jest to nasza szukana.
Zwracana jest wartość *11* będąca w rzeczy samej indeksem liczby 144 w ***fib***.

Proszę zwrócić uwagę, że w celu znalezienia odpowiedniego indeksu
zostały sprawdzone jedynie trzy liczby: **13**, **55** oraz **144**,
podczas gdy zastosowanie wyszukiwania liniowego do tego samego problemu
wiązałoby się ze sprawdzeniem aż 12! Wyszukiwanie binarne w najgorszych przypadkach musi wykonać
log<sub>2</sub>n + 1 kroków (z zaokrągleniem w dół), gdzie n to liczba elementów w przeszukiwanym zbiorze.
Oznacza to, że w celu znalezienia wybranego gatunku w tablicy składającej się z 8.7 miliona znanych gatunków
algorytm musiałby w **najgorszym** przypadku zbadać jedynie **24 elementy**!

Warto również zaznaczyć, że wyszukiwanie binarne może zwracać nieprzewidywalne wyniki,
jeżeli w przeszukiwanym zbiorze znajdują się identyczne elementy i staramy się je znaleźć.
Z wyszukiwaniem liniowym nie wiąże się taki problem. 