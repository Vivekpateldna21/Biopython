from Bio.Blast import NCBIXML

with open("blast_result.xml") as handle:
    blast_record = NCBIXML.read(handle)

print("Query length:", blast_record.query_length)

top_alignment = blast_record.alignments[0]
hsp = top_alignment.hsps[0]

print("Top hit:", top_alignment.hit_def)
print("Length:", top_alignment.length)
print("E-value:", hsp.expect)
print("Identity:", hsp.identities, "/", hsp.align_length)
