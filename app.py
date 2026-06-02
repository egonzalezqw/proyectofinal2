import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Linux Challenge",
    page_icon="🐧"
)

# Variables de sesión
if "nivel" not in st.session_state:
    st.session_state.nivel = 1

# Título
st.title("🐧 Linux Survival Challenge")

# Mostrar nivel actual
st.write(f"Nivel actual: {st.session_state.nivel}")

# Nivel 1
if st.session_state.nivel == 1:

    st.header("Misión 1")

    st.write("""
    Cree un script llamado bienvenida.sh que muestre:

    Bienvenido al Linux Challenge
    """)

    respuesta = st.text_input(
        "¿Qué mostró el script?"
    )

    if st.button("Validar"):

        if respuesta == "Bienvenido al Linux Challenge":

            st.success("Correcto")

            st.session_state.nivel = 2

            st.rerun()

        else:

            st.error("Respuesta incorrecta")

# Nivel 2
elif st.session_state.nivel == 2:

    st.header("Misión 2")

    st.write("""
    Cree un script que utilice una variable llamada nombre
    y la muestre utilizando echo.
    """)

    respuesta = st.text_input(
        "¿Qué valor mostró?"
    )

    if st.button("Validar Nivel 2"):

        if respuesta.strip() != "":

            st.success("¡Proyecto completado!")

            st.balloons()

        else:

            st.error("Ingrese una respuesta")
