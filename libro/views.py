from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from .models import Libro
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
class LibrosView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def get(self, request, id=0):
        if id > 0:
            libros = list(Libro.objects.filter(id=id).values())
            if len(libros) > 0:
                libro = libros[0]
                datos = {'message': "Success", 'libros': libro}
            else:
                datos = {'message': "Libro not found"}
            return JsonResponse(datos)
        else:
            status_param = request.GET.get('status', None)
            if status_param is not None:
                if status_param.lower() == 'true':
                    libros = list(Libro.objects.filter(status=True).values())
                elif status_param.lower() == 'false':
                    libros = list(Libro.objects.filter(status=False).values())
                else:
                    datos = {'message': "Invalid status parameter"}
                    return JsonResponse(datos)

                if len(libros) > 0:
                    datos = {'message': "Success", 'libros': libros}
                else:
                    datos = {'message': "Libros not found"}
            else:
                libros = list(Libro.objects.values())
                if len(libros) > 0:
                    datos = {'message': "Success", 'libros': libros}
                else:
                    datos = {'message': "Libros not found"}

            return JsonResponse(datos)




        
    # def get(self, request, id=0):
    #     if id>0:
    #         libros = list(Libro.objects.filter(id=id).values())
    #         if len(libros)>0:
    #             libro = libros[0]
    #             datos={'message':"Success", 'libros': libro}
    #         else:
    #             datos={'message': "libros not found"}
    #         return JsonResponse(datos)
    #     else:
    #         libros = list(Libro.objects.values())
    #         if len(libros)>0:
    #             datos={'message':"Success", 'libros': libros}
    #         else: 
    #             datos={'message': "libros not found"}
            
    #         return JsonResponse(datos)
    
    def post(self, request):
        jd = json.loads(request.body)
        Libro.objects.create(titulo = jd['titulo'],autor = jd['autor'], editorial = jd['editorial'], ncapitulos = jd['ncapitulos'], npaginas = jd['npaginas'], isbn = jd['isbn'], actual = jd['actual'], status = jd['status'] )
        datos = {'message':"Success"}
        return JsonResponse(datos)
    
    def put(self, request, id):
        jd = json.loads(request.body)
        libros = list(Libro.objects.filter(id=id).values())
        if len(libros)>0:
            user = Libro.objects.get(id=id)
            user.actual = jd['actual']
            user.status = jd['status']
            user.save()
            datos = {'message':"Success"}
        else:
            datos={'message': "Libros not found"}
        return JsonResponse(datos)
    
    def delete(self, request, id):
        libros = list(Libro.objects.filter(id=id).values())
        if len(libros)>0:
            Libro.objects.filter(id=id).delete()
            datos = {'message':"Success"}
        else:
            datos={'message': "Usuarios not found"}
        return JsonResponse(datos)