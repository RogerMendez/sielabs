#encoding:utf-8
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from consultas.form import ContactoForm
from django.core.mail import EmailMessage

def home(request):
    return render_to_response('base.html', context_instance=RequestContext(request))
    #return render_to_response('base.html', context_instance=RequestContext(request))

def nosotros(request):
    return  render_to_response('nosotros.html', context_instance=RequestContext(request))

def servicios(request):
    return  render_to_response('servicios.html', context_instance=RequestContext(request))

def temascursos(request):
   return  render_to_response('temascursos.html', context_instance=RequestContext(request))

def new_contacto(request):
    if request.method =='POST' :
        formulario = ContactoForm(request.POST)
        if formulario.is_valid() :
            formulario.save()
            titulo = "Mensaje desde SIELABs"
            contenido = formulario.cleaned_data['descripcion'] + "\n"
            contenido += "Comunicarse con: " + formulario.cleaned_data['email']
            correo = EmailMessage(titulo, contenido, to=['Roger.Mendez.R@gmail.com'])
            correo.send()
            return HttpResponseRedirect('/')
    else:
        formulario = ContactoForm()
    return render_to_response('consultas/new_consulta.html', {'formulario' :formulario}, context_instance=RequestContext(request))