from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from appCRUD.forms import * 
from appCRUD.models import * 
# Create your views here.


def listar(request):
    form = FormFiltroLista(request.GET)
    listar_usuario = UsuarioCRUD.objects.all()

    if form.is_valid():
        codCA = form.cleaned_data.get('codCA')
        nombre = form.cleaned_data.get('nombre')
        if codCA:
            listar_usuario = listar_usuario.filter(codCA=codCA)
        if nombre:
            listar_usuario = listar_usuario.filter(nombre__icontains=nombre)

    return render(request, 'templatesAPP/index.html', {'form': form, 'listar_usuario': listar_usuario})


def agregar(request):  
    if request.method == "POST":  
        form = UsuarioForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('listar')  
            except:  
                pass
    else:  
        form = UsuarioForm()  
    return render(request,'templatesAPP/agregar.html',{'form':form})  


def modificar_usuario(request, id):
    usuario = get_object_or_404(UsuarioCRUD, id=id)
    
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('listar')  # Cambia esto con el nombre de tu vista de listado
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'templatesApp/modificar.html', {'form': form})


def eliminar(request, id):
    usuario = get_object_or_404(UsuarioCRUD, id=id)
    usuario.delete()
    # Agrega un mensaje de éxito para notificar al usuario que la eliminación fue exitosa
    messages.success(request, 'Usuario eliminado exitosamente.')
    return redirect('listar')

