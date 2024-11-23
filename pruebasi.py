# -*- coding: utf-8 -*-
"""pruebasi.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1LavK5GdUl7s8zV28DZhLGHvTFVYMUdBj
"""

pip install requests pandas streamlit matplotlib

import requests
import json
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Función para obtener datos de la API REST Countries
def obtener_datos_api():
    url = "https://restcountries.com/v3.1/all"
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        return respuesta.json()
    else:
        st.error("Error al obtener los datos de la API.")
        return []

# Función para procesar los datos obtenidos de la API
def procesar_datos(datos):
    paises = []
    for pais in datos:
        paises.append({
            "Nombre": pais.get("name", {}).get("common", "Desconocido"),
            "Región": pais.get("region", "Desconocido"),
            "Población": pais.get("population", 0),
            "Área": pais.get("area", 0),
            "Fronteras": len(pais.get("borders", [])),
            "Idiomas": len(pais.get("languages", {})),
            "Zonas Horarias": len(pais.get("timezones", []))
        })
    return pd.DataFrame(paises)

# Configuración de la aplicación multipágina
def main():
    st.set_page_config(page_title="Análisis de Datos - REST Countries", layout="wide")

    # Sidebar para navegar entre páginas
    menu = ["Descripción del Proyecto", "Interacción con Datos", "Gráficos Interactivos"]
    eleccion = st.sidebar.selectbox("Seleccione una página", menu)

    # Cargar datos de la API
    datos_api = obtener_datos_api()
    if not datos_api:
        return

    df_paises = procesar_datos(datos_api)

    if eleccion == "Descripción del Proyecto":
        st.title("Descripción del Proyecto")
        st.markdown(
            """### Proyecto: Análisis de Datos de REST Countries

Este proyecto utiliza datos de la API REST Countries para realizar un análisis exploratorio sobre información de países como población, área, regiones, y más. La aplicación permite visualizar y analizar estos datos mediante gráficos y herramientas interactivas.

**Fuente de Datos:** [REST Countries](https://restcountries.com/v3.1/all)

**Librerías Usadas:** requests, pandas, matplotlib, y Streamlit.

            """
        )

    elif eleccion == "Interacción con Datos":
        st.title("Interacción con Datos")

        # Mostrar datos originales
        if st.checkbox("Mostrar Datos Originales"):
            st.dataframe(df_paises)

        # Análisis de una columna específica
        columna = st.selectbox("Seleccione una columna para análisis estadístico", ["Población", "Área"])
        if columna:
            st.write(f"### Estadísticas de {columna}")
            st.write(f"Media: {df_paises[columna].mean():,.2f}")
            st.write(f"Mediana: {df_paises[columna].median():,.2f}")
            st.write(f"Desviación Estándar: {df_paises[columna].std():,.2f}")

        # Ordenar datos
        columna_orden = st.selectbox("Seleccione una columna para ordenar los datos", df_paises.columns)
        if columna_orden:
            ascendente = st.radio("Ordenar en", ["Ascendente", "Descendente"]) == "Ascendente"
            df_ordenado = df_paises.sort_values(by=columna_orden, ascending=ascendente)
            st.dataframe(df_ordenado)

        # Filtrar filas
        filtro = st.slider("Filtrar por población mínima", int(df_paises["Población"].min()), int(df_paises["Población"].max()), 1000000)
        df_filtrado = df_paises[df_paises["Población"] >= filtro]
        st.dataframe(df_filtrado)

        # Descargar datos filtrados
        if st.button("Descargar Datos Filtrados"):
            df_filtrado.to_csv("datos_filtrados.csv", index=False)
            st.success("Archivo descargado como datos_filtrados.csv")

    elif eleccion == "Gráficos Interactivos":
        st.title("Gráficos Interactivos")

        # Selección de variables
        x_var = st.selectbox("Seleccione la variable para el eje X", ["Población", "Área"])
        y_var = st.selectbox("Seleccione la variable para el eje Y", ["Población", "Área"])

        if x_var and y_var:
            st.write(f"### Gráfico de {x_var} vs {y_var}")
            tipo_grafico = st.selectbox("Seleccione el tipo de gráfico", ["Dispersión", "Línea", "Barra"])

            fig, ax = plt.subplots()
            if tipo_grafico == "Dispersión":
                ax.scatter(df_paises[x_var], df_paises[y_var])
            elif tipo_grafico == "Línea":
                ax.plot(df_paises[x_var], df_paises[y_var])
            elif tipo_grafico == "Barra":
                ax.bar(df_paises[x_var], df_paises[y_var])

            ax.set_xlabel(x_var)
            ax.set_ylabel(y_var)
            ax.set_title(f"{tipo_grafico} de {x_var} vs {y_var}")
            st.pyplot(fig)

        if st.button("Descargar Gráfico en PNG"):
            fig.savefig("grafico.png")
            st.success("Gráfico descargado como grafico.png")

