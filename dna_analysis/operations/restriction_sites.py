def find_restriction_sites(sequence, enzymes):
    """
    Encuentra los sitios de corte de enzimas de restricción en una secuencia de ADN.

    Args:
        sequence (str): La secuencia de ADN en la que buscar los sitios de corte.
        enzymes (list): Una lista de nombres de enzimas de restricción a buscar.

    Returns:
        dict: Un diccionario donde las claves son nombres de enzimas y los valores son listas de posiciones de sitios de corte.
    """
    enzyme_sites = {enzyme: [] for enzyme in enzymes}  # Inicializar un diccionario para almacenar los sitios por enzima

    for enzyme in enzymes:
        enzyme_site_positions = []  # Lista para almacenar las posiciones de los sitios de corte para la enzima actual
        current_position = sequence.find(enzyme)  # Encontrar la primera aparición de la enzima en la secuencia

        while current_position != -1:
            enzyme_site_positions.append(current_position)
            current_position = sequence.find(enzyme, current_position + 1)  # Buscar más sitios de corte
       
        enzyme_sites[enzyme] = enzyme_site_positions

    return enzyme_sites

def count_restriction_sites(sequence, enzymes):
    """
    Cuenta la frecuencia de aparición de sitios de corte de enzimas de restricción en una secuencia de ADN.

    Args:
        sequence (str): La secuencia de ADN en la que contar los sitios de corte.
        enzymes (list): Una lista de nombres de enzimas de restricción a contar.

    Returns:
        dict: Un diccionario donde las claves son nombres de enzimas y los valores son las frecuencias de aparición de los sitios.
    """
    enzyme_counts = {enzyme: 0 for enzyme in enzymes}  # Inicializar un diccionario para contar las frecuencias por enzima

    for enzyme in enzymes:
        count = 0
        current_position = sequence.find(enzyme)  # Encontrar la primera aparición de la enzima en la secuencia

        while current_position != -1:
            count += 1
            current_position = sequence.find(enzyme, current_position + 1)  # Buscar más sitios de corte

        enzyme_counts[enzyme] = count

    return enzyme_counts
