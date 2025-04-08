from google_auth_oauthlib.flow import InstalledAppFlow
import pickle
import os

# Escopes recomendados para NubemFlow (Gmail y Calendar, opcionalmente Meet)
SCOPES = [
    'https://www.googleapis.com/auth/calendar.readonly',
    'https://www.googleapis.com/auth/gmail.send'
]

def autenticar_google_oauth():
    creds = None
    token_path = "token_google.pkl"

    if os.path.exists(token_path):
        with open(token_path, 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials_oauth_google.json', SCOPES)
        creds = flow.run_local_server(port=0)

        with open(token_path, 'wb') as token:
            pickle.dump(creds, token)

    return creds

# Ejemplo de uso
if __name__ == "__main__":
    creds = autenticar_google_oauth()
    print("✅ Autenticación exitosa. Acceso a Google API concedido.")