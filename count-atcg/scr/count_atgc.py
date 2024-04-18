"""
SYNOPSIS
    python3 count_atgc -inputfile <file> [-n]

DESCRIPTION
    This script counts the occurrence of nucleotides 'A', 'T', 'G' and 'C' in a file with a .txt extension.
    The file is provided as a positional argument from the command line.

OPTIONS

    inputfile  
        Path to the input file containing DNA sequences.
        
    -n  --nucleotides
        Nucleotides to be counted.


EXAMPLES
    Command line usage examples:
    
        python3 count_atgc.py dna_sequence.txt
        python3 count_atgc.py dna_sequence.txt -n A T
        python3 count_atgc.py dna_sequence.txt --nucleotides A T
"""


# library
import argparse

# functions


def count_symbols(dna_sequence, nucleotides):
    """Count occurrences of symbols in a DNA sequence."""
    # Convert both the DNA sequence and nucleotides to lowercase
    dna_sequence = dna_sequence.lower()
    nucleotides = [nucleotide.lower() for nucleotide in nucleotides]
    # Count occurrences of symbols
    counts = {nucleotide: dna_sequence.count(
        nucleotide) for nucleotide in nucleotides}
    return counts

# main


def main():
    # Create ArgumentParser object
    parser = argparse.ArgumentParser(
        description='Count occurrences of DNA symbols in a file.')

    # Add argument for input file
    parser.add_argument('inputfile', type=str,
                        help='Path to the input file containing DNA sequences.')

    # Add optional argument for nucleotides of interest
    parser.add_argument('-n', '--nucleotides', nargs='+', default=['A', 'T', 'G', 'C'],
                        help='List of nucleotides to count. Default: A, T, G, C.')

    # Parse command-line arguments
    args = parser.parse_args()

    # Read DNA sequences from the input file
    try:
        with open(args.inputfile, 'r') as file:
            dna_sequences = file.read()
    except IOError as ex:
        print("Sorry, couldn't find the file: " + ex.strerror)
        return

    # Count occurrences of symbols
    counts = count_symbols(dna_sequences, args.nucleotides)

    # Print the results
    print("Occurrences of nucleotides:")
    for nucleotide, count in counts.items():
        print(f"Occurrences of '{nucleotide}': {count}")


if __name__ == "__main__":
    main()
