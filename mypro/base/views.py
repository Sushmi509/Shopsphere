from django.shortcuts import render,redirect
from. models import Products,Cart
from django. db .models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.
def home(request):
    category_nav=True
    a=Products.objects.all()
#__for search___
    if 'key' in request.GET:
        key_data=request.GET['key']
        category_nav=False
        a=Products.objects.filter(Q(category__icontains=key_data) | Q(name__icontains=key_data))

# trending functionality
    if 'trending' in request.GET:
        trending_prods=Products.objects.filter(trending=1)
        a=trending_prods
        category_nav=False
# sale functionality
    if 'sale' in request.GET:
        sale_prods=Products.objects.filter(offer=1)
        a=sale_prods
        category_nav=False
  
    if request.method=='POST':
        category_data=request.POST['category']
        name_data=request.POST['name']
        desc_data=request.POST['desc']
        price_data=request.POST['price']
        img_data=request.FILES['img']
        Products.objects.create(category=category_data,name=name_data,desc=desc_data,price=price_data,image=img_data)
        return redirect('home')

    products_category=[]
    for i in a:
        if i.category not in products_category:
            products_category+=[i.category]
    
    if 'category_query' in request.GET:
        b=request.GET['category_query']
        a=Products.objects.filter(category=b)
        return render(request,'home.html',{'a':a,'prod_categories':products_category,'category_nav':category_nav})

    return render(request,'home.html',{'a':a,'prod_categories':products_category})

@login_required(login_url='login')
def add_cart(request,id):
    a=Products.objects.get(id=id)

    try:
        item_exist = Cart.objects.get(name=a.name)
        item_exist.quantity+=1
        item_exist.totalprice += item_exist.price
        item_exist.save()

    except:
        Cart.objects.create(category=a.category,name=a.name,desc=a.desc,price=a.price,image=a.image,host = request.user)
    return redirect('cartpage')

@login_required(login_url='login')
def cart_page(request):
    a=Cart.objects.all()
    return render(request,'add_cart.html',{'a':a})

@login_required(login_url='login')
def delete(request,id):
    a=Products.objects.get(id=id)
    a.delete()
    return redirect('home')

@login_required(login_url='login')

def About(request):
    return render(request,'about.html')

@login_required(login_url='login')
def Detail(request,id):
    a=Products.objects.get(id=id)
    return render(request,'about.html',{'data':a})


