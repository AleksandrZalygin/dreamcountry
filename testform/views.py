from django.shortcuts import render, redirect
from .models import Country
from .forms import CountryForm

def testform(request):
    error = ''

    if request.method == 'POST':
        form = CountryForm(request.POST)
        if form.is_valid():

            climate = form.cleaned_data['climate']
            world = form.cleaned_data['world']
            work = form.cleaned_data['work']
            medicine = form.cleaned_data['medicine']
            citizenship = form.cleaned_data['citizenship']

            if climate == 'Лето':
                if world == 'Европа':
                    if citizenship == 'Нет':
                        if medicine == 'Да':
                            if work == 'Нет':
                                return render(request, 'testform/denmark.html')
                            else:
                                return render(request, 'testform/bulgaria.html')
                            
                        else:
                            if work == 'Нет':
                                return render(request, 'testform/switzerland.html')
                            else:
                                return render(request, 'testform/germany.html')
                        
                    else:
                        if medicine == 'Нет':
                            return render(request, 'testform/netherlands.html')
                        else:
                            return render(request, 'testform/sweden.html')

                elif world == 'Азия':
                    return render(request, 'testform/thailand.html')

                elif world == 'Америка':
                    if medicine == 'Нет':
                        return render(request, 'testform/usa.html')
                    else:
                        return render(request, 'testform/cuba.html')
                else:
                    return render(request, 'testform/australia.html')

            else:
                if world == 'Европа':
                    if medicine == 'Да':
                        return render(request, 'testform/finland.html')
                    else:
                        return render(request, 'testform/norway.html')
                else:
                    return render(request, 'testform/canada.html')
        else:
            error = 'error'


    form = CountryForm()

    data = {
        'form': form,
        'error': error,
    }

    return render(request, 'testform/test.html', data)
