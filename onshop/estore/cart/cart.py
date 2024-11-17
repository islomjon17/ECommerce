class Cart():
    def __init__(self, request):
        self.session = request.session
        
        
        cart = self.session.get('session_key')
        
        
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}
            
        self.cart = cart
        
    def add(self, product):
        product_id = str(product.id)
        
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = {'price': str(product.price)}
            
        self.session.modified = True
        
    def __len__(self):
        return len(self.cart)


# class Cart:
#     def __init__(self, request):
#         if not hasattr(request, 'session'):
#             raise ValueError("Request object must have a session attribute")   
#         self.session = request.session
#         cart = self.session.get('cart', {})
#         if 'cart' not in self.session:
#             self.session['cart'] = {}
#         self.cart = self.session['cart']
    
#     def add(self, product):
#         product_id = str(product.id)
#         if product_id in self.cart:
#             self.cart[product_id]['quantity'] = self.cart[product_id].get('quantity', 1) + 1
#         else:
#             self.cart[product_id] = {'price': str(product.price), 'quantity': 1}
        
#         self.session.modified = True
