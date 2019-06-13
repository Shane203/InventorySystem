from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic

import datetime

from .models import Item


class IndexView(generic.ListView):
    template_name = 'inventory/index.html'
    context_object_name = 'categories'

    def get_queryset(self):
        return Item.objects.values_list('category', flat=True).distinct()


class DetailView(generic.DetailView):
    model = Item
    template_name = 'inventory/detail.html'


class ModifyView(generic.ListView):
    template_name = 'inventory/modify.html'
    context_object_name = 'items'

    def get_queryset(self):
        return Item.objects.all()


class CategoryView(generic.ListView):
    template_name = 'inventory/category.html'
    context_object_name = 'items'

    def get_queryset(self):
        return Item.objects.all()


class RangeView(generic.ListView):
    template_name = 'inventory/range.html'
    context_object_name = 'items'

    def get_queryset(self):
        return Item.objects.all()


class RecentView(generic.ListView):
    template_name = 'inventory/recent.html'
    context_object_name = 'recent_additions'

    def get_queryset(self):
        return Item.objects.order_by('-date_time_added')[:5]


class ExpiringView(generic.ListView):
    template_name = 'inventory/duetoexpire.html'
    context_object_name = 'expiring'

    def get_queryset(self):
        return Item.objects.filter(expiry_date__lte=datetime.datetime.today() + datetime.timedelta(days=2))


class AddedView(generic.DetailView):
    model = Item
    template_name = 'inventory/added.html'


def add(request):
	if request.method == "POST":
		if request.POST.get('name') and request.POST.get('price') and request.POST.get('category'):
			# This check excludes expiry_date because I was trying to allow null entries to indicated "Not Applicable"
			if len(Item.objects.filter(name=request.POST.get('name'))) < 5 and len(Item.objects.all()) < 200:
				new = Item(name=request.POST.get('name'), price=request.POST.get('price'), category=request.POST.get('category'), expiry_date=request.POST.get('expiry'))
				new.save()
				return redirect('../%s/added/' % new.id)
			else:
				# Should give feedback saying you can't add more
				return render(request, 'inventory/modify.html')

	
def delete(request):
    if request.method == 'POST':
        if request.POST.get('todelete'):
            todelete = Item.objects.filter(id=request.POST.get('todelete'))
            deleted = []
            for item in todelete:
                deleted.append((item.name, item.id))
            # Unused due to time constraints
            todelete.delete()
            return HttpResponse("Successfully deleted selected item(s)")


def update(request):
    if request.method == "POST":
        if request.POST.get('toupdate'):
            if request.POST.get('name'):
                Item.objects.filter(id=request.POST.get('toupdate')).update(name=request.POST.get('name'))
            if request.POST.get('price'):
                Item.objects.filter(id=request.POST.get('toupdate')).update(price=request.POST.get('price'))
            if request.POST.get('category'):
                Item.objects.filter(id=request.POST.get('toupdate')).update(category=request.POST.get('category'))
            if request.POST.get('expiry'):
                Item.objects.filter(id=request.POST.get('toupdate')).update(expiry_date=request.POST.get('expiry'))
            return render(request, 'inventory/modify.html')
