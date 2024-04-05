# Counter of the occurrence of DNA nucleotides in a file

Date: April 5, 2024

**Participants**:

- Gabriel Alberto Garcia Vargas : gabrielg@lcg.unam.mx

## Problem description
Counts the occurrences of the symbols 'A', 'T', 'G' and 'C' of a DNA strand that is read through a file.



## Requirements specification

Functional requirements 

- The occurrence of the characters 'A', 'C', 'G' and 'T' is accumulated in a different variable for each character.
- To work correctly, the user must enter the path to the file containing the DNA sequence.

Non-functional requirements

- The script is easy to use but only runs from the command line.
- Requisito 2
- Program maintenance can be done over relatively long periods of time due to the simple structure of the script.


## Analysis and design

```
python3 count_atgc.py <file> [-n]
```

The input file must be a plain text file with a .txt extension.


#### Test: 

```
         +---------------+
         |   User        |
         +-------+-------+
                 |
                 | 1. User provides input file
                 v
         +-------+-------+
         |   Program     |
         |               |
         |               |
         |               |
         +---------------+
```

- **Actor**: User
- **Description**: The user provides the input file from the command line and can use the -n or --nucleotides option to count the occurrence of a particular nucleotide.
- **Flujo principal**:

	1. The user provides the input file from the command line.
	1. The occurrence of the characters 'A', 'C', 'G' and 'T' in the provided file is counted.
	1. The occurrence of the characters is printed.
	
- **Alternative flows**:
	- If a file is not provided, the program should print an error message to the screen.       

