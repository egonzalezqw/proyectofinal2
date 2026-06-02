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

    if respuesta.strip().lower() == "curso":

        st.success("Correcto")

        st.session_state.nivel += 1

        st.rerun()

    else:

        st.error("Incorrecto")
