import unittest
from unittest.mock import patch

from nubem_core.flujo_documentacion import generar_documentacion_con_gpt, guardar_localmente

class TestFlujoDocumentacion(unittest.TestCase):

    @patch("nubem_core.flujo_documentacion.generar_con_gpt")
    def test_generar_documentacion_con_gpt(self, mock_gpt):
        mock_gpt.return_value = "Documento generado por GPT."

        contexto = {
            "proyecto": "Sistema de Gestión IT",
            "incidencia": "INC-1234",
            "resumen": "El sistema falla al conectarse con la base de datos.",
            "scripts": ["conexion_db.py", "verificar_estado.py"],
            "equipo": {
                "PM": {
                    "nombre": "Laura",
                    "apellido": "Martínez",
                    "telefono": "600123456",
                    "empresa": "NubemSystems",
                    "direccion": "Carrer de la Tecnologia, 12",
                    "email": "laura.martinez@nubemsystems.es"
                }
            }
        }

        resultado = generar_documentacion_con_gpt(contexto)
        self.assertIn("contenido", resultado)
        self.assertIn("version", resultado)
        self.assertIn("timestamp", resultado)
        self.assertTrue(resultado["contenido"].startswith("Documento"))

    def test_guardar_localmente(self):
        contenido = "Este es un documento de prueba."
        nombre_archivo = "documento_prueba.txt"
        ruta = guardar_localmente(nombre_archivo, contenido)
        self.assertTrue(ruta.endswith(nombre_archivo))

if __name__ == '__main__':
    unittest.main()
