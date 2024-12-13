# creamos este carrito para crear session mientras hagamos las compras

class Cart:
    
    def __init__(self,request):
        self.request = request
        # obtiene la session del navegador
        self.session = request.session
        
        # invocar una variable de session
        cart = self.session.get("cart")

        # creando una variable de session
        montoTotal = self.session.get("cartMontoTotal")
        if not cart:
            cart = self.session['cart'] = {}
            montoTotal = self.session["cartMontoTotal"] = "0"
            
        self.cart = cart
        self.montoTotal = float(montoTotal)
        

        # para agregar un carrito de compra y que datos va necesitar
    def add(self,producto,cantidad):
        # pregunta si la clave no se encuentra dentro de card entonces add
        if str(producto.id) not in self.cart.keys():
            self.cart[producto.id] = {
                "producto_id":producto.id,
                "nombre":producto.nombre,
                "cantidad":cantidad,
                "precio":str(producto.precio),
                "imagen":producto.imagen.url,
                "categoria":producto.categoria.nombre,
                "subtotal":str(cantidad * producto.precio)
            }
        else:
            #actualizamos el producto en el carrito
            for key,value in self.cart.items():
                if key == str(producto.id):
                    value["cantidad"] = str(int(value["cantidad"]) + cantidad)
                    value["subtotal"] = str(float(value["cantidad"]) * float(value["precio"]))
                    break
        
        self.save()
    
    # para eliminar productos del carrito de compra
    def delete(self,producto):
        producto_id = str(producto.id)
        if producto_id in self.cart:
            del self.cart[producto_id]
            self.save()
    
    # para limpiar el carrito
    def clear(self):
        self.session["cart"] = {}
        self.session["cartMontoTotal"] = "0"
    

    # para guardar el carrito 
    def save(self):
        """ guarda cambios en el carrito de compras recien calculo el total"""
        
        montoTotal = 0
        
        for key,value in self.cart.items():
            montoTotal += float(value["subtotal"])
            
        # actualizas el monto
        self.session["cartMontoTotal"] = montoTotal
        self.session["cart"] = self.cart
        self.session.modified = True