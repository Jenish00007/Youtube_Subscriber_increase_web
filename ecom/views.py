from django.shortcuts import render,redirect,reverse
from . import forms,models
from django.http import HttpResponseRedirect,HttpResponse
from django.core.mail import send_mail
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib import messages
from django.conf import settings
from . models import *
import pywhatkit as kit




from django.http import  JsonResponse
from django.views.decorators.csrf import csrf_protect


import json

def shop(request):
    category=Catagory.objects.all()
    Trending_products=Product.objects.filter(trending=1)
    Latest_products=Product.objects.filter(latest=1)
   

    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        counter=product_ids.split('|')
        product_count_in_cart=len(set(counter))
    else:
        product_count_in_cart=0
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'shop/index.html',{'category':category,'Trending_products':Trending_products,'Latest_products':Latest_products,'product_count_in_cart':product_count_in_cart})


def test1(request):
  
    return render(request,'ecom/customerlogin.html')

@login_required(login_url='customerlogin')
def collections(request):
  catagory=Catagory.objects.filter(status=0)
  customer = Customer.objects.get(user_id=request.user.id)
  products=Product.objects.filter(status=0)
  return render(request,"shop/category.html",{"products":products})
  
def collectionsview(request,name):
    try: 
        customer = Customer.objects.get(user_id=request.user.id)
        if(Catagory.objects.filter(name=name,status=0)):
              products=Product.objects.filter(category__name=name)
              customer = Customer.objects.get(user_id=request.user.id)
              return render(request,"shop/product-page.html",{'customer':customer,"products":products,"category_name":name})
        else:
            messages.warning(request,"No Such Catagory Found")
            return redirect('collections')
          
    except Customer.DoesNotExist:
        messages.error(request, "Customer does not exist.")
        return redirect('customerlogin')
       
 
@login_required(login_url='customerlogin')
def product_details(request, cname, pname):
    try:
        customer = Customer.objects.get(user_id=request.user.id)
        trending_products = Product.objects.filter(trending=1)
        if Catagory.objects.filter(name=cname, status=0).exists():
            if Product.objects.filter(name=pname, status=0).exists():
                products = Product.objects.filter(name=pname, status=0).first()
                return render(request, "shop/product-two-details.html", {'customer': customer, "products": products, 'trending_products': trending_products})
            else:
                messages.error(request, "No such product found.")
                return redirect('collections')
        else:
            messages.error(request, "No such category found.")
            return redirect('collections')
    except Customer.DoesNotExist:
        messages.error(request, "Customer does not exist.")
        return redirect('customerlogin')
    

#for showing login button for admin(by sumit)
def adminclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return HttpResponseRedirect('adminlogin')


def customer_signup_view(request):
    userForm=forms.CustomerUserForm()
    customerForm=forms.CustomerForm()
    mydict={'userForm':userForm,'customerForm':customerForm}
    if request.method=='POST':
        userForm=forms.CustomerUserForm(request.POST)
        customerForm=forms.CustomerForm(request.POST,request.FILES)
        if userForm.is_valid() and customerForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            customer=customerForm.save(commit=False)
            customer.user=user
            customer.save()
            my_customer_group = Group.objects.get_or_create(name='CUSTOMER')
            my_customer_group[0].user_set.add(user)
        return HttpResponseRedirect('customerlogin')
    return render(request,'ecom/customersignup.html',context=mydict)

#-----------for checking user iscustomer
def is_customer(user):
    return user.groups.filter(name='CUSTOMER').exists()



#---------AFTER ENTERING CREDENTIALS WE CHECK WHETHER USERNAME AND PASSWORD IS OF ADMIN,CUSTOMER
def afterlogin_view(request):
    if is_customer(request.user):
        return redirect('customer-home')
    else:
        return redirect('admin-dashboard')

