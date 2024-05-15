import argparse
from dna_analysis.operations.restriction_sites import find_restriction_sites, count_restriction_sites
# Importar la función read_dna_sequence
from dna_analysis.utils.file_io import read_dna_sequence


def main():
    # Configurar el argumento de línea de comandos para el nombre del archivo de entrada
    parser = argparse.ArgumentParser(
        description="Find restriction enzyme sites in a DNA sequence from a file")
    parser.add_argument("input_file", type=str,
                        help="Path to the input file containing DNA sequence")
    parser.add_argument("--enzymes", nargs="+", type=str,
                        required=True, help="List of restriction enzyme names")
    args = parser.parse_args()

    # Leer la secuencia de ADN desde el archivo de entrada utilizando read_dna_sequence
    try:
        # Utilizar la función read_dna_sequence
        sequence = read_dna_sequence(args.input_file)
    except FileNotFoundError:
        print(f"Error: File '{args.input_file}' not found.")
        return
    except IOError as e:
        print(f"Error reading file: {e}")
        return

    # Encontrar los sitios de restricción para las enzimas especificadas
    enzyme_sites = find_restriction_sites(sequence, args.enzymes)

    # Contar la frecuencia de aparición de sitios para cada enzima
    enzyme_counts = count_restriction_sites(sequence, args.enzymes)

    # Mostrar los resultados
    print(f"Sequence: {sequence}")
    for enzyme, sites in enzyme_sites.items():
        print(f"Enzyme: {enzyme}")
        print(f"Sites: {sites}")
        print(f"Frequency: {enzyme_counts.get(enzyme, 0)}")


if __name__ == "__main__":
    main()
