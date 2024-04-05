"""
SYNOPSIS
    python3 count_atgc -inputfile <file>

DESCRIPTION
    This script counts the occurrence of nucleotides 'A', 'T', 'G' and 'C' in a file with a .txt extension.
    The file is provided as a positional argument from the command line.

OPTIONS
    - inputfile
        Path to the input file containing DNA sequences.

EXAMPLES
    Command line usage example:
        python3 count_atgc.py dna_sequence.txt
"""

# library
import argparse

# functions


def count_symbols(dna_sequence):
    """Count occurrences of symbols in a DNA sequence."""
    count_A = dna_sequence.count('A')
    count_T = dna_sequence.count('T')
    count_G = dna_sequence.count('G')
    count_C = dna_sequence.count('C')
    return count_A, count_T, count_G, count_C


# main

def main():
    # Create ArgumentParser object
    parser = argparse.ArgumentParser(
        description='Count occurrences of DNA symbols in a file.')

    # Add argument for input file
    parser.add_argument('inputfile', type=str,
                        help='Path to the input file containing DNA sequences.')

    # Parse command-line arguments
    args = parser.parse_args()

    # Read DNA sequences from the input file
    try:
        with open(args.inputfile, 'r') as file:
            dna_sequences = file.read()
    except FileNotFoundError:
        print("Error: File not found.")
        return

    # Count occurrences of symbols
    count_A, count_T, count_G, count_C = count_symbols(dna_sequences)

    # Print the results
    print("Occurrences of 'A':", count_A)
    print("Occurrences of 'T':", count_T)
    print("Occurrences of 'G':", count_G)
    print("Occurrences of 'C':", count_C)


if __name__ == "__main__":
    main()