#---------------------------------------------------------------------------------
#------------------------ ADMIN RELATED VIEWS START ------------------------------
#---------------------------------------------------------------------------------
@login_required(login_url='adminlogin')
def admin_dashboard_view(request):
    # for cards on dashboard
    customercount=Customer.objects.all().count()
    productcount=Product.objects.all().count()
    ordercount=Orders.objects.all().count()

    # for recent order tables
    orders=Orders.objects.all()
    ordered_products=[]
    ordered_bys=[]
    for order in orders:
        ordered_product=Product.objects.all().filter(id=order.product.id)
        ordered_by=Customer.objects.all().filter(id = order.customer.id)
        ordered_products.append(ordered_product)
        ordered_bys.append(ordered_by)

    mydict={
    'customercount':customercount,
    'productcount':productcount,
    'ordercount':ordercount,
    'data':zip(ordered_products,ordered_bys,orders),
    }
    return render(request,'ecom/admin1.html',context=mydict)

# admin-dashboard
# admin view customer table
@login_required(login_url='adminlogin')
def view_customer_view(request):
    customers=Customer.objects.all()
    customer = Customer.objects.get(user_id=request.user.id)
    return render(request,'ecom/customers_new.html',{'customer':customer,'customers':customers})

# admin delete customer
@login_required(login_url='adminlogin')
def delete_customer_view(request,pk):
    customer=Customer.objects.get(id=pk)
    user=User.objects.get(id=customer.user_id)
    user.delete()
    customer.delete()
    return redirect('view-customer')


@login_required(login_url='adminlogin')
def update_customer_view(request,pk):
    customer=Customer.objects.get(id=pk)
    user=User.objects.get(id=customer.user_id)
    userForm=forms.CustomerUserForm(instance=user)
    customerForm=forms.CustomerForm(request.FILES,instance=customer)
    mydict={'userForm':userForm,'customerForm':customerForm}
    if request.method=='POST':
        userForm=forms.CustomerUserForm(request.POST,instance=user)
        customerForm=forms.CustomerForm(request.POST,instance=customer)
        if userForm.is_valid() and customerForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            customerForm.save()
            return redirect('view-customer')
    return render(request,'ecom/customer_update_new.html',context=mydict)

# admin view the product
@login_required(login_url='adminlogin')
def admin_products_view(request):
    products=Product.objects.all()
    return render(request,'ecom/product_new.html',{'products':products})


# admin add product by clicking on floating button
@login_required(login_url='adminlogin')
def admin_add_product_view(request):
    productForm=forms.ProductForm()
    if request.method=='POST':
        productForm=forms.ProductForm(request.POST, request.FILES)
        if productForm.is_valid():
            productForm.save()
        return HttpResponseRedirect('admin-products')
    return render(request,'ecom/add_product_new.html',{'productForm':productForm})


@login_required(login_url='adminlogin')
def delete_product_view(request,pk):
    product=Product.objects.get(id=pk)
    product.delete()
    return redirect('admin-products')


@login_required(login_url='adminlogin')
def update_product_view(request,pk):
    product=Product.objects.get(id=pk)
    productForm=forms.ProductForm(instance=product)
    if request.method=='POST':
        productForm=forms.ProductForm(request.POST,request.FILES,instance=product)
        if productForm.is_valid():
            productForm.save()
            return redirect('admin-products')
    return render(request,'ecom/update_product_new.html',{'productForm':productForm})


@login_required(login_url='adminlogin')
def admin_view_booking_view(request):
    orders=Orders.objects.all()
    ordered_products=[]
    ordered_bys=[]
    for order in orders:
        ordered_product=Product.objects.all().filter(id=order.product.id)
        ordered_by=Customer.objects.all().filter(id = order.customer.id)
        ordered_products.append(ordered_product)
        ordered_bys.append(ordered_by)
    return render(request,'ecom/orders_new.html',{'data':zip(ordered_products,ordered_bys,orders)})

 
@login_required(login_url='adminlogin')
def delete_order_view(request,pk):
    order=Orders.objects.get(id=pk)
    order.delete()
    return redirect('admin-view-booking')

# for changing status of order (pending,delivered...)
@login_required(login_url='adminlogin')
def update_order_view(request,pk):
    order=Orders.objects.get(id=pk)
    orderForm=forms.OrderForm(instance=order)
    if request.method=='POST':
        orderForm=forms.OrderForm(request.POST,instance=order)
        if orderForm.is_valid():
            orderForm.save()
            return redirect('admin-view-booking')
    return render(request,'ecom/update_order.html',{'orderForm':orderForm})


