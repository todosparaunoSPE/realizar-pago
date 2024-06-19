# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 10:27:45 2024

@author: jperezr
"""

import streamlit as st

# Título de la Aplicación
st.title('Pagar Servicio de Gestión de Contactos')

# URL del producto en Stripe
stripe_product_url = "https://buy.stripe.com/5kAbKi4tC5up6Fq7ss"

# Mostrar el enlace para pagar
if st.button('Pagar'):
    st.write("Procede al siguiente enlace para completar el pago:")
    st.markdown(f'<a href="{stripe_product_url}" target="_blank">Pagar ahora</a>', unsafe_allow_html=True)
