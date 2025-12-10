import streamlit as st
import pandas as pd

st.set_page_config(page_title="Yami & Yumi", page_icon="🍡")

st.title("🌙 Buscando a mi hermano ☀️")
st.markdown("### ¡Bienvenido al desafío de Mercadito de Asia!")

# Formulario simple
with st.form("registro"):
    personaje = st.radio("¿Qué personaje te tocó?", ["Yami (Nena/Luna 🌙)", "Yumi (Nene/Sol ☀️)"])
    codigo = st.text_input("Ingresá tu Código (Ej: A2580)").upper().strip()
    instagram = st.text_input("Tu usuario de Instagram (@...)").strip()
    enviado = st.form_submit_button("🔍 ¡Buscar match!")

if enviado:
    if not codigo or not instagram:
        st.error("Por favor completá todos los datos.")
    else:
        st.success(f"¡Hola {instagram}! Guardamos que tenés a {personaje} con código {codigo}.")
        st.info("⚠️ Esta es una versión de prueba. Si encontrás a alguien con tu mismo código, ¡escribile!")
        
        # Simulación de visualización (Para que veas algo en pantalla)
        st.write("---")
        st.write("Participantes recientes:")
        st.write(f"1. {instagram} - {codigo} ({personaje})")
