from django.http import HttpResponse

from models import Settings


def testdb(request):
    test1 = Settings(name='runoob')
    test1.save()
    return HttpResponse("<p>db add success</p>")
