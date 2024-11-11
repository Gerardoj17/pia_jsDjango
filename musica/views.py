from django.shortcuts import render, redirect
from .models import Feedback

# Create your views here.
def index(request):
    return render(request,"index.html")
def Academica(request):
    return render(request,"Academica.html")
def Ceremonial(request):
    return render(request,"Ceremonial.html")
def Comercial(request):
    return render(request,"Comercial.html")
def Publicitaria(request):
    return render(request,"index.html")

def RegistrarFeedback(request):
    # Capturar los datos del formulario desde los campos ocultos
    te_gusta_la_pagina = request.POST.get('Te_gusta_la_pagina')
    genero_musical = request.POST.get('Genero')
    frecuencia_escucha = request.POST.get('Frecuencia')
    plataforma_utilizada = request.POST.get('Plataforma')
    aprender_mas_musica = request.POST.get('Aprender')

    # Verificar que todos los campos han sido seleccionados
    if te_gusta_la_pagina and genero_musical and frecuencia_escucha and plataforma_utilizada and aprender_mas_musica:
        # Crear el registro en la base de datos
        feedback = Feedback.objects.create(
            te_gusta_la_pagina=te_gusta_la_pagina,
            genero_musical=genero_musical,
            frecuencia_escucha=frecuencia_escucha,
            plataforma_utilizada=plataforma_utilizada,
            aprender_mas_musica=aprender_mas_musica
        )

        # Redirigir a la página de inicio o a una página de confirmación
        return redirect('index')