# admin view the feedback
@login_required(login_url='adminlogin')
def view_feedback_view(request):
    feedbacks=Feedback.objects.all().order_by('-id')
    return render(request,'ecom/view_feedback.html',{'feedbacks':feedbacks})



#---------------------------------------------------------------------------------
#------------------------ PUBLIC CUSTOMER RELATED VIEWS START ---------------------
#---------------------------------------------------------------------------------





def favviewpage(request):
  if request.user.is_authenticated:
    fav=Favourite.objects.filter(user=request.user)
    customer = Customer.objects.get(user_id=request.user.id)
  
    return render(request,"shop/fav.html",{'customer':customer,"fav":fav})
  else:
    return redirect("")
 
def remove_fav(request,fid,item_id):
  item=Favourite.objects.get(id=fid)
  item.delete()
  return redirect("/favviewpage")
 

def fav_page(request, item_id):
   if request.headers.get('x-requested-with') == 'XMLHttpRequest':
      if request.user.is_authenticated:
         data = json.load(request)
         product_id = data['pid']
         product_status = Product.objects.get(id=product_id)
         fav_count = Favourite.objects.filter(item_id=item_id)
         print(fav_count)
         if product_status:
            if Favourite.objects.filter(user=request.user.id, product_id=product_id):
               return JsonResponse({'status': 'Product Already in Favourite'}, status=200)
            else:
               Favourite.objects.create(user=request.user, product_id=product_id)
               return JsonResponse({'status': 'Product Added to Favourite'}, status=200)
      else:
         return JsonResponse({'status': 'Login to Add Favourite'}, status=200)
   else:
      return JsonResponse({'status': 'Invalid Access'}, status=200)




def navbar(request):
  customer = Customer.objects.get(user_id=request.user.id)
  return render(request,'ecom/customer_navbar.html',{'customer':customer})


def search_view(request):
    # whatever user write in search box we get in query
    query = request.GET['query']
    products=Product.objects.all().filter(name__icontains=query)
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        counter=product_ids.split('|')
        product_count_in_cart=len(set(counter))
    else:
        product_count_in_cart=0

    # word variable will be shown in html when user click on search button
    word="Searched Result :"

    if request.user.is_authenticated:
        return render(request,'ecom/customer_home.html',{'products':products,'word':word,'product_count_in_cart':product_count_in_cart})
    





# any one can add product to cart, no need of signin
@login_required(login_url='customerlogin')
def add_to_cart_view(request,pk):
    products=Product.objects.all()
    category=Catagory.objects.all()
    Trending_products=Product.objects.filter(trending=1)
    Latest_products=Product.objects.filter(latest=1)
    customer = Customer.objects.get(user_id=request.user.id)


    product_qty = int(request.POST.get('quantity', 1)) 
   
    #for cart counter, fetching products ids added by customer from cookies
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        counter=product_ids.split('|')
        product_count_in_cart=len(set(counter))
    else:
        product_count_in_cart=1

    response = render(request, 'shop/index.html',{'customer':customer,'Latest_products':Latest_products,'Trending_products':Trending_products,'category':category,'products':products,'product_count_in_cart':product_count_in_cart})

    #adding product id to cookies
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        if product_ids=="":
            product_ids=str(pk)
        else:
            product_ids=product_ids+"|"+str(pk)
        response.set_cookie('product_ids', product_ids)
    else:
        response.set_cookie('product_ids', pk)

    product=Product.objects.get(id=pk)
    messages.info(request, product.name + ' added to cart successfully!')

    return response




