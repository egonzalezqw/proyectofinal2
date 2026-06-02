import streamlit as st
from datetime import datetime

# ==================================================

# CONFIGURACIÓN

# ==================================================

st.set_page_config(
page_title="🏝️ Linux Escape Island",
page_icon="🐧",
layout="wide"
)

# ==================================================

# SESSION STATE

# ==================================================

if "nombre" not in st.session_state:
st.session_state.nombre = ""

if "nivel" not in st.session_state:
st.session_state.nivel = 1

if "vidas" not in st.session_state:
st.session_state.vidas = 3

if "coins" not in st.session_state:
st.session_state.coins = 0

if "logros" not in st.session_state:
st.session_state.logros = []

if "boss_hp" not in st.session_state:
st.session_state.boss_hp = 100

if "inicio" not in st.session_state:
st.session_state.inicio = datetime.now()

# ==================================================

# FUNCIONES

# ==================================================

def ganar_nivel():
st.session_state.nivel += 1
st.session_state.coins += 100

def perder_vida():
st.session_state.vidas -= 1

def agregar_logro(logro):
if logro not in st.session_state.logros:
st.session_state.logros.append(logro)

# ==================================================

# LOGIN

# ==================================================

st.title("🏝️ Linux Escape Island")

if st.session_state.nombre == "":
nombre = st.text_input("👤 Ingresa tu nombre")

```
if st.button("Comenzar Aventura"):

    if nombre.strip():
        st.session_state.nombre = nombre
        st.rerun()

st.stop()
```

# ==================================================

# SIDEBAR

# ==================================================

st.sidebar.title("🎮 Estado")

st.sidebar.success(
f"👤 {st.session_state.nombre}"
)

st.sidebar.metric(
"❤️ Vidas",
st.session_state.vidas
)

st.sidebar.metric(
"🪙 Linux Coins",
st.session_state.coins
)

st.sidebar.metric(
"📍 Nivel",
st.session_state.nivel
)

st.sidebar.progress(
min(st.session_state.nivel / 6, 1.0)
)

tiempo = datetime.now() - st.session_state.inicio

st.sidebar.write(
f"⏱️ Tiempo: {tiempo.seconds // 60} min"
)

st.sidebar.subheader("🏆 Logros")

if st.session_state.logros:
for logro in st.session_state.logros:
st.sidebar.write(logro)

# ==================================================

# GAME OVER

# ==================================================

if st.session_state.vidas <= 0:

```
st.error("💀 GAME OVER")

if st.button("Reiniciar"):

    for key in list(st.session_state.keys()):
        del st.session_state[key]

    st.rerun()

st.stop()
```

# ==================================================

# HISTORIA

# ==================================================

st.info("""
Hace muchos años un Administrador Linux desapareció.

Antes de desaparecer ocultó un tesoro digital.

Para encontrarlo deberás superar desafíos Linux.
""")

# ==================================================

# NIVEL 1

# ==================================================

if st.session_state.nivel == 1:

```
st.header("🌴 Playa Oculta")

st.markdown("""
Encuentra el comando que muestra el directorio actual.
""")

respuesta = st.text_input("Respuesta")

with st.expander("💡 Pista"):
    st.write("No cambia directorios, solamente muestra dónde estás.")

if st.button("Validar"):

    if respuesta.lower().strip() == "pwd":

        st.success("✅ Correcto")

        agregar_logro("🌴 Explorador Linux")

        ganar_nivel()

        st.rerun()

    else:

        perder_vida()

        st.error("❌ Incorrecto")
```

# ==================================================

# NIVEL 2

# ==================================================

elif st.session_state.nivel == 2:

```
st.header("🔐 Bosque de Permisos")

st.code(
    "chmod 755 respaldo.sh",
    language="bash"
)

respuesta = st.text_input(
    "¿Qué permisos tiene el propietario?"
)

with st.expander("💡 Pista"):
    st.write("755 = rwx r-x r-x")

if st.button("Validar"):

    if respuesta.lower().strip() == "rwx":

        st.success("Correcto")

        agregar_logro("🔐 Maestro de Permisos")

        ganar_nivel()

        st.rerun()

    else:

        perder_vida()

        st.error("Incorrecto")
```

# ==================================================

# NIVEL 3

# ==================================================

elif st.session_state.nivel == 3:

```
st.header("👤 Aldea de Usuarios")

respuesta = st.text_input(
    "Comando para crear el usuario juan"
)

with st.expander("💡 Pista"):
    st.write("Empieza por user...")

if st.button("Validar"):

    if respuesta.lower().strip() == "useradd juan":

        st.success("Correcto")

        agregar_logro("👤 Administrador de Usuarios")

        ganar_nivel()

        st.rerun()

    else:

        perder_vida()

        st.error("Incorrecto")
```

# ==================================================

# NIVEL 4

# ==================================================

elif st.session_state.nivel == 4:

```
st.header("📜 Templo Bash")

st.code("""
```

for i in 1 2 3
do
echo $i
done
""", language="bash")

```
respuesta = st.text_input(
    "Último valor mostrado"
)

if st.button("Validar"):

    if respuesta.strip() == "3":

        st.success("Correcto")

        agregar_logro("📜 Guerrero Bash")

        ganar_nivel()

        st.rerun()

    else:

        perder_vida()

        st.error("Incorrecto")
```

# ==================================================

# NIVEL 5

# ==================================================

elif st.session_state.nivel == 5:

```
st.header("🌋 Jefe Final Linux")

st.progress(
    st.session_state.boss_hp / 100
)

st.write(
    f"❤️ Vida del Guardián: {st.session_state.boss_hp}"
)

respuesta = st.text_input(
    "¿Qué comando lista archivos?"
)

if st.button("Atacar"):

    if respuesta.lower().strip() == "ls":

        st.session_state.boss_hp -= 25

        st.success("⚔️ Ataque exitoso")

    else:

        perder_vida()

        st.error("Fallaste")

    if st.session_state.boss_hp <= 0:

        agregar_logro("🐧 Vencedor del Guardián Linux")

        ganar_nivel()

        st.rerun()
```

# ==================================================

# TESORO FINAL

# ==================================================

elif st.session_state.nivel >= 6:

```
st.balloons()

st.success(
    "💎 ¡HAS ENCONTRADO EL TESORO LINUX!"
)

st.markdown("""
```

# 🏆 Misión Completada

Has demostrado conocimientos de:

* Bash
* Usuarios
* Permisos
* Bucles
* Comandos Linux
* Administración básica
  """)
