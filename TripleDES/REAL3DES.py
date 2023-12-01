from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
import streamlit as st
import base64

# Set page configuration
st.set_page_config(
    page_title="Triple DES Encryption & Decryption",
    page_icon="🔐",
    layout='wide'
)

# Define functions for encryption and decryption
def triple_des_encrypt(message, key, mode='EEE'):
    key = key.ljust(24)  # Pastikan panjang kunci sesuai (24 byte)
    cipher = DES3.new(key.encode(), DES3.MODE_ECB)
    
    # Sesuaikan panjang pesan agar sesuai dengan blok kunci
    block_size = 8
    padded_message = message + ' ' * (block_size - len(message) % block_size)
    
    if mode == 'EEE':
        # Enkripsi tiga kali secara berturut-turut
        encrypted_message = cipher.encrypt(padded_message.encode())
        encrypted_message = cipher.encrypt(encrypted_message)
        encrypted_message = cipher.encrypt(encrypted_message)
    elif mode == 'EDE':
        # Enkripsi, dekripsi, dan enkripsi kembali
        encrypted_message = cipher.encrypt(padded_message.encode())
        encrypted_message = cipher.decrypt(encrypted_message)
        encrypted_message = cipher.encrypt(encrypted_message)
    elif mode == 'DED':
        # Dekripsi, enkripsi, dan dekripsi kembali
        encrypted_message = cipher.decrypt(padded_message.encode())
        encrypted_message = cipher.encrypt(encrypted_message)
        encrypted_message = cipher.decrypt(encrypted_message)
    else:
        # Mode tidak valid
        raise ValueError("Mode harus 'EEE', 'EDE', atau 'DED'")
    
    encoded_message = base64.b64encode(encrypted_message).decode()
    return encoded_message

def triple_des_decrypt(encoded_message, key, mode='EEE'):
    key = key.ljust(24)  # Pastikan panjang kunci sesuai (24 byte)
    cipher = DES3.new(key.encode(), DES3.MODE_ECB)
    encrypted_message = base64.b64decode(encoded_message)
    
    if mode == 'EEE':
        # Dekripsi tiga kali secara berturut-turut
        decrypted_message = cipher.decrypt(encrypted_message)
        decrypted_message = cipher.decrypt(decrypted_message)
        decrypted_message = cipher.decrypt(decrypted_message)
    elif mode == 'EDE':
        # Dekripsi, enkripsi, dan dekripsi kembali
        decrypted_message = cipher.decrypt(encrypted_message)
        decrypted_message = cipher.encrypt(decrypted_message)
        decrypted_message = cipher.decrypt(decrypted_message)
    elif mode == 'DED':
        # Enkripsi, dekripsi, dan enkripsi kembali
        decrypted_message = cipher.encrypt(encrypted_message)
        decrypted_message = cipher.decrypt(decrypted_message)
        decrypted_message = cipher.decrypt(decrypted_message)
    else:
        # Mode tidak valid
        raise ValueError("Mode harus 'EEE', 'EDE', atau 'DED'")
    
    decrypted_message = decrypted_message.decode()
    return decrypted_message

# Home page
def home_page():
    st.title("🏡 Home")
    st.markdown("""
        Selamat datang di aplikasi enkripsi dan dekripsi menggunakan algoritma Triple DES. Pilih menu di sebelah kiri untuk mulai.
    """)

    with st.expander("Definisi Triple DES"):
        st.markdown("""
            Triple DES (Triple Data Encryption Standard) adalah pengembangan dari DES (Data Encryption Standard) yang menggunakan tiga blok kunci untuk meningkatkan keamanan enkripsi. 
            Algoritma ini melakukan enkripsi tiga kali pada blok data yang sama menggunakan tiga kunci yang berbeda. Triple DES memperoleh keamanan tambahan dengan panjang kunci yang lebih besar (168 bit).
        """)

# Encryption page
# Encryption page
def encrypt_page():
    st.title("🔒 Enkripsi")
    st.write("Masukkan kalimat yang akan dienkripsi:")

    message = st.text_input("Kalimat:")
    key = st.text_input("Kata Kunci Enkripsi:")
    mode = st.selectbox("Pilih Mode Enkripsi:", ['EEE', 'EDE', 'DED'])

    if st.button("Enkripsi"):
        if not message or not key:
            st.warning("Masukkan kalimat dan kunci enkripsi terlebih dahulu.")
        else:
            encrypted_message = triple_des_encrypt(message, key, mode)
            st.success(f"Hasil enkripsi kalimat input adalah:\n{encrypted_message}")

# Decryption page
def decrypt_page():
    st.title("🔓 Dekripsi")
    st.write("Masukkan kalimat yang akan didekripsi:")

    message = st.text_input("Kalimat Terenkripsi:")
    key = st.text_input("Kata Kunci Enkripsi:")
    mode = st.selectbox("Pilih Mode Dekripsi:", ['EEE', 'EDE', 'DED'])

    if st.button("Dekripsi"):
        if not message or not key:
            st.warning("Masukkan kalimat terenkripsi dan kunci enkripsi terlebih dahulu.")
        else:
            decrypted_message = triple_des_decrypt(message, key, mode)
            st.success(f"Hasil dekripsi dari kalimat terenkripsi adalah:\n{decrypted_message}")

# About Us page
def about_us_page():
    st.title("👨‍💻 About Us 👨‍💻")
    st.markdown("""
        Kami adalah tim pengembang yang menciptakan aplikasi ini untuk keperluan enkripsi dan dekripsi menggunakan algoritma Triple DES.

        Anggota Tim:
        - 2210511044	Rahman Ilyas Al Kahfi
        - 2210511051	Salwa Nafisa
        - 2210511065	Intan Febyola Putri Dwina Sidabutar
        - 2210511068	Muhammad Nur Alam
        - 2210511073	Farel Bayhaqi
    """)

# Main App
def main():
    pages = {
        "Home": home_page,
        "Enkripsi": encrypt_page,
        "Dekripsi": decrypt_page,
        "About Us": about_us_page,
    }

    st.sidebar.title("Menu")
    selected_page = st.sidebar.radio("Pilih Halaman", list(pages.keys()))

    pages[selected_page]()

if __name__ == "__main__":
    main()
