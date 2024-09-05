from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from product.models import Car, Comment
from product.forms import CommentForm, AddCarForm, EditCarForm
from django.http import HttpResponseRedirect


def main(request):
    cars = Car.objects.all()
    return render(request, 'main.html', {'cars': cars})


def get_car(request, car_id):
    try:
        car = Car.objects.select_related('owner').get(id=car_id)
        comments = Comment.objects.select_related('author').filter(car_id=car_id)
    except Car.DoesNotExist:
        return HttpResponseRedirect('/product/main/')
    return render(request, 'car.html', {'car': car, 'comments': comments})


@login_required
def add_comment(request, car_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            Comment.objects.create(content=form.cleaned_data['content'], car_id=car_id, author=request.user)
            return HttpResponseRedirect(f"/product/car/{car_id}/")
    else:
        form = CommentForm()

    return render(request, 'add_comment.html', {'form': form})


@login_required
def add_car(request):
    if request.method == 'POST':
        form = AddCarForm(request.POST)
        if form.is_valid():
            Car.objects.create(make=form.cleaned_data['make'], model=form.cleaned_data['model'],
                               year=form.cleaned_data['year'], description=form.cleaned_data['description'],
                               owner=request.user)
            return HttpResponseRedirect('/product/main/')
    else:
        form = AddCarForm()

    return render(request, 'add_car.html', {'form': form})


@login_required
def edit_car(request, car_id):
    try:
        car = Car.objects.get(id=car_id, owner=request.user)
    except Car.DoesNotExist:
        return HttpResponseRedirect('/product/main/')

    if request.method == 'POST':
        form = EditCarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/product/main/')
    else:
        form = EditCarForm(instance=car)

    return render(request, 'edit_car.html', {'form': form, 'car_id': car_id})


@login_required
def delete_car(request, car_id):
    try:
        car = Car.objects.get(id=car_id, owner=request.user)
        car.delete()
        return HttpResponseRedirect('/product/main/')
    except Car.DoesNotExist:
        return HttpResponseRedirect('/product/main/')
