import streamlit as st

st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://upload.wikimedia.org/wikipedia/commons/4/4d/Flag_of_Ottoman_Empire_%281517-1793%29.png");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
    .main > div {
        background-color: rgba(255, 255, 255, 0.8);
        padding: 1.5em;
        border-radius: 10px;
        box-shadow: 0 0 15px rgba(0,0,0,0.2);
    }
    </style>
    """,
    unsafe_allow_html=True
)

with st.sidebar:
    st.header("Hazırlayan: Bartu Özkanay")

latince_arapca = {
    "a": "ا", "b": "ب", "c": "ج", "ç": "چ", "d": "د", "e": "ا", "f": "ف",
    "g": "گ", "ğ": "غ", "h": "ﺡ", "ı": "ی", "i": "ی", "j": "ژ", "k": "ك",
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

