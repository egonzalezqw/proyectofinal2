import streamlit as st

st.set_page_config(
    page_title="Linux Survival Challenge",
    page_icon="🐧"
)

st.title("🐧 Linux Survival Challenge")

st.header("🏝️ Misión 1")

st.code("""
#!/bin/bash

_______="Linux"

echo $curso
""", language="bash")

respuesta = st.text_input(
    "¿Qué palabra falta?"
)

if st.button("Validar"):

    if respuesta.lower().strip() == "curso":
        st.success("✅ Correcto")
    else:
        st.error("❌ Incorrecto")
