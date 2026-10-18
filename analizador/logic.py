BASES_VALIDAS = {2, 8, 10, 16}


def convertir_numero(numero, base):
    """Convierte un entero no negativo entre 0 y 65535 a varias bases."""
    if numero is None or not str(numero).strip():
        raise ValueError("Debe ingresar un número.")

    numero = str(numero).strip()

    if base not in BASES_VALIDAS:
        raise ValueError("La base debe ser 2, 8, 10 o 16.")

    if numero.startswith("-"):
        raise ValueError("No se permiten valores negativos.")

    if numero.startswith("+"):
        raise ValueError("Ingrese el número sin signo.")

    try:
        valor = int(numero, base)
    except ValueError:
        raise ValueError(f"El número contiene dígitos inválidos para la base {base}.") from None

    if not 0 <= valor <= 65535:
        raise ValueError("El valor convertido debe estar entre 0 y 65535.")

    bits_significativos = max(1, valor.bit_length())
    bytes_necesarios = max(1, (bits_significativos + 7) // 8)
    bits_representacion = bytes_necesarios * 8

    return {
        "decimal": str(valor),
        "binario": format(valor, f"0{bits_representacion}b"),
        "octal": format(valor, "o"),
        "hexadecimal": format(valor, "X"),
        "bits_significativos": bits_significativos,
        "bytes_necesarios": bytes_necesarios,
        "bits_representacion": bits_representacion,
    }


def analizar_texto(texto):
    """Devuelve información Unicode y UTF-8 para cada carácter."""
    if texto is None or texto == "":
        raise ValueError("Debe ingresar un texto.")
    if len(texto) > 20:
        raise ValueError("El texto no puede superar 20 caracteres.")

    resultados = []
    for caracter in texto:
        codigo = ord(caracter)
        resultados.append({
            "caracter": caracter,
            "decimal": codigo,
            "unicode": f"U+{codigo:04X}",
            "hexadecimal": f"{codigo:X}",
            "bytes_utf8": len(caracter.encode("utf-8")),
        })
    return resultados
