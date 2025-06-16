import random

codon_table = {
    'Phe': ['TTT', 'TTC'],
    'Leu': ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'],
    'Ile': ['ATT', 'ATC', 'ATA'],
    'Met': ['ATG'],
    'Val': ['GTT', 'GTC', 'GTA', 'GTG'],
    'Ser': ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'],
    'Pro': ['CCT', 'CCC', 'CCA', 'CCG'],
    'Thr': ['ACT', 'ACC', 'ACA', 'ACG'],
    'Ala': ['GCT', 'GCC', 'GCA', 'GCG'],
    'Tyr': ['TAT', 'TAC'],
    'His': ['CAT', 'CAC'],
    'Gln': ['CAA', 'CAG'],
    'Asn': ['AAT', 'AAC'],
    'Lys': ['AAA', 'AAG'],
    'Asp': ['GAT', 'GAC'],
    'Glu': ['GAA', 'GAG'],
    'Cys': ['TGT', 'TGC'],
    'Trp': ['TGG'],
    'Arg': ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
    'Gly': ['GGT', 'GGC', 'GGA', 'GGG'],
    'STOP': ['TAA', 'TAG', 'TGA']
}

bases = ['A', 'C', 'T', 'G']
random_sequence = ''.join(random.choices(bases, k=300))  # 300 bases = 100 codons

with open("sequence.txt", "w") as f:
    f.write(random_sequence)

codon_to_amino = {}
for amino, codons in codon_table.items():
    for codon in codons:
        codon_to_amino[codon] = amino

with open("sequence.txt") as f:
    sequence = f.read().strip().upper()

amino_counts = {}
for i in range(0, len(sequence) - 2, 3):
    codon = sequence[i:i+3]
    if codon in codon_to_amino:
        amino = codon_to_amino[codon]
        amino_counts[amino] = amino_counts.get(amino, 0) + 1

for amino in sorted(amino_counts):
    print(f"{amino}: {amino_counts[amino]}")
