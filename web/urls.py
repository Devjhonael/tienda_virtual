from django.urls import path
from django.contrib.auth import views as auth_views


from . import views

app_name = 'web'

urlpatterns = [
    path('', views.index,name='index'),

    path('productosPorCategoria/<int:categoria_id>',views.productosPorCategoria,name='productosPorCategoria'),
    
    path('productosPorNombre',views.productosPorNombre,name='productosPorNombre'),
    
    path('producto/<int:producto_id>',views.productoDetalle,name='producto'),
    
    # ruta de carrito de compras
    path('carrito',views.carrito,name='carrito'),
    path('agregarCarrito/<int:producto_id>',views.agregarCarrito,name='agregarCarrito'),
    path('eliminarProductoCarrito/<int:producto_id>',views.eliminarProductoCarrito,name='eliminarProductoCarrito'),
    path('limpiarCarrito',views.limpiarCarrito,name='limpiarCarrito'),
    
    # para crear cuentas
    path('crearUsuario',views.crearUsuario,name='crearUsuario'),
    path('cuenta',views.cuentaUsuario,name='cuentaUsuario'),
    path('actualizarCliente',views.actualizarCliente,name='actualizarCliente'),
    path('login',views.loginUsuario,name='loginUsuario'),
    path('logout',views.logoutUsuario,name='logoutUsuario'),
    path('registrarPedido',views.registrarPedido,name='registrarPedido'),
    path('confirmarPedido',views.confirmarPedido,name='confirmarPedido'),
    path('gracias',views.gracias,name='gracias'),

] 
