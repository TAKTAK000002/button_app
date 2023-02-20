from django.shortcuts import render

# Create your views here.

def button_form(request):
    if request.method == "POST":
            if "start_button" in request.POST:
                conetent = {

                'message': 'ボタンが押されました。'

                }
                return render(request,'buttonapp/button_form.html',conetent)


    return render(request, 'buttonapp/button_form.html',{})
