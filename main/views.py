from django.http import HttpResponse
from django.http import HttpResponseForbidden
from django.template import loader
from .converter_form import ConverterForm
from converters.base_two import BaseTwo
from .decorators import Decorators

# main index
def index(request):
    template = loader.get_template('main/index.html')
    # generate from form template
    form = ConverterForm()
    context = {
        'form': form,
    }
    return HttpResponse(template.render(context, request))

# redirect for converter form
@Decorators.catch_and_log
def convert(request):
    template = loader.get_template('main/index.html')
    requestMod = request.POST.copy()
    
    try:
        # get value from form request
        valueToconvert = requestMod['valueToConvert']
        # use converter utility
        base2 = BaseTwo().convert(valueToconvert)
    except:
        # any exceptions should be handled in the util and we only care that its not an integer
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