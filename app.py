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
