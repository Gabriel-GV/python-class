def get_at_content(dna, num):
    dna = dna.replace('N', '')
    length = len(dna)
    a_count = dna.upper().count('A')
    t_count = dna.upper().count('T')
    at_content = (a_count + t_count) / length
    return round(at_content, num)


num = 2
at_content = get_at_content("ATGACTGGACCA", num)
print("ATGACTGGACCA" + ": " + str(at_content))
print("AT content ATGACTGGACCA  is " + str(get_at_content("ATGACTGGACCA", 4)))
print(get_at_content("ATGCGCGATCGATCGAATCG", 5))

# Paso de argumento por posicion
print(get_at_content("agctacgtacgtacgatcgatcgatcattatctagcatcgatctatcagcta", 1))

# Funcionan de igualmanera al asignar un valor a las varibles de cada argumento, paso de argumento por nombre
print(get_at_content(dna="CATCATGCACGAGATCATCAGCATATACGATTATCGACTACGAT", num=7))
print(get_at_content(num=7, dna="CATCATGCACGAGATCATCAGCATATACGATTATCGACTACGAT"))

# Esto si funciona
print(get_at_content("ACACGACTGACGACTATTATCGAGCCGATATCGACTAGCT", num=1))
# Esto no funciona ya que los argumento sposicionales (el 2) deben ir primero que los argumentos con nombre
print(get_at_content(dna="ATATAGGGCATCGACTATTCGATACGATCGATTACGATCGACTA", num=2))

# Probando funcion get_at_content
assert get_at_content("ATGC", 2) == 0.5
assert get_at_content("ATGCNNNNNNNNNNN", 2) == 0.5