# for checkout of cart
def cart_view(request):

    #for cart counter
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        counter=product_ids.split('|')
        product_count_in_cart=len(set(counter))
    else:
        product_count_in_cart=0

    # fetching product details from db whose id is present in cookie
    products=None
    total=0
    gst=0
    Shiping_charge=0
    producttotal=0
    grand_total=0
    product_qty =1
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        
        if product_ids != "":
            product_id_in_cart=product_ids.split('|')
            products=Product.objects.all().filter(id__in = product_id_in_cart)
            
            #for total price shown in cart
            
            for p in products:
                Product_qty = int(request.POST.get('quantity', 1)) 
                
                producttotal=p.selling_price*Product_qty
                total=total+p.selling_price
                
                gst=gst+p.gst
                gst =gst+p.gst * int(18 / 100)
                Shiping_charge=0
                grand_total= total+gst+Shiping_charge
    return render(request,'shop/cart.html',{'product_qty':product_qty,'Shiping_charge':Shiping_charge,'gst':gst,'products':products,'total':total,'product_count_in_cart':product_count_in_cart,'producttotal':producttotal,'grand_total':grand_total})



@login_required(login_url='customerlogin')
def remove_from_cart_view(request, pk):
    # Check if 'product_ids' cookie exists
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        product_id_in_cart = product_ids.split('|')
        
        # Remove the product ID from the list
        if str(pk) in product_id_in_cart:
            product_id_in_cart.remove(str(pk))
        
        # Update the cookie value
        value = '|'.join(product_id_in_cart)
        response = redirect('cart')  # Redirect to the cart page
        
        # Set the updated 'product_ids' cookie value
        response.set_cookie('product_ids', value)
        return response
    
    # If 'product_ids' cookie doesn't exist, simply redirect to the cart page
    return redirect('cart')


def send_feedback_view(request):
    feedbackForm=forms.FeedbackForm()
    if request.method == 'POST':
        feedbackForm = forms.FeedbackForm(request.POST)
        if feedbackForm.is_valid():
            feedbackForm.save()
            return render(request, 'ecom/feedback_sent.html')
    return render(request, 'ecom/send_feedback.html', {'feedbackForm':feedbackForm})


#---------------------------------------------------------------------------------
#------------------------ CUSTOMER RELATED VIEWS START ------------------------------
#---------------------------------------------------------------------------------
@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def customer_home_view(request):
    category=Catagory.objects.all()
    Trending_products=Product.objects.filter(trending=1)
    Latest_products=Product.objects.filter(latest=1)
    customer = Customer.objects.get(user_id=request.user.id)
    products=Product.objects.all()
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        counter=product_ids.split('|')
        product_count_in_cart=len(set(counter))
    else:
        product_count_in_cart=0
    return render(request,'shop/index.html',{'customer':customer,'Latest_products':Latest_products,'Trending_products':Trending_products,'category':category,'products':products,'product_count_in_cart':product_count_in_cart})






@login_required(login_url='customerlogin')
def customer_address_view(request):
    customer = Customer.objects.get(user_id=request.user.id)
    total = 0
    shipping_charge = 0
    grand_total = 0
    product_in_cart = False
    product_count_in_cart = 0
    gst=0
    products = []

    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        if product_ids != "":
            product_in_cart = True
            product_count_in_cart = len(set(product_ids.split('|')))
            product_id_in_cart = product_ids.split('|')
            products = Product.objects.filter(id__in=product_id_in_cart)
            for product in products:
                product_qty = 1
                product_total = product.selling_price * product_qty
                total += product_total
                total += product.gst
                gst+= product.gst
                total += product.gst * int(18 / 100)
            shipping_charge = 0
            grand_total = total + shipping_charge

    addressForm = forms.AddressForm()
  

    if request.method == 'POST':
        addressForm = forms.AddressForm(request.POST)
        if addressForm.is_valid():
            email = addressForm.cleaned_data['Email']
            mobile = addressForm.cleaned_data['Mobile']
            address = addressForm.cleaned_data['Address']

            if request.POST.get('payment_method') == 'gpay':
                message = "Payment Method: Online"
                response = render(request, 'ecom/payment_success.html', {'grand_total': grand_total})
                response.set_cookie('email', email)
                response.set_cookie('mobile', mobile)
                response.set_cookie('address', address)
                return response

     

    return render(request, 'ecom/customer_address.html', {
        'customer': customer,
        'products': products,
        'grand_total': grand_total,
        'shipping_charge': shipping_charge,
        'gst':gst,
        'total': total,
        'addressForm': addressForm,
       
        'product_in_cart': product_in_cart,
        'product_count_in_cart': product_count_in_cart
    })


