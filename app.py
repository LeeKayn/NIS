import os
import time
import pyfiglet
import streamlit as st
from Extract.url_main import scan_url
from Extract.PE_main import scan_pe_file

def run_PE():
    file = st.file_uploader("Upload the file to scan", type=["exe"])
    if file is not None:
        result = scan_pe_file(file.name)
        st.write(f"PE file analysis result: {result}")

def run_URL():
    url = st.text_input("Enter the URL to scan")
    if url:
        result = scan_url(url)
        st.write(f"URL scan result: {result}")

def start():
    st.set_page_config(
        page_title="Malware Detector",
        page_icon=":robot:",
        layout="wide",
    )

    st.title(pyfiglet.figlet_format("Malware Detector"))
    st.write(" Welcome to antimalware detector")

    options = ["PE scanner", "URL scanner", "Exit"]
    choice = st.selectbox("Select an option", options)

    if choice == "PE scanner":
        run_PE()
    elif choice == "URL scanner":
        run_URL()
    else:
        st.write("Exiting...")
        time.sleep(3)
        st.stop()

start()