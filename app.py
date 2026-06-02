import streamlit as st

# ==========================================
# CONFIGURACIÓN
# ==========================================

st.set_page_config(
    page_title="🏝️ Isla Linux Essentials",
    page_icon="🏝️",
    layout="wide"
)

# ==========================================
# ESTADOS
# ==========================================

RETOS = [
    "playa",
    "variables",
    "ifelse",
    "forloop",
    "permisos"
]

for reto in RETOS:
    if reto not in st.session_state:
        st.session_state[reto] = False

if "letras" not in st.session_state:
    st.session_state.letras = []

# ==========================================
# FUNCIONES
# ==========================================

def agregar_letra(letra):
    if letra not in st.session_state.letras:
        st.session_state.letras.append(letra)

def progreso():
    completados = sum(
        st.session_state[r] for r in RETOS
    )
    return completados / len(RETOS)

# ==========================================
# ENCABEZADO
# ==========================================

st.title("🏝️ La Isla Perdida de Linux")

st.markdown("""
Un antiguo administrador Linux escondió un tesoro en esta isla.

Para encontrarlo deberás resolver pequeños desafíos de Bash.

Cada reto te entregará una letra.

Cuando tengas todas las letras podrás abrir el cofre final.
""")

# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.title("🎒 Inventario")

if st.session_state.letras:
    for letra in st.session_state.letras:
        st.sidebar.success(f"Letra: {letra}")
else:
    st.sidebar.info("Todavía no has encontrado letras.")

st.sidebar.divider()

st.sidebar.subheader("📊 Progreso")

st.sidebar.progress(progreso())

# ==========================================
# RETO 1
# ==========================================

st.header("🌴 Playa del Bash")

if not st.session_state.playa:

    st.code(
        """
#!/bin/bash

nombre="Cisco"

echo $nombre
""",
        language="bash"
    )

    respuesta = st.text_input(
        "¿Qué mostrará el script?"
    )

    if st.button("Validar Reto 1"):

        if respuesta.strip().lower() == "cisco":

            st.success("¡Correcto!")

            st.session_state.playa = True
            agregar_letra("L")

            st.rerun()

        else:
            st.error("Respuesta incorrecta")

else:
    st.success("✅ Completado")

# ==========================================
# RETO 2
# ==========================================

if st.session_state.playa:

    st.header("🏕️ Campamento de Variables")

    if not st.session_state.variables:

        st.code(
            """
#!/bin/bash

______="Linux"

echo $curso
""",
            language="bash"
        )

        respuesta = st.text_input(
            "¿Qué palabra falta?"
        )

        if st.button("Validar Reto 2"):

            if respuesta.strip().lower() == "curso":

                st.success("Correcto")

                st.session_state.variables = True
                agregar_letra("I")

                st.rerun()

            else:
                st.error("Respuesta incorrecta")

    else:
        st.success("✅ Completado")

# ==========================================
# RETO 3
# ==========================================

if st.session_state.variables:

    st.header("🌋 Volcán del IF")

    if not st.session_state.ifelse:

        st.code(
            """
edad=20

if [ $edad -gt 18 ]
then
    echo "Mayor"
else
    echo "Menor"
fi
""",
            language="bash"
        )

        respuesta = st.text_input(
            "¿Cuál será la salida?"
        )

        if st.button("Validar Reto 3"):

            if respuesta.strip().lower() == "mayor":

                st.success("Excelente")

                st.session_state.ifelse = True
                agregar_letra("N")

                st.rerun()

            else:
                st.error("Respuesta incorrecta")

    else:
        st.success("✅ Completado")

# ==========================================
# RETO 4
# ==========================================

if st.session_state.ifelse:

    st.header("🏰 Fortaleza FOR")

    if not st.session_state.forloop:

        st.code(
            """
for i in 1 2 3
do
    echo $i
done
""",
            language="bash"
        )

        respuesta = st.text_input(
            "¿Cuál es el último valor mostrado?"
        )

        if st.button("Validar Reto 4"):

            if respuesta.strip() == "3":

                st.success("Correcto")

                st.session_state.forloop = True
                agregar_letra("U")

                st.rerun()

            else:
                st.error("Respuesta incorrecta")

    else:
        st.success("✅ Completado")

# ==========================================
# RETO 5
# ==========================================

if st.session_state.forloop:

    st.header("⛰️ Montaña de Permisos")

    if not st.session_state.permisos:

        st.code(
            "chmod 755 respaldo.sh",
            language="bash"
        )

        respuesta = st.text_input(
            "¿Qué permisos tiene el propietario?"
        )

        if st.button("Validar Reto 5"):

            if respuesta.strip().lower() == "rwx":

                st.success("Correcto")

                st.session_state.permisos = True
                agregar_letra("X")

                st.rerun()

            else:
                st.error("Respuesta incorrecta")

    else:
        st.success("✅ Completado")

# ==========================================
# TESORO FINAL
# ==========================================

if all(st.session_state[r] for r in RETOS):

    st.divider()

    st.header("💎 Tesoro Linux")

    st.info(
        "Utiliza las letras obtenidas para formar la palabra secreta."
    )

    palabra = st.text_input(
        "Palabra secreta"
    )

    if st.button("Abrir Cofre"):

        if palabra.strip().upper() == "LINUX":

            st.balloons()

            st.success(
                "🏆 ¡FELICIDADES! Has encontrado el Tesoro Linux."
            )

        else:
            st.error("Palabra incorrecta.")
