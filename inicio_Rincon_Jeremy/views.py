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

def detalle_tema(request, id):

    temas = {
        1: {
            'nombre': 'Tema 1',
            'descripcion': 'Descripción del primer tema de nuestro proyecto.',
            'imagenes': [
                'inicio_Rincon_Jeremy/images/tema1_1.jpg',
                'inicio_Rincon_Jeremy/images/tema1_2.jpg',
            ]
        },
        2: {
            'nombre': 'Tema 2',
            'descripcion': 'Descripción del segundo tema de nuestro proyecto.',
            'imagenes': [
                'inicio_Rincon_Jeremy/images/tema2_1.jpg',
                'inicio_Rincon_Jeremy/images/tema2_2.jpg',
            ]
        }
    }

    tema = temas.get(id)

    if tema is None:
        return render(
            request,
            'inicio_Rincon_Jeremy/inicio.html'
        )

    return render(
        request,
        'inicio_Rincon_Jeremy/detalle.html',
        {'tema': tema}
    )