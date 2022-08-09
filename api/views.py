from django.shortcuts import render

from api.forms import CreateNewUser
#from .serializers import RoomSerializer
from .models import User, CourseCode
from django.http import HttpResponse, HttpResponseRedirect
import scrape

# Create your views here.


def index(request, name):
    invalid_code = False
    try:
        u = User.objects.get(name=name)

        print(u.coursecode_set.all())
        
        if request.method == "POST":
            print("...post...", request.POST)

            if request.POST.get("newItem"):
                txt = request.POST.get("name")
                try:
                    dic = scrape.return_data(txt)
                except:
                    print('invalid!!!!!')
                    invalid_code = True
                else:
                    print("...this is the dic...", dic)
                    u.coursecode_set.create(
                        code=txt,
                        class_abr=dic["class_abr"],
                        class_name=dic["class_name"],
                        instructors=dic["instructor_list"],
                        class_time=dic["class_time"],
                        class_type=dic["class_type"],
                        units=dic["units"],
                        max_capacity=dic["max_capacity"],
                        enrolled=dic["enrolled"],
                        waitlisted=dic["waitlisted"],
                        requested=dic["requested"],
                        reserved_new=dic["reserved_new"],
                        status=dic["status"]
                    )
            elif request.POST.get("delItem"):
                print('WOEBHWOBIEHWOBEIHWBOEWIHBOWIBH')
                txt = request.POST.get("name")
                for cc in u.coursecode_set.all():
                    if cc.code == txt:
                        cc.delete()
                    else:
                        invalid_code = True


        # remove duplicate data
        for instance in CourseCode.objects.all():
            if CourseCode.objects.filter(code=instance.code).filter(username=instance.username).count() > 1:
                instance.delete()


        # return render(request, "api/courseview.html", {"u": u, "dicc":dic})
        return render(request, "api/courseview.html", {"u": u, "invalid": invalid_code})
    except:
        print('oops')
        return render(request, "api/courseview.html", {})
        
 
def create(request):
    if request.method == "POST":
        print('.......', request.method)

        # if entered name already exists in the database
        if User.objects.filter(name=request.POST["name"]).count() > 0:
            print('already exists')
            return HttpResponseRedirect(f"/{request.POST['name']}")
        else: # new
            print("yay new created")
            form = CreateNewUser(request.POST)

            if form.is_valid():
                n = form.cleaned_data["name"]
                u = User(name=n)
                u.save()

            return HttpResponseRedirect(f"/{u.name}")


    else:
        print('.......', request.method)
        form = CreateNewUser()

    return render(request, "api/create.html", {"form":form})

