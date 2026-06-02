import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="🏝️ La Isla del Administrador Perdido",
    page_icon="🏝️",
    layout="wide"
)

# Inicializar estados
if "playa" not in st.session_state:
    st.session_state.playa = False

if "usuarios" not in st.session_state:
    st.session_state.usuarios = False

if "permisos" not in st.session_state:
    st.session_state.permisos = False

if "procesos" not in st.session_state:
    st.session_state.procesos = False

if "scripts" not in st.session_state:
    st.session_state.scripts = False

if "inventario" not in st.session_state:
    st.session_state.inventario = []

# Título
st.title("🏝️ La Isla del Administrador Perdido")
st.markdown("""
Bienvenido aventurero.

Un antiguo administrador Linux escondió un tesoro en esta isla.
Debes superar cada reto para encontrarlo.

Cada desafío te otorgará una llave.
""")

# Sidebar
st.sidebar.title("🎒 Inventario")

for item in st.session_state.inventario:
    st.sidebar.success(item)

st.sidebar.divider()

st.sidebar.markdown("### Estado de la misión")

st.sidebar.write("🌴 Playa:", "✅" if st.session_state.playa else "❌")
st.sidebar.write("🏕️ Usuarios:", "✅" if st.session_state.usuarios else "❌")
st.sidebar.write("⛰️ Permisos:", "✅" if st.session_state.permisos else "❌")
st.sidebar.write("🌋 Procesos:", "✅" if st.session_state.procesos else "❌")
st.sidebar.write("🏰 Scripts:", "✅" if st.session_state.scripts else "❌")

# ------------------------------------
# RETO 1
# ------------------------------------

st.header("🌴 Reto 1 - Playa del Bash")

if not st.session_state.playa:

    respuesta = st.radio(
        "¿Cuál comando muestra el directorio actual?",
        ["ls", "pwd", "cd", "cat"],
        key="r1"
    )

    if st.button("Validar Reto 1"):

        if respuesta == "pwd":
            st.success("¡Correcto!")
            st.session_state.playa = True

            if "Llave de la Playa" not in st.session_state.inventario:
                st.session_state.inventario.append("🔑 Llave de la Playa")

            st.rerun()

        else:
            st.error("Respuesta incorrecta")

else:
    st.success("Reto completado")

# ------------------------------------
# RETO 2
# ------------------------------------

if st.session_state.playa:

    st.header("🏕️ Reto 2 - Campamento de Usuarios")

    if not st.session_state.usuarios:

        st.code("useradd juan", language="bash")

        respuesta2 = st.radio(
            "¿Qué hace este comando?",
            [
                "Elimina usuario",
                "Crea usuario",
                "Cambia contraseña",
                "Muestra usuarios"
            ],
            key="r2"
        )

        if st.button("Validar Reto 2"):

            if respuesta2 == "Crea usuario":

                st.success("¡Correcto!")

                st.session_state.usuarios = True

                if "👤 Llave de Usuarios" not in st.session_state.inventario:
                    st.session_state.inventario.append("👤 Llave de Usuarios")

                st.rerun()

            else:
                st.error("Respuesta incorrecta")

    else:
        st.success("Reto completado")

# ------------------------------------
# RETO 3
# ------------------------------------

if st.session_state.usuarios:

    st.header("⛰️ Reto 3 - Montaña de Permisos")

    if not st.session_state.permisos:

        st.code("chmod 755 archivo.sh", language="bash")

        respuesta3 = st.text_input(
            "¿Qué permisos tiene el propietario?"
        )

        if st.button("Validar Reto 3"):

            if respuesta3.lower().strip() == "rwx":

                st.success("¡Excelente!")

                st.session_state.permisos = True

                if "🛡️ Llave de Permisos" not in st.session_state.inventario:
                    st.session_state.inventario.append("🛡️ Llave de Permisos")

                st.rerun()

            else:
                st.error("Respuesta incorrecta")

    else:
        st.success("Reto completado")

# ------------------------------------
# RETO 4
# ------------------------------------

if st.session_state.permisos:

    st.header("🌋 Reto 4 - Volcán de Procesos")

    if not st.session_state.procesos:

        respuesta4 = st.radio(
            "¿Cuál comando muestra procesos activos?",
            ["mkdir", "cp", "top", "rm"],
            key="r4"
        )

        if st.button("Validar Reto 4"):

            if respuesta4 == "top":

                st.success("¡Correcto!")

                st.session_state.procesos = True

                if "🔥 Llave del Volcán" not in st.session_state.inventario:
                    st.session_state.inventario.append("🔥 Llave del Volcán")

                st.rerun()

            else:
                st.error("Respuesta incorrecta")

    else:
        st.success("Reto completado")

# ------------------------------------
# RETO 5
# ------------------------------------

if st.session_state.procesos:

    st.header("🏰 Reto 5 - Fortaleza de Scripts")

    if not st.session_state.scripts:

        st.code("""
#!/bin/bash

for i in 1 2 3
do
    echo $i
done
""", language="bash")

        respuesta5 = st.text_input(
            "¿Cuál es el último número que mostrará el script?"
        )

        if st.button("Validar Reto 5"):

            if respuesta5.strip() == "3":

                st.success("¡Perfecto!")

                st.session_state.scripts = True

                if "🏆 Llave Maestra" not in st.session_state.inventario:
                    st.session_state.inventario.append("🏆 Llave Maestra")

                st.rerun()

            else:
                st.error("Respuesta incorrecta")

    else:
        st.success("Reto completado")

# ------------------------------------
# TESORO FINAL
# ------------------------------------

if (
    st.session_state.playa
    and st.session_state.usuarios
    and st.session_state.permisos
    and st.session_state.procesos
    and st.session_state.scripts
):

    st.divider()

    st.header("💎 Tesoro Final")

    palabra = st.text_input(
        "Une todas las llaves y escribe la palabra secreta:"
    )

    st.info("Pista: El sistema operativo estudiado en Cisco.")

    if st.button("Abrir Cofre"):

        if palabra.upper() == "LINUX":

            st.balloons()

            st.success(
                "🎉 ¡FELICIDADES! Has encontrado el Tesoro Linux."
            )

            st.markdown("""
# 🏆 Misión Completada

Has demostrado tus conocimientos de:

- Bash
- Usuarios
- Permisos
- Procesos
- Scripting

Ahora eres un verdadero explorador Linux.
""")

        else:
            st.error("La palabra secreta es incorrecta.")
