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
        python3 count_atgc.py dna_sequence.txt --nucleotides g c
"""


# library
import argparse

# functions


def count_symbols(dna_sequence, nucleotides):
    """Count occurrences of symbols in a DNA sequence."""
    # Convert nucleotides to lowercase
    nucleotides = set(nucleotide.lower() for nucleotide in nucleotides)
    # List to store counts
    counts = [0] * len(nucleotides)
    # List to store invalid characters
    invalid_chars = []
    # Iterate over each character in the DNA sequence
    for char in dna_sequence:
        # Convert the character to lowercase
        char_lower = char.lower()
        # Check if the character is a valid nucleotide
        if char_lower in nucleotides:
            # Increment the count for the corresponding nucleotide
            index = list(nucleotides).index(char_lower)
            counts[index] += 1
        else:
            # Add invalid character to the list
            invalid_chars.append(char)
    return counts, invalid_chars

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
                        choices=['A', 'T', 'G', 'C', 'a', 't', 'g', 'c'],
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
            counts, invalid_chars = count_symbols(
                dna_sequences, args.nucleotides)
            # Print the results
            print("\nOccurrences of nucleotides:")
            for i in range(len(args.nucleotides)):
                nucleotide = args.nucleotides[i]
                count = counts[i]
                print(f"Occurrences of '{nucleotide}': {count}")
            # Print invalid characters
            if invalid_chars:
                print("\nInvalid characters found in the file:")
                invalid_chars_filtered = [char for char in invalid_chars if char not in {
                    'A', 'T', 'G', 'C', 'a', 't', 'g', 'c'}]
                print(" ".join(invalid_chars_filtered))

    except IOError as ex:
        print("Sorry, couldn't find the file: " + ex.strerror)
        return


if __name__ == "__main__":
    main()