# here we are just directing to this view...actually we have to check whther payment is successful or not
#then only this view should be accessed
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Customer, Product, Orders

@login_required(login_url='customerlogin')
def payment_success_view(request):
    customer = Customer.objects.get(user_id=request.user.id)
    products = None
    email = None
    mobile = None
    address = None
    order_status = None

    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        if product_ids != "":
            product_id_in_cart = product_ids.split('|')
            products = Product.objects.filter(id__in=product_id_in_cart)

    if 'email' in request.COOKIES:
        email = request.COOKIES['email']
    if 'mobile' in request.COOKIES:
        mobile = request.COOKIES['mobile']
    if 'address' in request.COOKIES:
        address = request.COOKIES['address']

    if 'payment_method' in request.COOKIES:
        payment_method = request.COOKIES['payment_method']
        if payment_method == 'gpay':
            order_status = 'GPay'
        elif payment_method == 'cash_on_delivery':
            order_status = 'Cash on Delivery'

    for product in products:
        Orders.objects.create(
            customer=customer,
            product=product,
            status=order_status,
            email=email,
            mobile=mobile,
            address=address
        )

    response = render(request, 'ecom/payment_success.html')
    response.delete_cookie('product_ids')
    response.delete_cookie('email')
    response.delete_cookie('mobile')
    response.delete_cookie('address')
    response.delete_cookie('payment_method')
    return response




@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def my_order_view(request):
    
    customer=Customer.objects.get(user_id=request.user.id)
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        counter=product_ids.split('|')
        product_count_in_cart=len(set(counter))
    else:
        product_count_in_cart=0
    
   
    
    fav=Favourite.objects.filter(user=request.user)

    if 'fav' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        counter=product_ids.split('|')
        product_count_in_fav=len(set(counter))
    else:
        product_count_in_fav=0   
    orders=Orders.objects.all().filter(customer_id = customer)
    ordered_products=[]
    for order in orders:
        ordered_product=Product.objects.all().filter(id=order.product.id)
        ordered_products.append(ordered_product)

    return render(request,'ecom/my_order.html',{'data':zip(ordered_products,orders),'customer':customer,'product_count_in_cart':product_count_in_cart,'product_count_in_fav':product_count_in_fav})
 



# @login_required(login_url='customerlogin')
# @user_passes_test(is_customer)
# def my_order_view2(request):

#     products=models.Product.objects.all()
#     if 'product_ids' in request.COOKIES:
#         product_ids = request.COOKIES['product_ids']
#         counter=product_ids.split('|')
#         product_count_in_cart=len(set(counter))
#     else:
#         product_count_in_cart=0
#     return render(request,'ecom/my_order.html',{'products':products,'product_count_in_cart':product_count_in_cart})    



#--------------for discharge patient bill (pdf) download and printing
import io
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse


