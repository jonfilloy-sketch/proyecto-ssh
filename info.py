#!/usr/bin/env python3
import getpass
from datetime import datetime
# esto pinta el usuario el usuario y fechar actual
# hay que compartir el usuario
print(f"Usuario: {getpass.getuser()}")
print(f"Fecha: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
