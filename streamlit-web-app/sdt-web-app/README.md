# Streamlit Web App

This is the basis of a basic interactive dashboard for exploring properties of a used car dataset.

## Prerequisites
Pipenv

## Install dependencies
```
pipenv shell
pipenv install
```

## Run locally
```
streamlit run app.py
```

## Render

See the live app at: [https://sdt-web-app.onrender.com](https://sdt-web-app.onrender.com). When deploying the app to Render, include the commands below:

**Build Command**

```
pip install -r requirements.txt & pip install streamlit
```

**Start Command**

```
streamlit run app.py
```