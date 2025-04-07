
latince_arapca = {
    "a": "ا",
    "b": "ب",
    "c": "ج",
    "ç": "چ",
    "d": "د",
    "e": "e",
    "f": "ف",
    "g": "گ",
    "ğ": "غ",
    "h": "ه",
    "ı": "ی",   
    "i": "ی",
    "j": "ژ",
    "k": "ك",
    "l": "ل",
    "m": "م",
    "n": "ن",
    "o": "و",
    "ö": "ۆ",   
    "p": "پ",
    "r": "ر",
    "s": "س",
    "ş": "ش",
    "t": "ت",
    "u": "و",
    "ü": "ۈ",
    "v": "ڤ",
    "y": "ی",
    "z": "ز",
    " ": " "  }

def latince_osmanlica(text):
    result = ""
    for char in text.lower():
        result += latince_arapca.get(char, char)  
    return result[::-1]

if 1 == 1:
    print("Latince-Osmanlıca Dönüştürücü")
    girdi = input("lütfen Çevirmek istediğiniz Latince yazıyı girin")
    yeni_metin = latince_osmanlica(girdi)
    print(yeni_metin)