# 코돈을 입력받아 아미노산을 출력하는 프로그램
print("="*30)
print("Four kinds of bases(A,G,C,T)")
print("XXX can stop this program.")
print("="*30)

while True:
    codon = input("Enter the three-base codon to build: ")
    if codon == "GCT" or codon == "GCC" or codon == "GCA" or codon == "GCG":
        print("Ala(A)")
    elif codon == "CGT" or codon == "CGC" or codon == "CGA" or codon == "CGG" or codon == "AGA" or codon == "AGG":
        print("Arg(R)")
    elif codon == "XXX":
        print("Program stopped.")
        break
    else:
        print("Can't translate this codon.")