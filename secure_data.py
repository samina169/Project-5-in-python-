import streamlit as st
from cryptography.fernet import Fernet

# Function to generate a key
def generate_key():
    return Fernet.generate_key()

# Function to encrypt data
def encrypt_data(data, key):
    fernet = Fernet(key)
    encrypted = fernet.encrypt(data.encode())
    return encrypted

# Function to decrypt data
def decrypt_data(encrypted_data, key):
    fernet = Fernet(key)
    decrypted = fernet.decrypt(encrypted_data).decode()
    return decrypted

# Streamlit app
st.title("Secure Data Encryption")

# Generate a key
key = generate_key()
st.write("Encryption Key (keep it safe):", key.decode())

# Input data to encrypt
data_to_encrypt = st.text_area("Enter data to encrypt:")

if st.button("Encrypt"):
    if data_to_encrypt:
        encrypted_data = encrypt_data(data_to_encrypt, key)
        st.success("Encrypted Data:")
        st.code(encrypted_data.decode())

# Input data to decrypt
data_to_decrypt = st.text_area("Enter data to decrypt:")

if st.button("Decrypt"):
    if data_to_decrypt:
        try:
            decrypted_data = decrypt_data(data_to_decrypt.encode(), key)
            st.success("Decrypted Data:")
            st.code(decrypted_data)
        except Exception as e:
            st.error("Decryption failed: " + str(e))
