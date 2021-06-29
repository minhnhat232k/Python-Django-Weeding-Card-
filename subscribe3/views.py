from django.shortcuts import render
from webapp_basic.settings import EMAIL_HOST_USER
from . import forms
from django.core.mail import send_mail
#from subscribe.forms import SubscribeForm
from .models import Subscribe3
# Create your views here.
#DataFlair #Send Email
def subscribe3(request):
    form = forms.Subscribe3()
    if request.method == 'POST':
        form = forms.Subscribe3(request.POST)
        print("table: ",request.POST)
        if form.is_valid():
           form.save()

        subject = 'Thư mời dự tiệc đám cưới'
        message = 'Kính mời ' + str(form['name'].value()) +' đến dự buổi tiệc đám cưới vào lúc ' + str(form['time'].value()) + ' ngày ' + str(form['day'].value()) + ' tháng ' + str(form['month'].value()) + ' năm ' + str(form['year'].value()) + '. Rất mong ' + str(form['name'].value()) + ' sẽ đến góp vui.'
        recepient = str(form['email'].value())
        send_mail(subject,
            message, EMAIL_HOST_USER, [recepient], fail_silently = False)
        return render(request, 'subscribe3/success.html', {'recepient': recepient})
    return render(request, 'subscribe3/index.html', {'form':form})
