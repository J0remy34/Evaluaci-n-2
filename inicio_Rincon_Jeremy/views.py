from django.shortcuts import render


def inicio(request):

    temas = [
        {
            'id': 1,
            'nombre': 'Tema 1',
            'descripcion': 'Descripción del primer tema de nuestro proyecto.',
        },
        {
            'id': 2,
            'nombre': 'Tema 2',
            'descripcion': 'Descripción del segundo tema de nuestro proyecto.',
        },
    ]

    return render(
        request,
        'inicio_Rincon_Jeremy/inicio.html',
        {'temas': temas}
    )