# Analizador de representación de datos

Aplicación web desarrollada con Python 3.12 y Django para convertir números entre las bases 2, 8, 10 y 16, y analizar caracteres Unicode y su representación en bytes UTF-8.

## Funcionalidades

- Conversión de números entre las bases binaria, octal, decimal y hexadecimal.
- Validación de bases, dígitos, entradas vacías, números negativos y valores fuera del rango de 0 a 65535.
- Representación binaria completada a múltiplos de 8 bits.
- Cálculo de bits significativos y bytes necesarios.
- Análisis de cada carácter: valor decimal, punto de código Unicode, hexadecimal y cantidad de bytes UTF-8.
- Pruebas automatizadas para comprobar conversiones y validaciones.

## Requisitos

- Python 3.12.
- Django 5.2.7.
- Docker Desktop, para ejecutar la aplicación en un contenedor.

## Ejecución local en Windows

Desde PowerShell, dentro de la carpeta del proyecto, ejecuta los siguientes comandos uno por uno:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py check
python manage.py test
python manage.py runserver
```

Abre la aplicación en el navegador:

http://127.0.0.1:8000/

## Ejecución con Docker

Asegúrate de que Docker Desktop esté en funcionamiento. Ejecuta los comandos uno por uno:

```powershell
docker compose build
docker compose up -d
docker compose exec web python manage.py migrate
docker stats --no-stream analizador_datos
```

Para consultar los registros:

```powershell
docker compose logs
```

Para detener los contenedores:

```powershell
docker compose down
```

El servicio publica el puerto 8000 y configura un límite de 256 MiB de memoria y 1 CPU.

## Arquitectura de Von Neumann y contenedores

En la arquitectura de Von Neumann, la CPU ejecuta instrucciones, la memoria principal mantiene las instrucciones y los datos necesarios durante la ejecución, y el almacenamiento conserva los archivos y programas.

En esta aplicación, Django recibe los datos enviados desde el navegador, ejecuta la lógica de conversión o análisis y devuelve los resultados.

Un contenedor Docker comparte el kernel del sistema operativo anfitrión. A diferencia de una máquina virtual tradicional, no necesita ejecutar un sistema operativo invitado con su propio kernel. Docker proporciona aislamiento de procesos y permite limitar recursos como memoria y CPU mediante mecanismos del kernel, como los cgroups.

## Casos de prueba para la demostración

1. **Conversión válida:** introducir `255` en base decimal y comprobar los resultados: binario `11111111`, octal `377` y hexadecimal `FF`.
2. **Validación de base:** introducir `102` en base binaria y comprobar que se rechaza.
3. **Unicode y UTF-8:** analizar el carácter `ñ` y comprobar su punto de código `U+00F1`, valor decimal `241`, hexadecimal `F1` y longitud de 2 bytes UTF-8.
4. **Pruebas automatizadas:** ejecutar `python manage.py test`.
5. **Docker:** comprobar el consumo y los límites mediante `docker stats --no-stream analizador_datos`.

## Entrega

- **Repositorio público:** https://github.com/RutSanchez/analizador-representacion-datos-examen
- **Video de demostración (máximo 2 minutos):** https://drive.google.com/file/d/1in4JqEZ1b6xK-Rzw6g_Rn_qvZul5OER0/view?usp=sharing

