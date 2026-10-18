
from django.test import SimpleTestCase, TestCase
from django.urls import reverse

from .logic import convertir_numero, analizar_texto
from .forms import TextoForm


class ConversionesTests(SimpleTestCase):

    def test_decimal_a_binario_con_relleno(self):
        self.assertEqual(
            convertir_numero("5", 10)["binario"],
            "00000101"
        )

    def test_256_ocupa_dos_bytes(self):
        resultado = convertir_numero("256", 10)

        self.assertEqual(
            resultado["binario"],
            "0000000100000000"
        )
        self.assertEqual(resultado["bytes_necesarios"], 2)

    def test_hexadecimal_a_decimal(self):
        self.assertEqual(
            convertir_numero("FF", 16)["decimal"],
            "255"
        )

    def test_binario_invalido(self):
        with self.assertRaisesRegex(ValueError, "dígitos inválidos"):
            convertir_numero("102", 2)

    def test_fuera_de_rango(self):
        with self.assertRaisesRegex(ValueError, "65535"):
            convertir_numero("65536", 10)

    def test_negativo(self):
        with self.assertRaisesRegex(ValueError, "negativos"):
            convertir_numero("-1", 10)

    def test_base_invalida(self):
        with self.assertRaisesRegex(ValueError, "base debe ser"):
            convertir_numero("10", 3)

    def test_entrada_vacia(self):
        with self.assertRaisesRegex(ValueError, "ingresar un número"):
            convertir_numero(" ", 10)

    def test_enie_utf8(self):
        item = analizar_texto("ñ")[0]

        self.assertEqual(item["decimal"], 241)
        self.assertEqual(item["unicode"], "U+00F1")
        self.assertEqual(item["hexadecimal"], "F1")
        self.assertEqual(item["bytes_utf8"], 2)

    def test_texto_mayor_de_20(self):
        with self.assertRaisesRegex(ValueError, "20 caracteres"):
            analizar_texto("a" * 21)


class FormularioTextoTests(SimpleTestCase):

    def test_acepta_20_caracteres(self):
        formulario = TextoForm(data={"texto": "a" * 20})

        self.assertTrue(formulario.is_valid())

    def test_rechaza_21_caracteres(self):
        formulario = TextoForm(data={"texto": "a" * 21})

        self.assertFalse(formulario.is_valid())
        self.assertIn("texto", formulario.errors)

    def test_rechaza_texto_vacio(self):
        formulario = TextoForm(data={"texto": ""})

        self.assertFalse(formulario.is_valid())
        self.assertIn("texto", formulario.errors)


class InterfazTests(TestCase):

    def test_pagina_principal(self):
        response = self.client.get(reverse("inicio"))

        self.assertEqual(response.status_code, 200)

    def test_conversion_desde_formulario(self):
        response = self.client.post(reverse("inicio"), {
            "numero-numero": "5",
            "numero-base": "10",
            "accion": "convertir",
        })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.context["conversion"]["binario"],
            "00000101"
        )

    def test_muestra_error_para_digito_invalido(self):
        response = self.client.post(reverse("inicio"), {
            "numero-numero": "102",
            "numero-base": "2",
            "accion": "convertir",
        })

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "dígitos inválidos")