def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = io.BytesIO()
    pdf = pisa.pisaDocument(io.BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return

@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def download_invoice_view(request,orderID,productID):
    order=Orders.objects.get(id=orderID)
    product=Product.objects.get(id=productID)
    mydict={
        'orderDate':order.order_date,
        'customerName':request.user,
        'customerEmail':order.email,
        'customerMobile':order.mobile,
        'shipmentAddress':order.address,
        'orderStatus':order.status,

        'productName':product.name,
        'productImage':product.product_image,
        'productPrice':product.price,
        'productDescription':product.description,


    }
    return render_to_pdf('ecom/download_invoice.html',mydict)






@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def my_profile_view(request):
    customer=Customer.objects.get(user_id=request.user.id)
    return render(request,'ecom/my_order.html',{'customer':customer})


@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def edit_profile_view(request):
    customer=Customer.objects.get(user_id=request.user.id)
    user=User.objects.get(id=customer.user_id)
    userForm=forms.CustomerUserForm(instance=user)
    customerForm=forms.CustomerForm(request.FILES,instance=customer)
    mydict={'userForm':userForm,'customerForm':customerForm}
    if request.method=='POST':
        userForm=forms.CustomerUserForm(request.POST,instance=user)
        customerForm=forms.CustomerForm(request.POST,instance=customer)
        if userForm.is_valid() and customerForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            customerForm.save()
            return HttpResponseRedirect('my-order')
    return render(request,'ecom/edit_profile.html',context=mydict)



#---------------------------------------------------------------------------------
#------------------------ ABOUT US AND CONTACT US VIEWS START --------------------
#---------------------------------------------------------------------------------
def aboutus_view(request):
    return render(request,'Shop/about.html')

def contactus_view(request):
    sub = forms.ContactusForm()
    if request.method == 'POST':
        sub = forms.ContactusForm(request.POST)
        if sub.is_valid():
            email = sub.cleaned_data['Email']
            name=sub.cleaned_data['Name']
            message = sub.cleaned_data['Message']
            send_mail(str(name)+' || '+str(email),message, settings.EMAIL_HOST_USER, settings.EMAIL_RECEIVING_USER, fail_silently = False)
            return render(request, 'ecom/contactussuccess.html')
    return render(request, 'ecom/contactus.html', {'form':sub})



# def service(request):
#    if request.method == 'GET':
#      Subscriber=request.GET['Subscriber']
#      Watch_hour=request.GET['Watch_hour']
#      Views=request.GET['Views']
#      Channel_Url=request.GET['Channel_Url']

#    return render(request,'ecom/ytservice.html',{'Subscriber':Subscriber,'Watch_hour':Watch_hour,'Views':Views,'Channel_Url':Channel_Url})

# def ytservice(request):
#    if request.method == 'GET':
#      name=request.GET['name']
#      mobile=request.GET['mobile']
#      Transaction_number=request.GET['Transaction_number']
   

#    return render(request,'ecom/payment.html',{'name':name})

def sellyt(request):
    if request.method == 'POST':
       
       ytsellname1=request.POST.get('Name')
       Whatsapp1=request.POST.get('Whatsapp')
       Channel_Link1=request.POST.get('Channel_Link')
       Subscribers1=request.POST.get('Subscribers')
       Status1=request.POST.get('Status')
       Price1=request.POST.get('Price')
       savetodatabase=ytsell()
    #    savetodatabase.save(ytsellname=ytsellname1,Whatsapp=Whatsapp,Channel_Link=Channel_Link,Subscribers=Subscribers,Status=Status,Price=Price)
       savetodatabase.ytsellname=ytsellname1
       savetodatabase.Whatsapp=Whatsapp1
       savetodatabase.Subscribers=Subscribers1
       savetodatabase.Channel_Link=Channel_Link1
       savetodatabase.Status=Status1
       savetodatabase.Price=Price1
    #    savetodatabase.user=User
       savetodatabase.save()
    else:
        return redirect('sellyt')
    return render(request,'ecom/sell_sucess.html')


def ytservice1(request):
    if request.method == 'POST':
       
       ytsellname1=request.POST.get('Name1')
       Whatsapp1=request.POST.get('Whatsapp1')
       Channel_Link1=request.POST.get('Channel_Url1')
       Subscribers1=request.POST.get('Subscriber1')
       watchhour=request.POST.get('Watch_hour1')
       Views1=request.POST.get('Views1')
       savetodatabase=ytservice()
    #    savetodatabase.save(ytsellname=ytsellname1,Whatsapp=Whatsapp,Channel_Link=Channel_Link,Subscribers=Subscribers,Status=Status,Price=Price)
       savetodatabase.ytname=ytsellname1
       savetodatabase.Whatsapp_number=Whatsapp1
       savetodatabase.ytSubscribers=Subscribers1
       savetodatabase.ytChannel_Link=Channel_Link1
       savetodatabase.ytStatus=watchhour
       savetodatabase.ytPrice=Views1
    #    savetodatabase.user=User
       savetodatabase.save()
    else:
        return redirect('sellyt')
    return render(request,'ecom/ytservice_sucess.html')


# # Replace 'your_message' with the actual message you want to send
# message = "Hello, this is your message."

# # Replace 'whatsapp_number' with the actual WhatsApp number you want to send the message to
# whatsapp_number = "+917418291374"

# # Send the message
# kit.sendwhatmsg(whatsapp_number, message, 0, 0)