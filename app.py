import streamlit as st
from datetime import datetime

# =====================================================
# CONFIGURACIÓN
# =====================================================

st.set_page_config(
    page_title="🐧 Linux Escape Room",
    page_icon="🐧",
    layout="wide"
)

# =====================================================
# SESSION STATE
# =====================================================

if "nombre" not in st.session_state:
    st.session_state["nombre"] = ""

if "nivel" not in st.session_state:
    st.session_state["nivel"] = 1

if "vidas" not in st.session_state:
    st.session_state["vidas"] = 3

if "coins" not in st.session_state:
    st.session_state["coins"] = 0

if "inicio" not in st.session_state:
    st.session_state["inicio"] = datetime.now()

# =====================================================
# FUNCIONES
# =====================================================

def nivel_completado():
    st.session_state["nivel"] += 1
    st.session_state["coins"] += 100

def perder_vida():
    st.session_state["vidas"] -= 1

# =====================================================
# LOGIN
# =====================================================

st.title("🏝️ Linux Escape Room")

if st.session_state["nombre"] == "":

    nombre = st.text_input(
        "👤 Ingrese su nombre"
    )

    if st.button("Comenzar"):

        if nombre.strip():
            st.session_state["nombre"] = nombre
            st.rerun()

    st.stop()

# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.header("🎮 Estado")

st.sidebar.write(
    f"👤 {st.session_state['nombre']}"
)

st.sidebar.metric(
    "❤️ Vidas",
    st.session_state["vidas"]
)

st.sidebar.metric(
    "🪙 Linux Coins",
    st.session_state["coins"]
)

st.sidebar.metric(
    "📍 Nivel",
    st.session_state["nivel"]
)

st.sidebar.progress(
    min(st.session_state["nivel"] / 6, 1.0)
)

tiempo = datetime.now() - st.session_state["inicio"]

st.sidebar.write(
    f"⏱️ Tiempo: {tiempo.seconds // 60} min"
)

# =====================================================
# GAME OVER
# =====================================================

if st.session_state["vidas"] <= 0:

    st.error("💀 GAME OVER")

    if st.button("Reiniciar Juego"):

        for key in list(st.session_state.keys()):
            del st.session_state[key]

        st.rerun()

    st.stop()

# =====================================================
# HISTORIA
# =====================================================

st.info("""
Un antiguo administrador Linux escondió un tesoro digital.

Supera los retos para encontrarlo.
""")

# =====================================================
# NIVEL 1
# =====================================================

if st.session_state["nivel"] == 1:

    st.header("🌴 Nivel 1 - Navegación")

    st.write(
        "¿Qué comando muestra el directorio actual?"
    )

    respuesta = st.text_input(
        "Respuesta"
    )

    if st.button("Validar Nivel 1"):

        if respuesta.strip().lower() == "pwd":

            st.success("✅ Correcto")

            nivel_completado()

            st.rerun()

        else:

            perder_vida()

            st.error("❌ Incorrecto")

# =====================================================
# NIVEL 2
# =====================================================

elif st.session_state["nivel"] == 2:

    st.header("🔐 Nivel 2 - Permisos")

    st.code(
        "chmod 755 archivo.sh",
        language="bash"
    )

    respuesta = st.text_input(
        "¿Qué permisos tiene el propietario?"
    )

    if st.button("Validar Nivel 2"):

        if respuesta.strip().lower() == "rwx":

            st.success("✅ Correcto")

            nivel_completado()

            st.rerun()

        else:

            perder_vida()

            st.error("❌ Incorrecto")

# =====================================================
# NIVEL 3
# =====================================================

elif st.session_state["nivel"] == 3:

    st.header("👤 Nivel 3 - Usuarios")

    respuesta = st.text_input(
        "Comando para crear el usuario juan"
    )

    if st.button("Validar Nivel 3"):

        if respuesta.strip().lower() == "useradd juan":

            st.success("✅ Correcto")

            nivel_completado()

            st.rerun()

        else:

            perder_vida()

            st.error("❌ Incorrecto")

# =====================================================
# NIVEL 4
# =====================================================

elif st.session_state["nivel"] == 4:

    st.header("📜 Nivel 4 - Bash")

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

    if st.button("Validar Nivel 4"):

        if respuesta.strip() == "3":

            st.success("✅ Correcto")

            nivel_completado()

            st.rerun()

        else:

            perder_vida()

            st.error("❌ Incorrecto")

# =====================================================
# NIVEL 5
# =====================================================

elif st.session_state["nivel"] == 5:

    st.header("🤖 Nivel 5 - Script Bash")

    st.code(
        """
#!/bin/bash
echo "Linux Master"
""",
        language="bash"
    )

    respuesta = st.text_input(
        "¿Qué mostrará el script?"
    )

    if st.button("Validar Nivel 5"):

        if respuesta.strip() == "Linux Master":

            st.success("✅ Correcto")

            nivel_completado()

            st.rerun()

        else:

            perder_vida()

            st.error("❌ Incorrecto")

# =====================================================
# FINAL
# =====================================================

elif st.session_state["nivel"] >= 6:

    st.balloons()

    st.success(
        "🏆 ¡FELICIDADES! Has completado Linux Escape Room"
    )

    st.write(
        f"Jugador: {st.session_state['nombre']}"
    )

    st.write(
        f"Monedas obtenidas: {st.session_state['coins']}"
    )

    st.write(
        f"Vidas restantes: {st.session_state['vidas']}"
    )
