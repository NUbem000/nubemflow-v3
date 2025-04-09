from google.cloud import storage
import os
import pickle
from googleapiclient.discovery import build

# Nombre del bucket y objeto
BUCKET_NAME = os.getenv("BUCKET_NAME", "nubemflow-oauth")
TOKEN_FILENAME = "token_google.pkl"
LOCAL_PATH = "/tmp/token_google.pkl"

def cargar_token_desde_storage():
    storage_client = storage.Client()
    bucket = storage_client.bucket(BUCKET_NAME)
    blob = bucket.blob(TOKEN_FILENAME)
    blob.download_to_filename(LOCAL_PATH)
    print("✅ Token descargado de Cloud Storage.")

def usar_token_para_calendar():
    with open(LOCAL_PATH, "rb") as token:
        creds = pickle.load(token)

    service = build("calendar", "v3", credentials=creds)
    eventos = service.events().list(calendarId='primary', maxResults=3).execute()
    for evento in eventos.get('items', []):
        print(f"📅 Evento: {evento.get('summary')} – {evento.get('start', {}).get('dateTime')}")

def usar_token_para_gmail():
    with open(LOCAL_PATH, "rb") as token:
        creds = pickle.load(token)

    service = build("gmail", "v1", credentials=creds)
    perfil = service.users().getProfile(userId="me").execute()
    print(f"📧 Gmail autenticado como: {perfil.get('emailAddress')}")

# MAIN SIMULACIÓN
if __name__ == "__main__":
    cargar_token_desde_storage()
    usar_token_para_calendar()
    usar_token_para_gmail()