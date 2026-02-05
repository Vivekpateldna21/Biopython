from Bio import SeqIO
from Bio.SeqUtils import gc_fraction
from collections import Counter

def sequence_analysis(fasta_file):
    record = SeqIO.read(fasta_file, "fasta")
    seq = record.seq.upper()

    print("Sequence ID:", record.id)
    print("Description:", record.description)

    # 1. Sequence Length
    print("Sequence Length:", len(seq))

    # 2. GC Content
    gc = gc_fraction(seq) * 100
    print("GC Content (%):", round(gc, 2))

    # 3. Nucleotide Composition
    comp = Counter(seq)
    print("Nucleotide Composition:")
    print("A:", comp.get("A", 0))
    print("T:", comp.get("T", 0))
    print("G:", comp.get("G", 0))
    print("C:", comp.get("C", 0))

    # 4. DNA → Protein Translation
    protein = seq.translate(to_stop=True)
    print("Protein Length:", len(protein))
    print("Protein Sequence (first 60 aa):")
    print(protein[:60])

if __name__ == "__main__":
    sequence_analysis("GSK3A.fasta")
