# Test cases

This document describes test cases for the Python script developed to count the occurrence of each nucleotide in a DNA sequence contained in a text file from the command line.

The test cases have been designed considering the different functionalities of the script as well as the possible errors that may arise.

The script allows you to provide the path of a file with the DNA sequence and count the occurrence of all the nucleotides or a particular one.

Test cases cover the key features of the program and test various conditions to ensure the robustness and reliability of the script.

Successful execution of these test cases ensures that the script is ready for use and can handle different input conditions and error situations.

Below are the details of the test cases. Each test case includes a description of the test case, the input data used, and the expected result.
    
    
### Test 1: Positional argument only

- Description: The script is executed when only the file with the DNA sequence is provided on the command line.
- Input data: Path to the input file containing DNA sequences.
- Rexpected result: The occurrence of the four nucleotides in the DNA sequence is printed.


### Test 2: No positional argument

- Description: The script can´t work properly when the file with the DNA sequence isn´t provided on the command line.
- Input data: No data.
- Rexpected result: An error message is printed stating that the input file is missing.


### Test 3: Positional argument and optional argument
- Description: The script can executed when the file with the DNA sequence is provided on the command line and the options -n and --nucleotides are used with a given nucleotide o nucleotides. In this case, In this case, only occurrences of the nucleotides indicated by the optional argument will be counted.
- Input data: Path to the input file containing DNA sequences.
- Rexpected result: In this case, only occurrences of the nucleotides indicated by the optional argument will be counted.




        
        
