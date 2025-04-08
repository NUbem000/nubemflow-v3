import functions_framework
from cloud_use_google_token import cargar_token_desde_storage, usar_token_para_calendar, usar_token_para_gmail

@functions_framework.http
def ejecutar_token_google(request):
    cargar_token_desde_storage()
    usar_token_para_calendar()
    usar_token_para_gmail()
    return "✅ Token Google usado correctamente (Calendar + Gmail)", 200