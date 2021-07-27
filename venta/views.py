from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'venta/index.html')


def compra(request):
    return render(request,'venta/compra.html')

def arriendo(request):
    return render(request,'venta/arriendo.html')

def seguimiento(request):
    return render(request,'venta/seguimiento.html')


def login(request):
    return render(request,'venta/login.html')


def check(request):
    return render(request,'venta/check.html')

def check_contraseña(request):
    return render(request,'venta/check_contraseña.html')

def recuperar_contraseña(request):
    return render(request,'venta/recuperar_contraseña.html')

def check_usuario(request):
    return render(request,'venta/check_usuario.html')

def crear_cuenta(request):
    return render(request,'venta/Crear_Cuenta.html')
