# Counter of the occurrence of DNA nucleotides in a file

Date: April 5, 2024

**Participants**:

- Gabriel Alberto Garcia Vargas : gabrielg@lcg.unam.mx

## Problem description
Counts the occurrences of the symbols 'A', 'T', 'G' and 'C' of a DNA strand that is read through a file.


## Requirements

### Functional Requirements

- The program should accumulate the occurrence of the nucleotide characters 'A', 'C', 'G', and 'T' each into distinct variables.
- The program should accept a path to a DNA sequence file as a command line argument.
- The nucleotides to be counted should be passed as an optional command line argument.
- If the optional nucleotide argument is omitted, the program should default to counting all 4 nucleotides: 'A', 'C', 'G', and 'T'.

### Non-functional Requirements

- The program will be developed in the Python programming language to ensure widespread compatibility and ease of use.
- Reading of command line arguments should be implemented using the argparse library for Python to allow for flexible and user-friendly command-line interfaces.
- Code developed for the program should adhere to PEP8 standards for Python code style. This enhances readability and maintainability of the code.
- The program should handle errors gracefully, providing meaningful error messages for potential issues like incorrect file paths or invalid file content.
- The efficiency of implementation should be considered, as DNA sequence files can be large and require significant processing. The program should aim to handle large input files swiftly.

## Analysis and design

Based on the requirements, we might have the following case:

```
         +---------------+
         |   User        |
         +-------+-------+
                 |
                 | 1. User provides input file and the nucleotides to be counted
                 v
         +-------+-------+
         |   count-atgc  |
         |               |
         |               |
         |               |
         +---------------+
```

### Use Case 1: Nucleotide Counting

**Actor**: User

**Main Flow**:

- The user starts the program from the command line, providing the path to the DNA sequence file and optionally, the nucleotides they wish to count.
- The system verifies if the file exists.
- The system reads and loads the file content into memory.
- The system counts the occurrence of each provided nucleotide (or all nucleotides if none provided) in the loaded DNA sequence.
- The system outputs the count of each nucleotide to the command line.

**Alternative Flow A:**

1a. The provided file does not exist or cannot be read: 
	1a1. The system throws an error and ends execution.

**Alternative Flow B:**

1b. No nucleotides to count are provided by user: 
	1b1. The system defaults to counting the occurrence of all nucleotides ('A', 'C', 'G', 'T').

**Alternative Flow C:**

3c. The provided file is empty: 
	3c1. The system throws an error and ends execution.


