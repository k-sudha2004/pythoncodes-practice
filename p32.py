# COMPLEMENTARY STRAND IN DNA
T = int(input())
complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
for _ in range(T):
    N = int(input())
    S = input().strip()  
    complementary_strand = "".join(complement[base] for base in S)
    print(complementary_strand)
