# Test cases

This document describes test cases for the Python script developed to count the occurrence of each nucleotide in a DNA sequence contained in a text file from the command line.

The test cases have been designed considering the different functionalities of the script as well as the possible errors that may arise.

The script allows you to provide the path of a file with the DNA sequence and count the occurrence of all the nucleotides or a particular one.

Test cases cover the key features of the program and test various conditions to ensure the robustness and reliability of the script.

Successful execution of these test cases ensures that the script is ready for use and can handle different input conditions and error situations.

Below are the details of the test cases. Each test case includes a description of the test case, the input data used, and the expected result.
    
    
**Test Case 1: User Input Validation**

For this test case, provide incorrect file paths or files that do not exist and verify if the program handles this properly.

- The FILE doesn´t exists

```{python}
python count-atcg the_file_does_not_exist.txt -n ACGT
```

- The file exists but not in this PATH ( create the file in the test directory and use it for this case)

```{python}
python count-atcg /incorrect/path/to/file.txt -n ACGT
```
---

**Test Case 2: Output Verification**

Create a text file with an explicit DNA sequence (Example: "ATCGGGTAC"), where you know the correct count of each nucleotide (2 'A's, 2 'T's, 3 'G's, 2 'C's in this example). The result from the program should match the exact counts.

```{python}
python count-atcg dna_sequence.txt -n ACGT
```

The output 

```
A: 2
C: 2
G: 3
T: 2
```

---

**Test Case 3: Handling Lowercase DNA Sequences**

Test with a file that has the DNA sequence in lowercase (Example: "atcgggtac"). Most implementations should consider both uppercase and lowercase, meaning 'A' and 'a' should be counted as the same element.

```{python}
python count-atcg lowercase_dna_sequence.txt -n ACGT
```

The output

```
A: 2
C: 2
G: 3
T: 2
```

---

**Test Case 4: Handling Invalid Characters**

Test with a file that has invalid characters, i.e., characters apart from 'A', 'T', 'C' and 'G' (or their respective lowercase), for exmaple "ATCGXXXTAC". Your program should either ignore these characters or handle this in some specific way.

```{python}
python count-atcg invalid_dna_sequence.txt -n ACGT
```

The output:  (The X are ignored)

```
A: 2
C: 2
G: 1
T: 2
```

---

**Test Case 5: Testing with an Empty File**

This is another important test case to assure that your program can correctly handle the situation where the provided file is empty.

```{python}
python count-atcg empty_file.txt -n ACGT
```

The output: 

```
A: 0
C: 0
G: 0
T: 0
```

---

**Test Case 6: Performance Test**

Test your program with a very large DNA file to see how it handles large files and to measure how long it takes to process.

```{python}
time python count-atcg large_dna_file.txt -n ACGT
```

The output: 

```
A: 
C: 
G: 
T: 
```

        
        
