import requests
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "index.html")


def peliculas(request, id):

    # Realizar una solicitud GET a una API externa (por ejemplo, JSONPlaceholder)
    response = requests.get(
        f'https://oaemdl.es/cinestar_sweb_php/peliculas/{id}')

    # Verificar si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:

        # Obtener los datos de la respuesta en formato JSON
        peliculas = response.json()

        # Procesar los datos como desees, por ejemplo, devolverlos como respuesta
        return render(request, 'peliculas.html', {"peliculas": peliculas})
    else:
        # Si la solicitud no fue exitosa, devolver un mensaje de error
        return HttpResponse("Error al consumir la API")


def pelicula(request, id):

    response = requests.get(
        f'https://oaemdl.es/cinestar_sweb_php/peliculas/{id}')

    if response.status_code == 200:

        pelicula = response.json()

        return render(request, 'pelicula.html', {"pelicula": pelicula})
    else:
        return HttpResponse("Error en el servidor")


def cines(request):

    response = requests.get("http://127.0.0.1:5000/cines")

    if response.status_code == 200:

        cines = response.json()

        return render(request, 'cines.html', {"cines": cines})
    else:
        return HttpResponse("Error en el servidor")


def cine(request, id):

    responseCine = requests.get(
        f'http://127.0.0.1:5000/cines/{id}')

    responseTarifas = requests.get(
        f'http://127.0.0.1:5000/cines/{id}/tarifas')

    responsePeliculas = requests.get(
        f'http://127.0.0.1:5000/cines/{id}/peliculas')

    if responseCine.status_code == 200 and responseTarifas.status_code == 200 and responsePeliculas.status_code == 200:
        cine = responseCine.json()
        tarifas = responseTarifas.json()
        peliculas = responsePeliculas.json()

        cine["peliculas"] = peliculas
        cine["tarifas"] = tarifas

        return render(request, 'cine.html', {"cine": cine})
    else:
        return HttpResponse("Error en el servidor")
