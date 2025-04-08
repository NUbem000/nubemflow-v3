import sys
import pytest
from pathlib import Path

# Asegura que el path raíz esté en sys.path
ROOT = Path(__file__).parent.resolve()
sys.path.append(str(ROOT))

# Ejecutar pruebas
exit(pytest.main(["tests", "-v", "--tb=short", "--disable-warnings"]))