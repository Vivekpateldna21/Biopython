from Bio import SeqIO

def load_sequence(fasta_path):
    record = SeqIO.read(fasta_path, "fasta")
    sequence = record.seq.upper()

    valid_nucleotides = set("ATGC")
    seq_type = "DNA" if set(sequence).issubset(valid_nucleotides) else "Protein"

    return {
        "id": record.id,
        "description": record.description,
        "sequence": sequence,
        "length": len(sequence),
        "type": seq_type
    }


if __name__ == "__main__":
    data = load_sequence("GSK3A.fasta")

    print("Sequence ID:", data["id"])
    print("Description:", data["description"])
    print("Sequence Type:", data["type"])
    print("Sequence Length:", data["length"])