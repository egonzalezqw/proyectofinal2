# app.py

import streamlit as st

st.set_page_config(
page_title="🏝️ Isla Linux Essentials",
page_icon="🏝️",
layout="wide"
)

# ----------------------------

# ESTADOS

# ----------------------------

retos = [
"playa",
"variables",
"ifelse",
"forloop",
"whileloop",
"permisos",
"usuarios",
"errores"
]

for reto in retos:
if reto not in st.session_state:
st.session_state[reto] = False

if "letras" not in st.session_state:
st.session_state.letras = []

# ----------------------------

# FUNCION

# ----------------------------

def agregar_letra(letra):
if letra not in st.session_state.letras:
st.session_state.letras.append(letra)

# ----------------------------

# TITULO

# ----------------------------

st.title("🏝️ La Isla Perdida de Linux")

st.markdown("""
Un antiguo administrador escondió un tesoro en esta isla.

Para encontrarlo deberás resolver retos relacionados con Bash y Linux.

Cada reto correcto te entregará una letra.

Cuando completes todos los desafíos podrás abrir el cofre.
""")

# ----------------------------

# INVENTARIO

# ----------------------------

st.sidebar.title("🎒 Inventario")

if st.session_state.letras:
for letra in st.session_state.letras:
st.sidebar.success(f"Letra obtenida: {letra}")
else:
st.sidebar.info("Aún no tienes letras")

# ==================================================

# RETO 1

# ==================================================

st.header("🌴 Playa del Bash")

if not st.session_state.playa:

```
st.code("""
```

#!/bin/bash

nombre="Cisco"

echo $nombre
""", language="bash")

```
r = st.text_input(
    "¿Qué mostrará el script?",
    key="playa_input"
)

if st.button("Validar Playa"):

    if r.strip().lower() == "cisco":
        st.success("¡Correcto!")
        st.session_state.playa = True
        agregar_letra("L")
        st.rerun()
    else:
        st.error("Respuesta incorrecta")
```

else:
st.success("Completado ✅")

# ==================================================

# RETO 2

# ==================================================

if st.session_state.playa:

```
st.header("🏕️ Campamento de Variables")

if not st.session_state.variables:

    st.code("""
```

#!/bin/bash

______="Linux"

echo $curso
""", language="bash")

```
    r = st.text_input(
        "¿Qué palabra falta?",
        key="variables_input"
    )

    if st.button("Validar Variables"):

        if r.strip().lower() == "curso":
            st.success("Correcto")
            st.session_state.variables = True
            agregar_letra("I")
            st.rerun()
        else:
            st.error("Incorrecto")

else:
    st.success("Completado ✅")
```

# ==================================================

# RETO 3

# ==================================================

if st.session_state.variables:

```
st.header("🌋 Volcán del IF")

if not st.session_state.ifelse:

    st.code("""
```

edad=20

if [ $edad -gt 18 ]
then
echo "Mayor"
else
echo "Menor"
fi
""", language="bash")

```
    r = st.text_input(
        "¿Cuál será la salida?",
        key="if_input"
    )

    if st.button("Validar IF"):

        if r.strip().lower() == "mayor":
            st.success("Excelente")
            st.session_state.ifelse = True
            agregar_letra("N")
            st.rerun()
        else:
            st.error("Incorrecto")

else:
    st.success("Completado ✅")
```

# ==================================================

# RETO 4

# ==================================================

if st.session_state.ifelse:

```
st.header("🏰 Fortaleza FOR")

if not st.session_state.forloop:

    st.code("""
```

for i in 1 2 3
do
echo $i
done
""", language="bash")

```
    r = st.text_input(
        "¿Cuál es el último valor mostrado?",
        key="for_input"
    )

    if st.button("Validar FOR"):

        if r.strip() == "3":
            st.success("Correcto")
            st.session_state.forloop = True
            agregar_letra("U")
            st.rerun()
        else:
            st.error("Incorrecto")

else:
    st.success("Completado ✅")
```

# ==================================================

# RETO 5

# ==================================================

if st.session_state.forloop:

```
st.header("🌊 Lago WHILE")

if not st.session_state.whileloop:

    st.code("""
```

contador=1

while [ $contador -le 3 ]
do
echo $contador
contador=$((contador+1))
done
""", language="bash")

```
    r = st.text_input(
        "¿Cuántas veces se ejecuta el ciclo?",
        key="while_input"
    )

    if st.button("Validar WHILE"):

        if r.strip() == "3":
            st.success("Correcto")
            st.session_state.whileloop = True
            agregar_letra("X")
            st.rerun()
        else:
            st.error("Incorrecto")

else:
    st.success("Completado ✅")
```

# ==================================================

# RETO 6

# ==================================================

if st.session_state.whileloop:

```
st.header("⛰️ Montaña de Permisos")

if not st.session_state.permisos:

    st.code("chmod 755 respaldo.sh", language="bash")

    r = st.text_input(
        "¿Qué permisos obtiene el propietario?",
        key="permisos_input"
    )

    if st.button("Validar Permisos"):

        if r.strip().lower() == "rwx":
            st.success("Correcto")
            st.session_state.permisos = True
            st.rerun()
        else:
            st.error("Incorrecto")

else:
    st.success("Completado ✅")
```

# ==================================================

# RETO 7

# ==================================================

if st.session_state.permisos:

```
st.header("👤 Aldea de Usuarios")

if not st.session_state.usuarios:

    r = st.text_input(
        "¿Qué comando crea un usuario llamado juan?",
        key="usuarios_input"
    )

    if st.button("Validar Usuario"):

        if r.strip().lower() == "useradd juan":
            st.success("Correcto")
            st.session_state.usuarios = True
            st.rerun()
        else:
            st.error("Incorrecto")

else:
    st.success("Completado ✅")
```

# ==================================================

# RETO 8

# ==================================================

if st.session_state.usuarios:

```
st.header("💀 Cueva de Errores")

if not st.session_state.errores:

    st.code("""
```

for i in 1 2 3
echo $i
done
""", language="bash")

```
    r = st.text_input(
        "¿Qué palabra falta?",
        key="errores_input"
    )

    if st.button("Validar Error"):

        if r.strip().lower() == "do":
            st.success("Correcto")
            st.session_state.errores = True
            st.rerun()
        else:
            st.error("Incorrecto")

else:
    st.success("Completado ✅")
```

# ==================================================

# TESORO

# ==================================================

if all(st.session_state[r] for r in retos):

```
st.divider()

st.header("💎 Cofre del Tesoro")

st.info(
    "Utiliza las letras obtenidas para descubrir la palabra secreta."
)

clave = st.text_input(
    "Palabra secreta:"
)

if st.button("Abrir Cofre"):

    if clave.strip().upper() == "LINUX":

        st.balloons()

        st.success(
            "🏆 FELICIDADES - Has conquistado la Isla Linux."
        )

        st.markdown("""
```

### Has demostrado conocimientos de:

✅ Variables

✅ IF / ELSE

✅ FOR

✅ WHILE

✅ Permisos

✅ Usuarios

✅ Bash Scripting
""")

```
    else:
        st.error("La palabra es incorrecta.")
```