if __name__ == "__main__":
    main()
import requests
import json
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Función para obtener datos de la API REST Countries
def obtener_datos_api():
    url = "https://restcountries.com/v3.1/all"
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        return respuesta.json()
    else:
        st.error("Error al obtener los datos de la API.")
        return []

# Función para procesar los datos obtenidos de la API
def procesar_datos(datos):
    paises = []
    for pais in datos:
        paises.append({
            "Nombre": pais.get("name", {}).get("common", "Desconocido"),
            "Región": pais.get("region", "Desconocido"),
            "Población": pais.get("population", 0),
            "Área": pais.get("area", 0),
            "Fronteras": len(pais.get("borders", [])),
            "Idiomas": len(pais.get("languages", {})),
            "Zonas Horarias": len(pais.get("timezones", []))
        })
    return pd.DataFrame(paises)

# Configuración de la aplicación multipágina
def main():
    st.set_page_config(page_title="Análisis de Datos - REST Countries", layout="wide")

    # Sidebar para navegar entre páginas
    menu = ["Descripción del Proyecto", "Interacción con Datos", "Gráficos Interactivos"]
    eleccion = st.sidebar.selectbox("Seleccione una página", menu)

    # Cargar datos de la API
    datos_api = obtener_datos_api()
    if not datos_api:
        return

    df_paises = procesar_datos(datos_api)

    if eleccion == "Descripción del Proyecto":
        st.title("Descripción del Proyecto")
        st.markdown(
            """### Proyecto: Análisis de Datos de REST Countries

Este proyecto utiliza datos de la API REST Countries para realizar un análisis exploratorio sobre información de países como población, área, regiones, y más. La aplicación permite visualizar y analizar estos datos mediante gráficos y herramientas interactivas.

**Fuente de Datos:** [REST Countries](https://restcountries.com/v3.1/all)

**Librerías Usadas:** requests, pandas, matplotlib, y Streamlit.

            """
        )

    elif eleccion == "Interacción con Datos":
        st.title("Interacción con Datos")

        # Mostrar datos originales
        if st.checkbox("Mostrar Datos Originales"):
            st.dataframe(df_paises)

        # Análisis de una columna específica
        columna = st.selectbox("Seleccione una columna para análisis estadístico", ["Población", "Área"])
        if columna:
            st.write(f"### Estadísticas de {columna}")
            st.write(f"Media: {df_paises[columna].mean():,.2f}")
            st.write(f"Mediana: {df_paises[columna].median():,.2f}")
            st.write(f"Desviación Estándar: {df_paises[columna].std():,.2f}")

        # Ordenar datos
        columna_orden = st.selectbox("Seleccione una columna para ordenar los datos", df_paises.columns)
        if columna_orden:
            ascendente = st.radio("Ordenar en", ["Ascendente", "Descendente"]) == "Ascendente"
            df_ordenado = df_paises.sort_values(by=columna_orden, ascending=ascendente)
            st.dataframe(df_ordenado)

        # Filtrar filas
        filtro = st.slider("Filtrar por población mínima", int(df_paises["Población"].min()), int(df_paises["Población"].max()), 1000000)
        df_filtrado = df_paises[df_paises["Población"] >= filtro]
        st.dataframe(df_filtrado)

        # Descargar datos filtrados
        if st.button("Descargar Datos Filtrados"):
            df_filtrado.to_csv("datos_filtrados.csv", index=False)
            st.success("Archivo descargado como datos_filtrados.csv")

    elif eleccion == "Gráficos Interactivos":
        st.title("Gráficos Interactivos")

        # Selección de variables
        x_var = st.selectbox("Seleccione la variable para el eje X", ["Población", "Área"])
        y_var = st.selectbox("Seleccione la variable para el eje Y", ["Población", "Área"])

        if x_var and y_var:
            st.write(f"### Gráfico de {x_var} vs {y_var}")
            tipo_grafico = st.selectbox("Seleccione el tipo de gráfico", ["Dispersión", "Línea", "Barra"])

            fig, ax = plt.subplots()
            if tipo_grafico == "Dispersión":
                ax.scatter(df_paises[x_var], df_paises[y_var])
            elif tipo_grafico == "Línea":
                ax.plot(df_paises[x_var], df_paises[y_var])
            elif tipo_grafico == "Barra":
                ax.bar(df_paises[x_var], df_paises[y_var])

            ax.set_xlabel(x_var)
            ax.set_ylabel(y_var)
            ax.set_title(f"{tipo_grafico} de {x_var} vs {y_var}")
            st.pyplot(fig)

        if st.button("Descargar Gráfico en PNG"):
            fig.savefig("grafico.png")
            st.success("Gráfico descargado como grafico.png")

