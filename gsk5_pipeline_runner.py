import subprocess
import sys

print("="*50)
print("AUTOMATED BIOINFORMATICS PIPELINE STARTED")
print("="*50)

# FASTA file
fasta_file = "recA_ecoli.fasta"

try:
    print("\n[STEP 1] Sequence Input & Validation")
    subprocess.run([sys.executable, "gsk1_seq_input.py"], check=True)

    print("\n[STEP 2] Sequence Analysis")
    subprocess.run([sys.executable, "gsk2_seq_analysis.py"], check=True)

    print("\n[STEP 3] ORF Detection & Translation")
    subprocess.run([sys.executable, "gsk3_orf_detection.py"], check=True)

    print("\n[STEP 4] BLAST result interpretation")
    subprocess.run([sys.executable, "gsk4_check_blast.py"], check=True)

    print("\nPipeline executed successfully ✅")

except Exception as e:
    print("\nPipeline failed ❌")
    print("Error:", e)

print("="*50)
print("PIPELINE COMPLETED")
print("="*50)
