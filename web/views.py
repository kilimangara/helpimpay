

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.template.context_processors import csrf

from .models import HelpImPayment


def help_im_pay(request, pk):
    try:
        payment = HelpImPayment.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return render(request, '404.html')
    return render(request, 'helpimpay.html', {'pay': payment})


def create_help_im_pay(request):
    args = {}
    args.update(csrf(request))
    if request.method == 'GET':
        return render(request, 'createhelpimpay.html', args)
    elif request.method == 'POST':
        description = request.POST.get('formcomment')
        amount = request.POST.get('sum')
        payment = HelpImPayment.objects.create(description=description, amount=amount)
        return redirect('/helpimpay/{}'.format(payment.id))

