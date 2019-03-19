from django.http import HttpResponse
from django.http import HttpResponseForbidden
from django.template import loader
from .converter_form import ConverterForm
from converters.base_two import BaseTwo


def index(request):
    template = loader.get_template('main/index.html')
    form = ConverterForm()
    context = {
        'form': form,
    }
    return HttpResponse(template.render(context, request))
    
def convert(request):
    template = loader.get_template('main/index.html')
    requestMod = request.POST.copy()
    
    # validate string is int
    try:
        valueToconvert = requestMod['valueToConvert']
        int(valueToconvert)
        base2 = BaseTwo().convert(valueToconvert)
    except:
        base2 = "value must be an integer"
    
    # possible use later
    requestMod['convertedValue'] = base2
    
    # only allow posts or redirects
    if (request.method == 'POST'):
        form = ConverterForm(requestMod)
    else:
        return HttpResponseForbidden()
    
    context = {
        'form': form,
        'convertedPage': True,
        'base2': base2,
    }
    
    return HttpResponse(template.render(context, request))