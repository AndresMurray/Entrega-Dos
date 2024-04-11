def new_structure (names,goals,goals_avoided,assists): ##lista de diccionarios . zip devuelve las 3 estruct en una
    """Esta función recibe las 3 listas y dado que todas tienen la misma cantidad de elementos,
     recorre a cada una desde el principio hasta el final, generando una nueva lista de diccionarios,
      donde cada diccionario tiene la info de cada jugador/a """
    names_list=names.split()
    list=[]
    for i in range(0,len(names_list)):
        list.append({'name': names_list[i], 'goals': goals[i], 'goals_avoided': goals_avoided[i],'assists': assists[i]})
    ##list comprehension y llamar una nuenva funcion new dictionary 
    return list

def top_scorer(structure):
    """ Esta función recorre la lista de diccionarios accediendo a través de la clave 'goals'
    a la cantidad de goles de cada jugador para buscar el maximo goleador"""
    max=0
    for dic in structure:
        goal=dic['goals']
        if goal > max:
            max=goal
            name=dic['name']
    print(f'El nombre del maximo/a goledor/a es: {name}')
    print(f'Marco un total de {max} goles')
    


    
def influence(structure): ##utilizando lambda y map
    """Esta función busca el jugador/a más influyente utilizando un map que devuelve un iterador,
    en este caso en la variable influencias donde se encuentra un valor con la influencia de cada jugador.
    Luego, se busca el máximo de esos y se imprime el nombre.
    """
    max=0
    index=-1
    influencias = map(lambda dic: dic['goals'] * 1.5 + dic['goals_avoided'] * 1.25 + dic['assists'], structure) 
    for elem in influencias:## devuelve un iterable
        index+=1
        if elem>max:
            max=elem
            ind_max=index
    max_name=structure[ind_max]['name']
    print(f'El nombre del jugador/a más influyente es: {max_name}')

"""def influence(structure):  ##tambien podria realizarse sin map y lambda, lo que resulta más legible
    max=0
    
    for dic in structure:
        current_name=dic['name']
        current_influence=dic['goals']*1.5+dic['goals_avoided']*1.25+dic['assists']*1 
        if(current_influence>max):
            max=current_influence
            max_name=current_name
    print(f'el nombre del jugador/a mas influyente es: {max_name}')"""

def average_goals(structure):
    """Esta función calculo el promedio de goles de todo el equipo recorriendo la lista de diccionarios
    y accediendo a los goles a través de su clave, va sumando los goles en la variable goals, y finalmente
    lo divide por la cantidad de partidos"""
    goals=0
    for dic in structure:
        goals+=dic['goals']
    print(f'el promedio de gol por partidos de todo el equipo es: {goals/25}')

def goal_scorer_average(structure):
    """Esta función calcula el promedio de goles por partido del maximo goleador, para esto obtiene el maximo goleador
    recorriendo la estructura y luego divide la cantidad de goles por la cantidad de partidos jugados
    """
    max=0
    for dic in structure:
        goal=dic['goals']
        if goal > max:
            max=goal
            name=dic['name']
    print(f'El nombre del maximo/a goledor/a es: {name}')
    print(f'Su promedio de goles es {max/25} goles por partido')
