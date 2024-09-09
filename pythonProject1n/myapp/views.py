
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from myapp.models import MovieDb

from myapp.forms import MovieForm


def ListFunction(request):
    recent_visits=request.session.get('recent_visits',[])
    count=request.session.get('count',0)
    count=int(count)
    count+=1
    request.session['count']=count
    recent_movie_set=MovieDb.objects.filter(pk__in=recent_visits)
    alldata = MovieDb.objects.all()
    movieList = {'key':alldata,'visits':count,'recent_visited':recent_movie_set}
    response= render(request,'Listpage.html',movieList)
    return response


@login_required(login_url='login')
def EditFunction(request,pk):
    actform_Edit = MovieDb.objects.get(id=pk)
    if request.POST:
        forms = MovieForm(request.POST,instance=actform_Edit)
        if forms.is_valid():
            actform_Edit.save()
            return redirect('list')
    else:
        recent_visits=request.session.get('recent_visits',[])
        recent_visits.insert(0,pk)
        request.session['recent_visits']=recent_visits
        movie=MovieForm(instance=actform_Edit)
        context={'key':movie}
    return render(request, 'Createpage.html', context)

@login_required(login_url='login')

def DeleteFunction(request,pk):
    actform =MovieDb.objects.get(id=pk)
    actform.delete()

    return redirect('list')
    return render(request, 'EditList.html')

@login_required(login_url='login')

def CreateFunction(request):
    movieform=MovieForm()
    context={'key':movieform}
    # if request.method == 'POST':
    #     title=request.POST.get('Movie_Title')
    #     desc=request.POST.get('Description')
    #     year=request.POST.get('ReleasedYear')
    #     movie=MovieDb.objects.create(Movie_Title=title,ReleasedYear=year,Description=desc)
    #     movie.save()
    if request.method == 'POST':
        movieform=MovieForm(request.POST,request.FILES)
        if movieform.is_valid():
            movieform.save()
            return redirect('list')
    return render(request,'Createpage.html',context)

