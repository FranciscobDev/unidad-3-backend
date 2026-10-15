def carrito_context(request):
    carrito = request.session.get('carrito',{})
    total_items = sum(item.get('cantidad0', 0) for item in carrito.values())
    return {
        'carrito_total_item' : total_items
    }
