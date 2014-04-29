Learn to Program: The Fundamentals // Assignment 2


A2 Problem Domain: Deoxyribonucleic Acid (DNA)

The problem domain for A2 is Deoxyribonucleic Acid (DNA), the double-stranded molecule that encodes genetic information for living organisms. DNA is made up of four kinds of nucleotides, which are molecules that bond together to form DNA sequences.

The four nucleotides are adenine (A), guanine (G), cytosine (C), and thymine (T). Each strand of DNA is a sequence of nucleotides, for example AGCTAC. In a program, we will use a string representation of this, "AGCTAC".

DNA has 2 strands in a double helix. The nucleotides in one strand are bonded to the nucleotides in the other strand. A and T can be bonded together, and thus complement each other; similarly, C and G are complements of each other.

You can see a picture of this on the Wikipedia page for DNA. The two strands in DNA are complementary because each nucleotide in one strand is bonded with its complement in the other strand. Thus, given the DNA sequence ACGTACG, its complementary strand is TGCATGC.

A DNA sequence is a sequence of nucleotides, such as TCATGT.

======================================================================================================================
Functions description:

get_length:
(str) -> int	 The parameter is a DNA sequence. Return the length of that sequence.

is_longer:
(str, str) -> bool	 The two parameters are DNA sequences. Return True if and only if the first DNA sequence is longer than the second DNA sequence. (If they are the same length, return False.)

count_nucleotides:
(str, str) -> int	 The first parameter is a DNA sequence and the second parameter is a nucleotide ('A', 'T', 'C' or 'G'). Return the number of times the nucleotide occurs in the DNA sequence.

contains_sequence:
(str, str) -> bool	 The two parameters are DNA sequences. Return True if and only if the first DNA sequence contains the second DNA sequence.

is_valid_sequence:
(str) -> bool	 The parameter is a potential DNA sequence. Return True if and only if the DNA sequence is valid (that is, it contains no characters other than 'A', 'T', 'C' and 'G').

insert_sequence:
(str, str, int) -> str	 The first two parameters are DNA sequences and the third parameter is an index. Return the DNA sequence obtained by inserting the second DNA sequence into the first DNA sequence at the given index. (You can assume that the index is valid.)

get_complement:
(str) -> str	 The first parameter is a nucleotide ('A', 'T', 'C' or 'G'). Return the nucleotide's complement.

get_complementary_sequence:
(str) -> str	 The parameter is a DNA sequence. Return the DNA sequence that is complementary to the given DNA sequence.

