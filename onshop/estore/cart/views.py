from django.shortcuts import render, get_object_or_404
from .cart import Cart
from shop1.models import Product

from django.http import JsonResponse

# Create your views here.


def cart_summary(request):
    return render(request, "cart_summary.html", {})



# def cart_add(request):
#     cart  = Cart(request)
    
#     if request.POST.get('action') == 'POST':
#         product_id = int(request.POST.get("product_id"))
        
#         product = get_object_or_404(Product, id=product_id)
        
#         cart.add(product=product)
        
#         response = JsonResponse({'Product Name': product.name})
#         return response
        

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .cart import Cart  # Assuming you have a custom Cart class

def cart_add(request):
    cart = Cart(request)
    if request.method == 'POST' and request.POST.get('action') == 'post':
        try:
            product_id = int(request.POST.get("product_id"))
        except (ValueError, TypeError):
            return JsonResponse({'error': 'Invalid product_id'}, status=400)

        product = get_object_or_404(Product, id=product_id)

        cart.add(product=product)
        return JsonResponse({
            'success': True,
            'product_name': product.name,
            'message': f'{product.name} has been added to the cart.',
        })

    return JsonResponse({'error': 'Invalid request'}, status=400)


def cart_delete(request):
    pass



def cart_update(request):
    pass