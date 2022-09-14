from django.shortcuts import render
from .models import *
import requests
def contact(request):
    data = Contact.objects.all()
    context = {
        'data': data
    }
    if request.method == "POST":
        ism = request.POST['ism']
        email = request.POST['email']
        telefon = request.POST['telefon']
        mavzu = request.POST['mavzu']
        xabar = request.POST['xabar']
        data = Contact.objects.create(fio=ism, email=email, phone=telefon, topic=mavzu, message=xabar)
        data.save()
        msg = f'Sizning xabaringiz muvaffaqiyatli yuborildi kuting albatta sizga admin javob yozadi'
        context = {
            'status': msg
        }
        token = "5683845173:AAE8f5sGxFm4AzhHuDrspYPske8meJ54-sE"
        text = "Abdulhodi Sizga xabar yuborishdi: \n\n Ism: " + str(request.POST.get('ism')) + '\n Email: ' + str(request.POST.get("email")) + '\n Telefon raqam: ' + str(request.POST.get("telefon")) + '\n Mavzu: ' + str(request.POST.get("mavzu")) + '\n Xabari: ' + str(request.POST.get('xabar'))
        url = 'https://api.telegram.org/bot' + token + '/sendMessage?chat_id='
        requests.get(url + str(1833947501) + '&text=' + text)
    return render(request, 'contact.html', context)

# def contact(request):
#     data = Contact.objects.all()
#     context = {
#         'data': data
#     }
#     if request.method=='POST':
#
    #     ism = request.POST['ism']
    #     email = request.POST['email']
    #     telefon = request.POST['telefon']
    #     mavzu = request.POST['mavzu']
    #     xabar = request.POST['xabar']
    #     data=Contact.objects.create(fio=ism,email=email,phone=telefon,topic=mavzu,message=xabar)
    #     data.save()
    #     msg=f'Sizning xabaringiz muvaffaqiyatli yuborildi kuting albatta sizga admin javob yozadi'
    #     context={
    #         'status':msg
    #     }
    # return render(request,'contact.html',context)



    ### bot deb turaylik ##

# Contact.objects.create(
#             name=request.POST.get("ism"),
#             email=request.POST.get("email"),
#             number=request.POST.get("telefon"),
#             topic=request.POST.get("mavzu"),
#             message=request.POST.get("xabar"),
#         )

### Mening telegram id im ###

# 1833947501 #