from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import *
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignupForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def home(request):
    slidesdata = Slides.objects.all()
    bestselling = mobiles.objects.filter(is_bestselling=True)
    brands = Brand.objects.all()
    offerdata=Offer.objects.all()
    bestlap=laptops.objects.filter(is_bestselling=True)
    lapoff=laptops.objects.filter(is_deals=True)
    lapbrands = lapBrand.objects.all()
    new_accessories = Accessories.objects.filter(Newly_lanched=True)
    return render(request, 'home.html', {'slidesdata': slidesdata, 'bestselling': bestselling, 'brands': brands,'bestlap':bestlap,'lapoff':lapoff,'moboff':offerdata,'lapbrands':lapbrands,'new_accessories': new_accessories })

def brand_view(request, brand_name):
    brand = Brand.objects.get(name__iexact=brand_name)
    mobiles_by_brand = mobiles.objects.filter(brand=brand)
    return render(request, 'brand_mobiles.html', {'mobiles': mobiles_by_brand, 'brand': brand})

def brand_mobiles_view(request, brand_name):
    brand = Brand.objects.get(name=brand_name)  # Assuming you have a Brand model
    mobiles_list = mobiles.objects.filter(brand=brand)
    return render(request, 'brand_mobiles.html', {'brand': brand, 'mobiles': mobiles_list})


def brand_laptops_view(request, brand_name):
    brand = get_object_or_404(lapBrand, name__iexact=brand_name)  # Case-insensitive search
    laptops_list = laptops.objects.filter(brand=brand)
    return render(request, 'brand_laptops.html', {'brand': brand, 'laptops': laptops_list})


def lapbrand_view(request, brand_name):
    brand = lapBrand.objects.get(name__iexact=brand_name)
    laptops_by_brand = laptops.objects.filter(brand=brand)
    return render(request, 'brand_laptops.html', {'laptops': laptops_by_brand, 'lapbrand': brand})

def mobiledataview(request, id):
    mobiledata = [mobiles.objects.get(id=id)]
    return render(request, 'mobiledata.html', {'mobiledata': mobiledata})


def lapdataview(request, id):
    lapdata = [laptops.objects.get(id=id)]
    return render(request, 'lapdata.html', {'lapdata': lapdata})

def allmobiles(request):
    data = mobiles.objects.all()
    return render(request, 'allmobiles.html', {'alldata': data})

def all_laptops(request):
    data = laptops.objects.all()
    return render(request, 'laptops.html', {'alldata': data})

def accessories(request):
    accessories_data = Accessories.objects.all()  # Retrieve all accessories from the database
    return render(request, 'accessories.html', {'accessories_data': accessories_data})


def accessoriesview(request, id):
    accessoriesdata = [Accessories.objects.get(id=id)]
    return render(request, 'accessoriesdata.html', {'accessoriesdata': accessoriesdata})


def search(request):
    query = request.GET.get("q", "").strip()

    mobile= mobiles.objects.none()  # Instead of []
    accessorie = Accessories.objects.none()
    laptop = laptops.objects.none()

    if query:
        mobile = mobiles.objects.filter(name__icontains=query)
        accessorie = Accessories.objects.filter(name__icontains=query)
        laptop = laptops.objects.filter(name__icontains=query)

    return render(request, "search_results.html", {
        "query": query,
        "mobile": mobile,
        "accessorie": accessorie,
        "laptop": laptop,
    })


def signup_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        # Check if passwords match
        if password != confirm_password:
            return render(request, "signup.html", {"error": "Passwords do not match"})

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            return render(request, "signup.html", {"error": "User account already exists"})

        # Create new user
        user = User.objects.create_user(username=username, password=password)
        user.save()

        return redirect("myapp:login")  # Redirect to login after successful signup

    return render(request, "signup.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect("myapp:home")  # Redirect to home page
        else:
            return render(request, "login.html", {"error": "Invalid username or password"})

    return render(request, "login.html")



def logout_view(request):
    logout(request)
    return redirect("myapp:home")  # Redirect to home after logout


def add_to_cart(request, item_id, category):
    cart = request.session.get('cart', {})

    # Add item to the cart (or increase quantity)
    if item_id in cart:
        cart[item_id]['quantity'] += 1
    else:
        cart[item_id] = {'category': category, 'quantity': 1}

    request.session['cart'] = cart  # Save cart in session
    request.session.modified = True  # Mark session as modified

    messages.success(request, "Item added to cart!")  # Optional message
    return redirect('myapp:cart')  # Redirect to cart page

def cart_view(request):
    cart = request.session.get('cart', {})
    return render(request, 'cart.html', {'cart': cart})

def remove_from_cart(request, item_id):
    cart = request.session.get('cart', {})
    
    # Remove item from cart if it exists
    if str(item_id) in cart:
        del cart[str(item_id)]
        request.session['cart'] = cart  # Save the updated cart in session

    return redirect('cart')  # Redirect back to the cart page