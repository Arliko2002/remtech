import base64

from django import forms
from django.core.files.base import ContentFile
from django.core.files.images import ImageFile
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import object_detection.opencv as cv
from django.http import JsonResponse


@csrf_exempt
def index(request):
    if request.method == "POST":
        file = request.FILES['thumbnail']
        with open(f'{file.name}', 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        w, h = cv.detect(file.name)
        with open(f'{file.name}-edited.jpg', "rb") as f:
            f = base64.b64encode(f.read()).decode('utf-8')
            ctx = {'image': f, 'w': w, 'h': h}
            return JsonResponse(ctx, safe=False)
