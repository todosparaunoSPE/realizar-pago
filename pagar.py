# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 10:27:45 2024

@author: jperezr
"""

import streamlit as st
import requests
import stripe

# Función para obtener la tasa de cambio actual
def get_exchange_rate(base_currency, target_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()
    rate = data['rates'].get(target_currency)
    if rate:
        return rate
    else:
        return None

# Clave de API de Stripe
stripe.api_key = "sk_test_51PTPe6P9rVcM6GuzXkFbVVk5CDHMNbpjKtjkdeVJuihCHtc6Km2QTAC4b3Z6ah8ICxc59Ug1aDDn0bxBvDEgom1r00fMtM4K3x"  # Clave secreta

# Título de la Aplicación
st.title('Pagar Servicio de Gestión de Contactos')

# Obtener la tasa de cambio actual de MXN a USD
exchange_rate = get_exchange_rate("MXN", "USD")

if exchange_rate:
    st.write(f"Tasa de cambio MXN/USD: {exchange_rate}")

    # Monto a pagar en MXN
    amount_mxn = 100

    # Monto a pagar en USD
    amount_usd = amount_mxn / exchange_rate

    st.write(f'Monto a pagar: {amount_mxn} MXN')

    # Integración de Stripe para pagos
    st.header('Realizar Pago')
    if st.button('Pagar'):
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': 'Servicio de Gestión de Contactos',
                    },
                    'unit_amount': int(amount_usd * 100),
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='https://agenda-gezabdkmhmy82vk2cmaztu.streamlit.app/',
            cancel_url='https://pago-cancelado-nrswpxmrmartvyslvfmwcg.streamlit.app/',
        )
        st.write("Procede al siguiente enlace para completar el pago:")
        st.markdown(f'<a href="{session.url}" target="_blank">Pagar ahora</a>', unsafe_allow_html=True)
else:
    st.error("No se pudo obtener la tasa de cambio actual. Por favor, inténtalo más tarde.")