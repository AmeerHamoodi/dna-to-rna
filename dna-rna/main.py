dnaRnaPairs = {
    "A": "U",
    "T": "A",
    "G": "C",
    "C": "G"
}


class DnaToRna:
    def __init__(this):
        print("")
        print("|||||||||||||| DNA -> RNA ||||||||||||||")
        print("Created by: Ameer Hamoodi :)")
        this.sequence = input("Enter the DNA sequence you would like to convert: ")
        this.rnaSequence = ""
        this.convert()

    def convert(this):
        error = 0
        for dna in this.sequence:
            try:
                this.rnaSequence += dnaRnaPairs[dna]
            except Exception as e:
                print(dna + " is not a DNA nucleotide!")
                error += 1

        if error > 0:
            print("Invalid sequence!")
        else:
            print("RNA: " + this.rnaSequence)


main = DnaToRna()
