# This is a project to make a morse code encoder and deceoder
# might be used for urgent communication
prompt = input("Enter a message to encode: ")
mapping = {
    # gonna learn about morse code rn
    #alphabets
    "A": "._", "B": "_...", "C": "_._.", "D": "_..", 
    "E": ".", "F": ".._.", "G": "__.", "H": "....", 
    "I": "..", "J": ".___", "K": "_._", "L": "._..", 
    "M": "__", "N": "_.", "O": "___", "P": ".__.", 
    "Q": "__._", "R": "._.", "S": "...", "T": "_", 
    "U": ".._", "V": "..._", "W": ".__", "X": "_.._", 
    "Y": "_.__", "Z": "__..",

    #numbers
    "1": ".____", "2": "..___", "3": "...__", "4": "...._",
    "5": ".....", "6": "_....", "7": "__...", "8": "___..",
    "9": "____.", "0": "_____"
}