if __name__ == "__main__":
    main()
import requests
import json
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Función para obtener datos de la API REST Countries
def obtener_datos_api():
    url = "https://restcountries.com/v3.1/all"
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        return respuesta.json()
    else:
        st.error("Error al obtener los datos de la API.")
        return []

# Función para procesar los datos obtenidos de la API
def procesar_datos(datos):
    paises = []
    for pais in datos:
        paises.append({
            "Nombre": pais.get("name", {}).get("common", "Desconocido"),
            "Región": pais.get("region", "Desconocido"),
            "Población": pais.get("population", 0),
            "Área": pais.get("area", 0),
            "Fronteras": len(pais.get("borders", [])),
            "Idiomas": len(pais.get("languages", {})),
            "Zonas Horarias": len(pais.get("timezones", []))
        })
    return pd.DataFrame(paises)

# Configuración de la aplicación multipágina
def main():
    st.set_page_config(page_title="Análisis de Datos - REST Countries", layout="wide")

    # Sidebar para navegar entre páginas
    menu = ["Descripción del Proyecto", "Interacción con Datos", "Gráficos Interactivos"]
    eleccion = st.sidebar.selectbox("Seleccione una página", menu)

    # Cargar datos de la API
    datos_api = obtener_datos_api()
    if not datos_api:
        return

    df_paises = procesar_datos(datos_api)

    if eleccion == "Descripción del Proyecto":
        st.title("Descripción del Proyecto")
        st.markdown(
            """### Proyecto: Análisis de Datos de REST Countries

Este proyecto utiliza datos de la API REST Countries para realizar un análisis exploratorio sobre información de países como población, área, regiones, y más. La aplicación permite visualizar y analizar estos datos mediante gráficos y herramientas interactivas.

**Fuente de Datos:** [REST Countries](https://restcountries.com/v3.1/all)

**Librerías Usadas:** requests, pandas, matplotlib, y Streamlit.

            """
        )

    elif eleccion == "Interacción con Datos":
        st.title("Interacción con Datos")

        # Mostrar datos originales
        if st.checkbox("Mostrar Datos Originales"):
            st.dataframe(df_paises)

        # Análisis de una columna específica
        columna = st.selectbox("Seleccione una columna para análisis estadístico", ["Población", "Área"])
        if columna:
            st.write(f"### Estadísticas de {columna}")
            st.write(f"Media: {df_paises[columna].mean():,.2f}")
            st.write(f"Mediana: {df_paises[columna].median():,.2f}")
            st.write(f"Desviación Estándar: {df_paises[columna].std():,.2f}")

        # Ordenar datos
        columna_orden = st.selectbox("Seleccione una columna para ordenar los datos", df_paises.columns)
        if columna_orden:
            ascendente = st.radio("Ordenar en", ["Ascendente", "Descendente"]) == "Ascendente"
            df_ordenado = df_paises.sort_values(by=columna_orden, ascending=ascendente)
            st.dataframe(df_ordenado)

        # Filtrar filas
        filtro = st.slider("Filtrar por población mínima", int(df_paises["Población"].min()), int(df_paises["Población"].max()), 1000000)
        df_filtrado = df_paises[df_paises["Población"] >= filtro]
        st.dataframe(df_filtrado)

        # Descargar datos filtrados
        if st.button("Descargar Datos Filtrados"):
            df_filtrado.to_csv("datos_filtrados.csv", index=False)
            st.success("Archivo descargado como datos_filtrados.csv")

    elif eleccion == "Gráficos Interactivos":
        st.title("Gráficos Interactivos")

        # Selección de variables
        x_var = st.selectbox("Seleccione la variable para el eje X", ["Población", "Área"])
        y_var = st.selectbox("Seleccione la variable para el eje Y", ["Población", "Área"])

        if x_var and y_var:
            st.write(f"### Gráfico de {x_var} vs {y_var}")
            tipo_grafico = st.selectbox("Seleccione el tipo de gráfico", ["Dispersión", "Línea", "Barra"])

            fig, ax = plt.subplots()
            if tipo_grafico == "Dispersión":
                ax.scatter(df_paises[x_var], df_paises[y_var])
            elif tipo_grafico == "Línea":
                ax.plot(df_paises[x_var], df_paises[y_var])
            elif tipo_grafico == "Barra":
                ax.bar(df_paises[x_var], df_paises[y_var])

            ax.set_xlabel(x_var)
            ax.set_ylabel(y_var)
            ax.set_title(f"{tipo_grafico} de {x_var} vs {y_var}")
            st.pyplot(fig)

        if st.button("Descargar Gráfico en PNG"):
            fig.savefig("grafico.png")
            st.success("Gráfico descargado como grafico.png")

if __name__ == "__main__":
    main()