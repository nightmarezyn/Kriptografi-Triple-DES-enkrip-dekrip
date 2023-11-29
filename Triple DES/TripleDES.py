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
def encrypt_message(message, key):
    cipher = DES3.new(key, DES3.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(message.encode())
    return base64.b64encode(ciphertext).decode()

def decrypt_message(ciphertext, key):
    try:
        cipher = DES3.new(key, DES3.MODE_EAX)
        decrypted_message = cipher.decrypt_and_verify(base64.b64decode(ciphertext))
        return decrypted_message.decode()
    except Exception as e:
        st.error(f"Gagal melakukan dekripsi. {str(e)}")

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
def encrypt_page():
    st.title("🔒 Enkripsi")
    st.write("Masukkan pesan yang ingin dienkripsi dan tekan tombol Enkripsi.")

    message = st.text_area("Masukkan Pesan")
    key = get_random_bytes(24)  # 24 bytes key for Triple DES

    if st.button("Enkripsi"):
        if not message:
            st.warning("Masukkan pesan sebelum melakukan enkripsi.")
        else:
            encrypted_message = encrypt_message(message, key)
            st.success(f"Pesan berhasil dienkripsi: {encrypted_message}")

            st.subheader("Kunci Enkripsi (Simpan dengan baik):")
            st.text_area("Kunci", value=base64.b64encode(key).decode(), height=150, disabled=True)

# Decryption page
def decrypt_page():
    st.title("🔓 Dekripsi")
    st.write("Masukkan pesan yang ingin didekripsi dan kunci enkripsi yang sesuai. Tekan tombol Dekripsi.")

    encrypted_message = st.text_area("Masukkan Pesan Terenkripsi")
    key_input = st.text_area("Masukkan Kunci Enkripsi", help="Kunci yang dihasilkan saat proses enkripsi", disabled=False)

    key = base64.b64decode(key_input) if key_input else None

    if st.button("Dekripsi"):
        if not encrypted_message or not key:
            st.warning("Masukkan pesan terenkripsi dan kunci enkripsi yang sesuai.")
        else:
            decrypted_message = decrypt_message(encrypted_message, key)
            if decrypted_message:
                st.success(f"Pesan berhasil didekripsi: {decrypted_message}")

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

if __name__ == "main":
    main()