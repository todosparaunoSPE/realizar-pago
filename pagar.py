# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 10:27:45 2024

@author: jperezr
"""

import streamlit as st

# Título de la Aplicación
st.title('Pagar Servicio de Gestión de Contactos')

st.subheader("")
st.subheader("")

st.subheader("El precio de suscripción para uso de la aplicación es de $100 por semestre")

st.subheader("")

st.subheader("No olvides ingresar tu correo electrónico")

# Ayuda para usuarios en el sidebar
st.sidebar.header("Ayuda")
st.sidebar.markdown("""
Este código en Python crea una aplicación web interactiva utilizando la biblioteca Streamlit para gestionar y analizar redes de contactos de LinkedIn. A continuación, te detallo sus características y funcionalidades principales:

**Título y Encabezado:**

La aplicación se presenta con el título "Gestión de Redes de Contactos de LinkedIn" y un encabezado con el autor "Creado por: jahoperi".

**Carga de Datos:**

Permite cargar un archivo CSV con los contactos desde una barra lateral.

**Visualización de Contactos:**

Muestra una tabla con los contactos cargados en la página principal.

**Añadir Nuevos Contactos:**

A través de la barra lateral, permite introducir y añadir nuevos contactos con campos como Nombre, Empresa, Correo, Teléfono, Etiqueta, Recordatorio y Notas.

**Buscar Contactos:**

Funcionalidad de búsqueda que permite filtrar contactos por nombre.

**Editar Contactos:**

Permite seleccionar un contacto existente y editar sus detalles.

**Eliminar Contactos:**

Funcionalidad para eliminar contactos seleccionados.

**Etiquetado de Contactos:**

Posibilidad de añadir etiquetas a contactos existentes para su clasificación.

**Recordatorios de Seguimiento:**

Permite añadir fechas de recordatorio para hacer seguimiento a contactos específicos.

**Análisis de Interacciones:**

Muestra interacciones con un contacto seleccionado, aunque esta sección parece estar planificada para futuras funcionalidades.

**Exportar Contactos:**

Permite descargar la lista de contactos en formato CSV.

**Gráficos y Visualizaciones:**

Muestra gráficos de barras con el conteo de etiquetas de los contactos, utilizando matplotlib para las visualizaciones.

**Guardar Cambios:**

Permite guardar los contactos actualizados en un archivo CSV llamado contacts_updated.csv.

Este código facilita la gestión de redes de contactos, permitiendo agregar, editar, buscar, etiquetar y eliminar contactos de manera intuitiva y visual. Además, ofrece la funcionalidad de exportar los datos y generar gráficos para una mejor comprensión y análisis de la red de contactos.
""")


# URL del producto en Stripe
stripe_product_url = "https://buy.stripe.com/5kAbKi4tC5up6Fq7ss"

# Mostrar el enlace para pagar
if st.button('Pagar'):
    st.write("Procede al siguiente enlace para completar el pago:")
    st.markdown(f'<a href="{stripe_product_url}" target="_blank">Pagar ahora</a>', unsafe_allow_html=True)
