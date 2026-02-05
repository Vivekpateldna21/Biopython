from Bio import SeqIO
from Bio.Seq import Seq

def find_orf(fasta_file):
    record = SeqIO.read(fasta_file, "fasta")
    dna_seq = record.seq.upper()

    stop_codons = ["TAA", "TAG", "TGA"]
    longest_orf = Seq("")
    longest_len = 0

    # Check all 3 reading frames
    for frame in range(3):
        seq = dna_seq[frame:]
        for i in range(0, len(seq)-2, 3):
            codon = seq[i:i+3]
            if codon == "ATG":  # Start codon
                for j in range(i, len(seq)-2, 3):
                    stop = seq[j:j+3]
                    if stop in stop_codons:
                        orf = seq[i:j+3]
                        if len(orf) > longest_len:
                            longest_len = len(orf)
                            longest_orf = orf
                        break

    protein = longest_orf.translate(to_stop=True)

    print("Longest ORF length (bp):", len(longest_orf))
    print("Protein length (aa):", len(protein))
    print("Protein sequence (first 60 aa):")
    print(protein[:60])

    return protein


# Run
find_orf("GSK3A.fasta")