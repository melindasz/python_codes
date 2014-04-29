def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len (dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return len (dna1) > len (dna2)


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    return dna.count (nucleotide)



def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    return dna2 in dna1


def is_valid_sequence (dna):
    """ (str) -> bool

    Return True if and only if dna is a valid DNA sequence,
    so it contains no characters other than 'A', 'T', 'C' and 'G'.

    >>> is_valid_sequence ('ATCGGC')
    True
    >>> is_valid_sequence ('GTCC')
    True
    >>> is_valid_sequence ('aggtCC')
    False
    >>> is_valid_sequence ('agg13cc')
    False
    
    """
    valid_chars = True
    
    for char in dna:
        if char in ('ATCG') and valid_chars:
            valid_chars = True
            
        else :
            valid_chars = False
        
    return valid_chars

def insert_sequence (dna1, dna2, index):
    """ (str, str, int) -> str

    Return the DNA sequence obtained by inserting DNA sequence dna2
    into DNA sequence dna1, at the given index.
    
    >>> insert_sequence('CCGG', 'AT', 2)
    'CCATGG'
    >>> insert_sequence('CCGG', 'AT', 0)
    'ATCCGG'
    >>> insert_sequence('CCGG', 'AT', 3)
    'CCGATG'
    >>> insert_sequence('CCGG', 'AT', 4)
    'CCGGAT'
    """
    return dna1 [:index] + dna2 + dna1 [index:]

    
def get_complement (nucleotide):
    """(str) -> str
    Return the complement of nucleotide.
    'A' and 'T' are complements of each other.
    'C' and 'G' are complements of each other.
    
    >>> get_complement ('A')
    'T'
     >>> get_complement ('T')
    'A'
     >>> get_complement ('C')
    'G'
     >>> get_complement ('G')
    'C'

    """
    if nucleotide == 'A':
        nucleotide = 'T'
        
    elif nucleotide == 'T':
        nucleotide = 'A'
        
    elif nucleotide == 'C':
        nucleotide = 'G'
        
    elif nucleotide == 'G':
        nucleotide = 'C'
        

    return nucleotide



def get_complementary_sequence (dna):
    """(str) -> str
    Return the DNA sequence that is complementary to the given dna.
    
    >>> get_complementary_sequence ('ATCC')
    'TAGG'
    >>> get_complementary_sequence ('ACGTACG')
    'TGCATGC'
    """
    dna_sequence = ''
    for nucleotide in dna:
        dna_sequence = dna_sequence + get_complement (nucleotide)
    return dna_sequence
        














