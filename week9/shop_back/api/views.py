from django.shortcuts import render
from api.models import Category,Product
from django.http import HttpResponse,JsonResponse


# Create your views here.
def category_list(request):
    categories=Category.objects.all()
    json_categories=[c.to_json() for c in categories ]
    return JsonResponse(json_categories,safe=False,json_dumps_params={'ensure_ascii': False})

def category_detail(request,pk):
    try:
        category=Category.objects.get(id=pk)
    except Category.DoesNotExist as e:
        return JsonResponse({'error':str(e)},safe=False)

    return JsonResponse(category.to_json(),safe=False,json_dumps_params={'ensure_ascii':False})

def category_products(request,pk):
    try:
        category = Category.objects.get(id=pk)
    except Category.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False)

    products=category.product_set.all()
    json_products=[product.to_json() for product in products]
    return JsonResponse(json_products, safe=False, json_dumps_params={'ensure_ascii': False})

def product_list(request):
    products=Product.objects.all()
    json_products=[p.to_json() for p in products]
    return JsonResponse(json_products,safe=False,json_dumps_params={'ensure_ascii': False})

def product_detail(request, pk):
    try:
        product= Product.objects.get(id=pk)
    except Product.DoesNotExist as e:
        return JsonResponse({'error':str(e)}, safe=False)
    return JsonResponse(product.to_json(),safe=False,json_dumps_params={'ensure_ascii':False})
