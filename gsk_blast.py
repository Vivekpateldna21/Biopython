from Bio.Blast import NCBIWWW
result_handle = NCBIWWW.qblast(
    program = "blastp",
    database = "nr",
    sequence = "METDCNPMELSSMSGFEEGSELNGFEGTDMKDMRLEAEAVVNDVLFAVNNMFVSKSLRCADDVAYINVETKERNRYCLELTEAGLKVVGYAFDQVDDHLQTPYHETVYSLLDTLSPAYREAFGNALLQRLEALKRDGQS"
)
# print(result_handle)

with open("blast_result.xml", "w") as b:
    b.write(result_handle.read())
    print("Blast Performed Successfully")