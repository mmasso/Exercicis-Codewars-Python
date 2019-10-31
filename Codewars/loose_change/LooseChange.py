
"""crear un diccionario donde aparecen el nombre de las monedas y el nume de
 ellas de devuelves
-Crear un diccionario nickels, pennis, .... y cuartes en las claves.
Valor:
 crear litas en el diccionario con el nombre de las monedas.
 2. crear lista con el valor de las modenas.
 3. usasr metodo para crear un diccionario con dos listas. (Libro de python)
 4. Crear lista de las monedas ordenadas. cojer diccionario y coger solo los
 valores y usamos un metodo para ordenarlo.
 5. y lo último convertirlo en una lista con el nombre de coins.
 6. Algotimo:
    lista=changes  (monedas utilizadas)
    mientras haya cambio por devolver -> coger cambio que nos han pasado,
    mientras que no sea == 0 tenemos que ir recorriendo la lista de las monedas
     e ir sacando de ahí las monedas.
    Hacer diccionario que coja las monedas (changeS) para asociar cuantas
    monedas tiene que devolver.
"""


def loose_change(input):
    list_monedas = ["Pennies", "Nickels", "Dimes", "Quarters"]
    list_valor = [1, 5, 10, 25]
    wallets = dict(zip(list_monedas, list_valor))
    assert wallets == {"Pennies": 1, "Nickels": 5, "Dimes": 10, "Quarters": 25}
    if input == 0:
        return {"Pennies": 0, "Nickels": 0, "Dimes": 0, "Quarters": 0}
    assert list_valor == [1, 5, 10, 25]
    change = []
    variable_input = input
    while variable_input > 0:
        if variable_input > list_valor[-1]:
            variable_input = variable_input - list_valor[-1]
            change = change.append(list_valor[-1])
        else:
            list_valor = list_valor.remove(list_valor[-1])
    for a in change:
        single_change = []
        single_counts = change.count(a)
        if single_counts in change:
            single_change = single_change.remove(a)
        else:
            single_change = single_change.append(a)
    single_change = reversed(single_change)
    final_change = dict(zip(list_monedas, single_change))
    return final_change
