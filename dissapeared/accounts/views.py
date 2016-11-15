from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

def denied_access(request):
    usuario = request.user
    return render_to_response('denied_acces.html', {'usuario':usuario}, context_instance=RequestContext(request))
