import streamlit as st

# ==========================================
# CONFIGURACIÓN
# ==========================================

st.set_page_config(
    page_title="🏝️ Linux Survival Challenge",
    page_icon="🐧",
    layout="wide"
)

# ==========================================
# DATOS DE LAS MISIONES
# ==========================================

MISIONES = [
    {
        "titulo": "🌴 Misión 1 - Primer Script",
        "descripcion": """
Cree un archivo llamado:

bienvenida.sh

Contenido:

#!/bin/bash
echo "TOKEN-101"

Ejecute el script y obtenga el token.
""",
        "token": "TOKEN-101"
    },
    {
        "titulo": "🏕️ Misión 2 - Variables",
        "descripcion": """
Cree un script llamado variables.sh

#!/bin/bash

curso="Linux"

echo "TOKEN-102"

Ejecute el script.
""",
        "token": "TOKEN-102"
    },
    {
        "titulo": "📢 Misión 3 - Echo",
        "descripcion": """
Cree un script llamado usuario.sh

#!/bin/bash

nombre="Cisco"

echo $nombre
echo "TOKEN-103"

Ejecute el script.
""",
        "token": "TOKEN-103"
    },
    {
        "titulo": "🔐 Misión 4 - Permisos",
        "descripcion": """
Cree un script llamado permisos.sh

#!/bin/bash

echo "TOKEN-104"

Asigne permisos de ejecución:

chmod +x permisos.sh

Luego ejecútelo.
""",
        "token": "TOKEN-104"
    },
    {
        "titulo": "📁 Misión 5 - Directorios",
        "descripcion": """
Cree un directorio llamado:

laboratorio

Ingrese al directorio y ejecute:

echo TOKEN-105 > secreto.txt

Visualice el contenido.
""",
        "token": "TOKEN-105"
    },
    {
        "titulo": "🔍 Misión 6 - Find",
        "descripcion": """
Busque el archivo:

secreto.txt

Utilice:

find

Obtenga el token almacenado.
""",
        "token": "TOKEN-106"
    },
    {
        "titulo": "👤 Misión 7 - Usuarios",
        "descripcion": """
Cree un usuario:

sudo useradd estudiante

Luego ejecute:

echo TOKEN-107
""",
        "token": "TOKEN-107"
    },
    {
        "titulo": "🔁 Misión 8 - FOR",
        "descripcion": """
Complete y ejecute:

#!/bin/bash

for i in 1 2 3
do
   echo $i
done

echo TOKEN-108
""",
        "token": "TOKEN-108"
    },
    {
        "titulo": "🔄 Misión 9 - WHILE",
        "descripcion": """
Complete y ejecute:

#!/bin/bash

contador=1

while [ $contador -le 3 ]
do
    echo $contador
    contador=$((contador+1))
done

echo TOKEN-109
""",
        "token": "TOKEN-109"
    },
    {
        "titulo": "🌋 Misión 10 - IF",
        "descripcion": """
Complete y ejecute:

#!/bin/bash

edad=20

if [ $edad -gt 18 ]
then
   echo "Mayor"
fi

echo TOKEN-110
""",
        "token": "TOKEN-110"
    },
    {
        "titulo": "📦 Misión 11 - Compresión",
        "descripcion": """
Comprima el directorio laboratorio:

tar -cvf respaldo.tar laboratorio

Luego ejecute:

echo TOKEN-111
""",
        "token": "TOKEN-111"
    },
    {
        "titulo": "📜 Misión 12 - Grep",
        "descripcion": """
Cree un archivo:

echo TOKEN-112 > sistema.log

Busque el token utilizando:

grep TOKEN sistema.log
""",
        "token": "TOKEN-112"
    },
    {
        "titulo": "🏆 Misión Final",
        "descripcion": """
Cree un script llamado final.sh

#!/bin/bash

echo TOKEN-LINUX-MASTER

Ejecute el script.
""",
        "token": "TOKEN-LINUX-MASTER"
    }
]

# ==========================================
# SESSION STATE
# ==========================================

if "nivel" not in st.session_state:
    st.session_state.nivel = 0

if "nombre" not in st.session_state:
    st.session_state.nombre = ""

# ==========================================
# LOGIN
# ==========================================

st.title("🏝️ Linux Survival Challenge")

if st.session_state.nombre == "":

    nombre = st.text_input(
        "👤 Ingrese su nombre"
    )

    if st.button("Comenzar"):

        if nombre.strip():
            st.session_state.nombre = nombre
            st.rerun()

    st.stop()

# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.success(
    f"👤 {st.session_state.nombre}"
)

st.sidebar.metric(
    "🎯 Misiones completadas",
    st.session_state.nivel
)

st.sidebar.progress(
    st.session_state.nivel / len(MISIONES)
)

# ==========================================
# JUEGO
# ==========================================

if st.session_state.nivel < len(MISIONES):

    mision = MISIONES[st.session_state.nivel]

    st.header(mision["titulo"])

    st.info(mision["descripcion"])

    token = st.text_input(
        "🔑 Ingrese el token obtenido:"
    )

    if st.button("Validar Token"):

        if token.strip() == mision["token"]:

            st.success(
                "✅ Misión completada"
            )

            st.session_state.nivel += 1

            st.rerun()

        else:

            st.error(
                "❌ Token incorrecto"
            )

# ==========================================
# FINAL
# ==========================================

else:

    st.balloons()

    st.success(
        "🏆 ¡FELICIDADES!"
    )

    st.markdown(f"""
### {st.session_state.nombre}

Has completado exitosamente el:

# 🐧 Linux Survival Challenge

Competencias demostradas:

✅ Scripts Bash  
✅ Variables  
✅ Permisos  
✅ Directorios  
✅ Usuarios  
✅ Find  
✅ Grep  
✅ IF  
✅ FOR  
✅ WHILE  
✅ Compresión de archivos

🎖️ Proyecto Final Aprobado
""")

    if st.button("Reiniciar Juego"):

        st.session_state.nivel = 0
        st.rerun()
