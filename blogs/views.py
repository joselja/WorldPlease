from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from blogs.models import Blog




class BlogListView(View):

    def get(self, request):
        """
        Muestra el listado de los últimos blogs
        :param request: objeto HttpRequest
        :return: HttpResponse
        """

        # Recuperamos todos los blogs de la DB
        blogs = Blog.objects.filter(active=True).order_by('-creation_date')

        # Creamos contexto
        messages.info(request,'Listado de blogs')
        context = {'items': blogs}

        # Devolver la respuesta utilizando una plantilla
        return render(request, 'blogs/list.html', context)
