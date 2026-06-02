import streamlit as st

st.set_page_config(
page_title="🏝️ Linux Survival Challenge",
page_icon="🐧"
)

# ----------------------------

# ESTADO

# ----------------------------

if "nivel" not in st.session_state:
st.session_state.nivel = 1

if "nombre" not in st.session_state:
st.session_state.nombre = ""

# ----------------------------

# LOGIN

# ----------------------------

st.title("🏝️ Linux Survival Challenge")

if st.session_state.nombre == "":

```
nombre = st.text_input(
    "Ingrese su nombre:"
)

if st.button("Comenzar"):

    if nombre.strip():
        st.session_state.nombre = nombre
        st.rerun()

st.stop()
```

st.success(
f"Bienvenido {st.session_state.nombre}"
)

st.progress(st.session_state.nivel / 6)

# ----------------------------

# NIVEL 1

# ----------------------------

if st.session_state.nivel == 1:

```
st.header("🌴 Misión 1 - Primer Script")

st.markdown("""
Cree un archivo llamado:

bienvenida.sh

El script debe mostrar:

Bienvenido al Linux Challenge

Ejecútelo y escriba el resultado.
""")

respuesta = st.text_input(
    "Resultado:"
)

if st.button("Validar Misión 1"):

    if respuesta == "Bienvenido al Linux Challenge":

        st.success("Nivel completado")

        st.session_state.nivel = 2
        st.rerun()

    else:
        st.error("Incorrecto")
```

# ----------------------------

# NIVEL 2

# ----------------------------

elif st.session_state.nivel == 2:

```
st.header("🏕️ Misión 2 - Variables")

st.markdown("""
Cree un script llamado:

usuario.sh

Debe contener una variable
llamada nombre.

Luego mostrarla utilizando echo.
""")

respuesta = st.text_input(
    "¿Qué valor mostró?"
)

if st.button("Validar Misión 2"):

    if respuesta.strip() != "":

        st.success("Nivel completado")

        st.session_state.nivel = 3
        st.rerun()
```

# ----------------------------

# NIVEL 3

# ----------------------------

elif st.session_state.nivel == 3:

```
st.header("⛰️ Misión 3 - Permisos")

st.markdown("""
Asigne permisos de ejecución
al script bienvenida.sh

Utilice chmod.
""")

respuesta = st.text_input(
    "¿Qué permisos tiene el propietario?"
)

if st.button("Validar Misión 3"):

    if respuesta.lower() == "rwx":

        st.success("Correcto")

        st.session_state.nivel = 4
        st.rerun()
```

# ----------------------------

# NIVEL 4

# ----------------------------

elif st.session_state.nivel == 4:

```
st.header("🌋 Misión 4 - IF")

st.markdown("""
Cree un script:

edad.sh

edad=20

Si edad es mayor a 18
debe mostrar:

Mayor
""")

respuesta = st.text_input(
    "¿Qué mostró el script?"
)

if st.button("Validar Misión 4"):

    if respuesta.lower() == "mayor":

        st.success("Correcto")

        st.session_state.nivel = 5
        st.rerun()
```

# ----------------------------

# NIVEL 5

# ----------------------------

elif st.session_state.nivel == 5:

```
st.header("🏰 Misión 5 - FOR")

st.markdown("""
Cree un script utilizando:

for

Debe mostrar:

1
2
3
""")

respuesta = st.text_input(
    "¿Cuál fue el último valor?"
)

if st.button("Validar Misión 5"):

    if respuesta == "3":

        st.success("Correcto")

        st.session_state.nivel = 6
        st.rerun()
```

# ----------------------------

# TESORO FINAL

# ----------------------------

elif st.session_state.nivel == 6:

```
st.balloons()

st.success(
    "🏆 Proyecto Final Completado"
)

st.markdown("""
Has demostrado conocimientos de:

- Bash
- Variables
- Permisos
- IF
- FOR
- Ejecución de scripts
""")
```
