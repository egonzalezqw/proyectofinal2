import streamlit as st

st.title("🐧 Linux Bash Challenge")

if "nivel" not in st.session_state:
    st.session_state.nivel = 1

st.write(f"Nivel actual: {st.session_state.nivel}")

# MISIÓN 1
if st.session_state.nivel == 1:

    st.header("🏝️ Misión 1")

    st.code("""
#!/bin/bash

_______="Linux"

echo $curso
""", language="bash")

    respuesta = st.text_input(
        "¿Qué palabra falta?"
    )

    if st.button("Validar Misión 1"):

        if respuesta.lower().strip() == "curso":

            st.success("✅ Correcto")

            st.session_state.nivel = 2

            st.rerun()

        else:

            st.error("❌ Incorrecto")

# MISIÓN 2
elif st.session_state.nivel == 2:

    st.header("🏕️ Misión 2")

    st.code("""
#!/bin/bash

echo "___________"
""", language="bash")

    respuesta = st.text_input(
        "Complete el mensaje"
    )

    if st.button("Validar Misión 2"):

        if respuesta.strip() == "Bienvenido a Linux":

            st.success("🎉 Pasaste la misión 2")

        else:

            st.error("❌ Incorrecto")
