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
    # Convert nucleotides to lowercase
    nucleotides = [nucleotide.lower() for nucleotide in nucleotides]
    # List to store counts
    counts = [0] * len(nucleotides)
    # Iterate over each character in the DNA sequence
    for char in dna_sequence:
        # Convert the character to lowercase
        char_lower = char.lower()
        # Check if the character is a valid nucleotide
        if char_lower in nucleotides:
            # Increment the count for the corresponding nucleotide
            index = nucleotides.index(char_lower)
            counts[index] += 1
        else:
            # Print an error message for invalid characters
            print(f"Sequence contains '{char}', it is an invalid character.")
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
            # Check if the file is empty
            if len(dna_sequences) == 0:
                print("Sorry, the file is empty.")
                return
            # Check if the file contains uppercase letters
            if any(char.isupper() for char in dna_sequences):
                # Convert the entire content to lowercase
                dna_sequences = dna_sequences.lower()
                print(
                    "The file contained uppercase letters. Converted to lowercase for counting.")
            # Count occurrences of symbols
            counts = count_symbols(dna_sequences, args.nucleotides)
            # Print the results
            print("\nOccurrences of nucleotides:")
            for i in range(len(args.nucleotides)):
                nucleotide = args.nucleotides[i]
                count = counts[i]
                print(f"Occurrences of '{nucleotide}': {count}")
    except IOError as ex:
        print("Sorry, couldn't find the file: " + ex.strerror)
        return


if __name__ == "__main__":
    main()
