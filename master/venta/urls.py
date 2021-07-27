
from django.urls import path ,include
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('index',views.index,name="index"),
    path('compra',views.compra,name="compra"),
    path('arriendo',views.arriendo,name="arriendo"),
    path('seguimiento',views.seguimiento,name="seguimiento"),
    path('login',views.login,name="login"),
    path('check',views.check,name="check"),
    path('check_contraseña',views.check_contraseña,name="check_contraseña"),
    path('recuperar_contraseña',views.recuperar_contraseña,name="recuperar_contraseña"),
    path('check_usuario',views.check_usuario,name="check_usuario"),
    path('Crear_Cuenta',views.crear_cuenta,name="Crear_Cuenta"),
]
