# 📊 Backend - Sistema Full Stack de Analítica Predictiva para la Deserción Estudiantil

## 📌 Descripción del Proyecto

Este proyecto forma parte del desarrollo de un **Sistema Full Stack de analítica predictiva** orientado a la identificación temprana del riesgo de deserción estudiantil en instituciones de educación superior.

El problema central radica en que muchas instituciones carecen de herramientas tecnológicas que integren modelos de **Machine Learning** dentro de una arquitectura moderna, lo que limita la toma de decisiones preventivas basadas en datos.

Este backend proporciona los servicios necesarios para:

* Gestión de datos académicos
* Procesamiento de información
* Integración con modelos predictivos
* Exposición de APIs seguras para consumo del frontend

---

## 🎯 Objetivo del Backend

Desarrollar una API robusta que permita integrar modelos de Machine Learning para analizar datos académicos y generar predicciones sobre el riesgo de deserción estudiantil, facilitando la toma de decisiones institucionales.

---

## 🏗️ Arquitectura del Sistema

El backend sigue una arquitectura desacoplada (Frontend - Backend), basada en servicios REST.

### 🔹 Componentes principales:

* **API Backend**

  * Framework: Django + Django REST Framework
  * Autenticación: JWT (JSON Web Tokens)
  * Control de acceso basado en usuarios

* **Base de Datos**

  * Motor: PostgreSQL
  * Instalado localmente en la máquina host (no en contenedor Docker)

* **Módulo de Machine Learning**

  * Implementado de forma independiente
  * Modelo actual: Random Forest
  * Encargado de generar predicciones de riesgo de deserción

* **Contenedorización**

  * Uso de Docker para levantar el servicio backend

---

## 🛠️ Tecnologías Utilizadas

* Python 3.x
* Django >= 4.2
* Django REST Framework
* JWT Authentication (SimpleJWT)
* PostgreSQL
* Docker
* Pandas (procesamiento de datos)
* Scikit-learn (modelo Random Forest)

---

## 📦 Requisitos del Proyecto

### 🔹 Dependencias principales

```txt
Django>=4.2
psycopg2-binary
djangorestframework
djangorestframework-simplejwt
django-cors-headers
pandas
scikit-learn
joblib
```

---

## 🔐 Seguridad

El sistema implementa:

* Autenticación basada en JWT
* Configuración de CORS para permitir comunicación con el frontend
* Control de acceso a endpoints protegidos

---

## 🐳 Ejecución del Proyecto con Docker

### 🔹 1. Clonar el repositorio

```bash
git clone [<URL_DEL_REPOSITORIO>](https://github.com/RichardBercap/seminariofinal-backend.git)
cd backend
```

---

### 🔹 2. Configurar variables de entorno

Crear un archivo `.env` o configurar directamente en `settings.py`:

```env
DB_NAME=nombre_db
DB_USER=postgres
DB_PASSWORD=tu_password
DB_HOST=host.docker.internal
DB_PORT=5432
```

> ⚠️ Nota: PostgreSQL debe estar corriendo en la máquina local (host).

---

### 🔹 3. Construir y levantar contenedores

```bash
docker compose up --build
```

---

## 🗄️ Configuración de Base de Datos

> ⚠️ Importante: Este proyecto **NO utiliza migraciones de Django**

### 🔹 1. Crear la base de datos en PostgreSQL

```sql
CREATE DATABASE nombre_db;
```

---

### 🔹 2. Ejecutar script SQL

Debes ejecutar manualmente el script SQL que contiene la estructura de tablas:

```bash
psql -U postgres -d nombre_db -f schema.sql
```

---

## 👤 Creación de Usuario Administrador

Para acceder al sistema:

```bash
docker compose exec web python manage.py createsuperuser
```

Luego ingresar credenciales:

* Username
* Email
* Password

---

## 🔗 Endpoints Principales

* `/api/auth/login/` → Autenticación JWT
* `/api/...` → Endpoints protegidos para gestión de datos
* `/api/predictions/` → Resultados del modelo predictivo

---

## 🤖 Módulo de Machine Learning

El módulo de Machine Learning actualmente:

* Se encuentra desacoplado del backend principal
* Está implementado en un archivo independiente
* Utiliza el algoritmo **Random Forest**

### 🔹 Funcionalidades:

* Lectura de datasets académicos (CSV)
* Procesamiento y limpieza de datos
* Entrenamiento del modelo
* Generación de predicciones

---

## 🧪 Validación del Sistema

El sistema es validado mediante:

* Pruebas técnicas del backend (endpoints)
* Evaluación de resultados del modelo predictivo
* Pruebas de integración con frontend

---

## 📈 Alcance del Sistema

Este backend permite:

* Gestionar datos académicos de estudiantes
* Procesar datasets para análisis predictivo
* Generar información útil para la toma de decisiones
* Integrarse con dashboards analíticos en el frontend

---

## ⚠️ Limitaciones

* El modelo de Machine Learning está en una versión inicial (Random Forest)
* No se utilizan migraciones automáticas
* Dependencia de base de datos local
* No incluye despliegue en producción aún

---

## 🚀 Futuras Mejoras

* Integración completa del modelo ML dentro del backend
* Implementación de más algoritmos (Regresión Lineal, etc.)
* Automatización de migraciones
* Despliegue en la nube
* Optimización de rendimiento

---

## 👨‍💻 Autor

RICHARD BERNA, proyecto seminario de especialización UNIVERSIDAD CATÓLICA BOLIVIANA SAN PABLO

---
