import streamlit as st

# ---------------------------------

# CONFIGURACIÓN

# ---------------------------------

st.set_page_config(
page_title="Linux Survival Challenge",
page_icon="🐧"
)

# ---------------------------------

# VARIABLES DE SESIÓN

# ---------------------------------

if "nivel" not in st.session_state:
st.session_state["nivel"] = 1

if "nombre" not in st.session_state:
st.session_state["nombre"] = ""

# ---------------------------------

# TÍTULO

# ---------------------------------

st.title("🐧 Linux Survival Challenge")

# ---------------------------------

# LOGIN

# ---------------------------------

if st.session_state["nombre"] == "":

```
nombre = st.text_input(
    "Ingrese su nombre:"
)

if st.button("Comenzar"):

    if nombre.strip() != "":
        st.session_state["nombre"] = nombre
        st.rerun()

st.stop()
```

# ---------------------------------

# BIENVENIDA

# ---------------------------------

st.success(
f"Bienvenido {st.session_state['nombre']}"
)

st.progress(
st.session_state["nivel"] / 5
)

# ---------------------------------

# NIVEL 1

# ---------------------------------

if st.session_state["nivel"] == 1:

```
st.header("Nivel 1 - Script Bash")

st.write("""
Cree un script llamado bienvenida.sh

El script debe mostrar:

Bienvenido al Linux Challenge
""")

respuesta = st.text_input(
    "¿Qué mostró el script?"
)

if st.button("Validar Nivel 1"):

    if respuesta == "Bienvenido al Linux Challenge":

        st.success("Correcto")

        st.session_state["nivel"] = 2

        st.rerun()

    else:

        st.error("Respuesta incorrecta")
```

# ---------------------------------

# NIVEL 2

# ---------------------------------

elif st.session_state["nivel"] == 2:

```
st.header("Nivel 2 - Variables")

st.write("""
Cree un script llamado usuario.sh

Debe crear una variable llamada nombre
y mostrarla con echo.
""")

respuesta = st.text_input(
    "¿Qué valor mostró?"
)

if st.button("Validar Nivel 2"):

    if respuesta.strip() != "":

        st.success("Correcto")

        st.session_state["nivel"] = 3

        st.rerun()

    else:

        st.error("Ingrese una respuesta")
```

# ---------------------------------

# NIVEL 3

# ---------------------------------

elif st.session_state["nivel"] == 3:

```
st.header("Nivel 3 - Permisos")

st.write("""
Asigne permisos de ejecución
a bienvenida.sh usando chmod.
""")

respuesta = st.text_input(
    "¿Qué permisos tiene el propietario?"
)

if st.button("Validar Nivel 3"):

    if respuesta.lower() == "rwx":

        st.success("Correcto")

        st.session_state["nivel"] = 4

        st.rerun()

    else:

        st.error("Incorrecto")
```

# ---------------------------------

# NIVEL 4

# ---------------------------------

elif st.session_state["nivel"] == 4:

```
st.header("Nivel 4 - IF")

st.write("""
Cree un script con:

edad=20

Si la edad es mayor a 18
debe mostrar:

Mayor
""")

respuesta = st.text_input(
    "¿Qué mostró el script?"
)

if st.button("Validar Nivel 4"):

    if respuesta.lower() == "mayor":

        st.success("Correcto")

        st.session_state["nivel"] = 5

        st.rerun()

    else:

        st.error("Incorrecto")
```

# ---------------------------------

# NIVEL 5

# ---------------------------------

elif st.session_state["nivel"] == 5:

```
st.header("Nivel 5 - FOR")

st.write("""
Cree un script que muestre:

1
2
3
""")

respuesta = st.text_input(
    "¿Cuál fue el último número mostrado?"
)

if st.button("Finalizar"):

    if respuesta == "3":

        st.balloons()

        st.success(
            "🏆 Proyecto Final Completado"
        )

    else:

        st.error("Respuesta incorrecta")
```
