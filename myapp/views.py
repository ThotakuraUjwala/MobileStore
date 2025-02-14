from django.shortcuts import render,get_object_or_404,redirect
from django.http import JsonResponse
from .models import *
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponseForbidden



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
        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "").strip()
        confirm_password = request.POST.get("confirm_password", "").strip()

        # Check if fields are empty
        if not username or not email or not password or not confirm_password:
            messages.error(request, "All fields are required.")
            return render(request, "signup.html")

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, "signup.html")

        # Check if username and email already exist
        if User.objects.filter(username=username, email=email).exists():
            messages.error(request, "An account with this username and email already exists.")
            return render(request, "signup.html")

        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists. Please choose another.")
            return render(request, "signup.html")

        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered. Try logging in.")
            return render(request, "signup.html")

        # Create new user
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()

        messages.success(request, "Account created successfully! Please log in.")
        return redirect("myapp:login")  # Redirect to login page

    return render(request, "signup.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "").strip()

        # Validate if all fields are filled
        if not username or not email or not password:
            messages.error(request, "All fields are required.")
            return render(request, "login.html")

        # Check if user exists with username and email
        if not User.objects.filter(username=username, email=email).exists():
            messages.error(request, "No account found with this username and email. Please sign up.")
            return render(request, "login.html")

        # Authenticate user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect("myapp:home")  # Redirect to home page
        else:
            messages.error(request, "Invalid password. Please try again.")
            return render(request, "login.html")

    return render(request, "login.html")


def logout_view(request):
    cart = request.session.get('cart', {})  # Preserve cart
    logout(request)  # Log out the user
    request.session['cart'] = cart  # Restore cart after logout
    request.session.modified = True  # Ensure session updates
    return redirect('myapp:home')


@login_required
def add_to_cart(request, item_id, category):
    # Fetch the item based on category
    if category == "mobile":
        item = get_object_or_404(mobiles, id=item_id)
    elif category == "laptop":
        item = get_object_or_404(laptops, id=item_id)
    elif category == "accessory":
        item = get_object_or_404(Accessories, id=item_id)
    else:
        return redirect('myapp:home')

    # Check if item already exists in the cart
    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        category=category,
        item_id=item_id,
        defaults={'name': item.name, 'price': float(item.price), 'image': item.image.url if item.image else '', 'quantity': 1}
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('myapp:cart_page')


@login_required
def cart_page(request):
    cart_items = CartItem.objects.filter(user=request.user)
    return render(request, 'cart.html', {'cart_items': cart_items})


@login_required
def remove_from_cart(request, category, item_id):
    try:
        cart_item = CartItem.objects.get(user=request.user, category=category, item_id=item_id)
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
    except CartItem.DoesNotExist:
        pass

    return redirect('myapp:cart_page')


@login_required
def place_order(request, item_id, category):
    user = request.user

    if category == "mobile":
        item = get_object_or_404(mobiles, id=item_id)
    elif category == "laptop":
        item = get_object_or_404(laptops, id=item_id)
    elif category == "accessory":
        item = get_object_or_404(Accessories, id=item_id)
    else:
        return redirect('myapp:home')

    # Save the order in Order model
    Order.objects.create(
        user=user,
        name=item.name,
        category=category,
        price=item.price,
        quantity=1
    )

    # Send confirmation email
    subject = "Order Confirmation - Your Purchase is Successful!"
    message = f"Dear {user.username},\n\nYour order has been placed successfully!\n\nOrder Details:\n{item.name} - ₹{item.price} (Qty: 1)\n\nThank you for shopping with us!\n\nBest Regards,\nOnline Mobile Store Team"
    send_mail(subject, message, 'lomamobiles15@gmail.com', [user.email], fail_silently=False)

    return redirect('myapp:order_success')


@login_required
def checkout(request):
    user = request.user
    cart_items = CartItem.objects.filter(user=user)

    if not cart_items:
        return redirect('myapp:cart_page')

    order_details = "\n".join([
        f"{item.name} - ₹{item.price} (Qty: {item.quantity})"
        for item in cart_items
    ])

    for item in cart_items:
        Order.objects.create(
            user=user,
            name=item.name,
            category=item.category,
            price=item.price,
            quantity=item.quantity
        )

    # Send confirmation email
    subject = "Order Confirmation - Your Purchase is Successful!"
    message = f"Dear {user.username},\n\nYour order has been placed successfully!\n\nOrder Details:\n{order_details}\n\nThank you for shopping with us!\n\nBest Regards,\nOnline Mobile Store Team"
    send_mail(subject, message, 'lomamobiles15@gmail.com', [user.email], fail_silently=False)

    cart_items.delete()

    return redirect('myapp:order_success')


@login_required
def owner_orders(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden("Access Denied")

    orders = Order.objects.all()  
    return render(request, "owner_orders.html", {"orders": orders})


def order_success(request):
    return render(request, 'order_success.html')
