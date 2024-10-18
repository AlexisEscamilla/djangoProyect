from django.shortcuts import render
#Mis importaciones - Richy
import json
import requests
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.views import APIView
from .serializers import EmisionesSerializer
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Emisiones
from .serializers import EmisionesSerializer


def vector_maps (request): 
    return render(request, 'vector-maps.html')
def canada (request): 
    return render(request, 'canada.html')
def russia (request): 
    return render(request, 'russia.html')
def spain (request): 
    return render(request, 'spain.html')
def mexico (request): 
    return render(request, 'mexico.html')
def italy (request): 
    return render(request, 'italy.html')
def usa (request): 
    return render(request, 'usa.html')
def countries (request): 
    return render(request, 'countries.html')
def widgets (request): 
    return render(request, 'widgets.html')
def wishlist (request): 
    return render(request, 'wishlist.html')


@csrf_exempt
def get_gemini_answer(request):
    if request.method == 'POST':
        # Cargar el cuerpo de la solicitud como JSON
        try:
            data = json.loads(request.body)
            question = data.get('question')  # Obtener 'question' del JSON

            if not question:
                return JsonResponse({'error': 'La pregunta es obligatoria'}, status=400)

            api_url = "https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent?key=AIzaSyB-BPYppGfIWDCZuiDSRrQpJdNKxO-RRP0"
            headers = {
                'Content-Type': 'application/json',
            }
            payload = {  # Usar 'payload' para mantener la estructura correcta
                "contents": [
                    {
                        "role": "user",
                        "parts": [{"text": question}]
                    }
                ]
            }

            response = requests.post(api_url, json=payload, headers=headers)

            if response.status_code == 200:
                return JsonResponse(response.json())
            else:
                return JsonResponse({'error': 'Error al obtener una respuesta válida de la API'}, status=response.status_code)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'El cuerpo de la solicitud no es JSON válido'}, status=400)

    return JsonResponse({'error': 'Método no permitido'}, status=405)
#Mis modificaciones (Richy backend y generación de api rest)

class EmisionesAPIView(APIView):
    def get(self, request):
        # Obtén todos los registros de la base de datos
        emisiones = Emisiones.objects.all()  # Cargar los datos desde la base de datos
        
        # Serializa los datos
        serializer = EmisionesSerializer(emisiones, many=True)
        
        # Retorna la respuesta JSON
        return Response(serializer.data)
    