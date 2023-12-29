from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse,HttpRequest
from payments.models import *
from frontend.models import *
from payments.forms import *
from django.contrib import messages
from django.conf import settings

# Create your views here.

def initiate_payment(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        payment_form = PaymentForm(request.POST)
        if payment_form.is_valid():
            payment = payment_form.save()
            return render(request, 'backend/make_payment.html', {'payment':payment, 'paystack_public_key':settings.PAYSTACK_PUBLIC_KEY})

    else:
        payment_form = PaymentForm()

        # amount = request.POST['amount']
        # email = request.POST['email']

        # pk = settings.PAYSTACK_PUBLIC_KEY

        # payment = Payment.objects.create(amount=amount, email=email, user=request.user)
        # payment.save()

        # context = {
        #     'payment':payment,
        #     'field_values':request.POST,
        #     'paystack_pub_key': pk,
        #     'amount_value': payment.amount_value(),
        # }
        # return render(request, 'backend/make_payment.html', context)
    return render (request, 'backend/initiate_payment.html', {'payment_form':payment_form})

def verify_payment(request, ref: str) -> HttpResponse:
    payment =get_object_or_404(Payment,Gadgets, ref=ref)
    verified = payment.verify_payment()
    
    if verified:
        messages.success(request, "verification Successful")
    else:
        messages.error(request, "verification Failed")
    return redirect("initiate_payment")

