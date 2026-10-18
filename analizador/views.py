from django.shortcuts import render
from .forms import NumeroForm, TextoForm
from .logic import convertir_numero, analizar_texto


def inicio(request):
    numero_form = NumeroForm(request.POST if request.method == "POST" and request.POST.get("accion") == "convertir" else None, prefix="numero")
    texto_form = TextoForm(request.POST if request.method == "POST" and request.POST.get("accion") == "analizar" else None, prefix="texto")
    conversion = None
    caracteres = None
    errores = []

    if request.method == "POST":
        accion = request.POST.get("accion")

        if accion == "convertir":
            if numero_form.is_valid():
                try:
                    conversion = convertir_numero(
                        numero_form.cleaned_data["numero"],
                        int(numero_form.cleaned_data["base"]),
                    )
                except ValueError as error:
                    errores.append(str(error))
            else:
                errores.extend(
                    error for field_errors in numero_form.errors.values()
                    for error in field_errors
                )

        elif accion == "analizar":
            if texto_form.is_valid():
                try:
                    caracteres = analizar_texto(texto_form.cleaned_data["texto"])
                except ValueError as error:
                    errores.append(str(error))
            else:
                errores.extend(
                    error for field_errors in texto_form.errors.values()
                    for error in field_errors
                )
        else:
            errores.append("Seleccione una operación válida.")

    return render(request, "analizador/index.html", {
        "numero_form": numero_form,
        "texto_form": texto_form,
        "conversion": conversion,
        "caracteres": caracteres,
        "errores": errores,
    })
