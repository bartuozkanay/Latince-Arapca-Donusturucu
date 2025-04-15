import streamlit as st

st.image(https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQbAWnnf0epJMRJJPOT4B0mQ5rcuizGJgWagg&s)

with st.sidebar:
    st.header("Hazırlayan: Bartu Özkanay")

latince_arapca = {
    "a": "ا", "b": "ب", "c": "ج", "ç": "چ", "d": "د", "e": "e", "f": "ف",
    "g": "گ", "ğ": "غ", "h": "ه", "ı": "ی", "i": "ی", "j": "ژ", "k": "ك",
    "l": "ل", "m": "م", "n": "ن", "o": "و", "ö": "ۆ", "p": "پ", "r": "ر",
    "s": "س", "ş": "ش", "t": "ت", "u": "و", "ü": "ۈ", "v": "ڤ", "y": "ی",
    "z": "ز", " ": " "
}

def latince_osmanlica(text):
    result = ""
    for char in text.lower():
        result += latince_arapca.get(char, char)  
    return result[::-1]  

st.title("Latince - Osmanlıca Çevirici")

st.markdown("Latince harflerle yazılmış Türkçe metni Osmanlıca Arap harflerine dönüştürür.")

girdi = st.text_input("Latince metni giriniz:")

if girdi:
    yeni = latince_osmanlica(girdi)
    st.subheader("Osmanlıca Çeviri:")
    st.write(yeni)

