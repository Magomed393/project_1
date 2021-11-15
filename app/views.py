
from django import forms
from django.http import JsonResponse
from django.shortcuts import render


class NameForm(forms.Form):
     val = forms.CharField(label='Введите строку ДНК', max_length=200)

s = input('Введите значение для поиска: ')
print(type(s))
# s='fad'

def get_json(request):
    form = NameForm()
    if request.method == 'POST' and request.is_ajax():
        x = request.POST.copy()
        if s in x['val']:
            return JsonResponse({"result": 'Найдено'})
        else:
            return JsonResponse({"result": 'Не найдено'})
    else:
        return render(request, '1.html', {'form': form})
