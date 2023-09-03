from django.shortcuts import render
from jotter.models import Entry, Category, Hashtag
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import EntryForm, CategoryForm, HashtagForm
import re

def new_entry(request):
    if request.method != 'POST':
        form1 = CategoryForm()
        form2 = EntryForm()
    else:
        form1 = CategoryForm(data=request.POST)
        form2 = EntryForm(data=request.POST)
        if form2.is_valid():
            form2.save()
        if form1.is_valid():
            entry = Entry.objects.last()
            category = Category(category=form1.cleaned_data['category'], entry_id=entry.id)
            category.save()
            hashtags = re.findall(r"#(\w+)", form2.cleaned_data['notes'])
            for tag in hashtags:
                hashtag = Hashtag(tag=tag, entry_id=entry.id)
                hashtag.save()
            return HttpResponseRedirect(reverse('jotter:all_entries'))
    context = {'form1': form1, 'form2': form2}
    return render(request, 'jotter/new_entry.html', context)

def all_entries(request):
    entries = Entry.objects.order_by('-date')
    context = {'entries': entries}
    return render(request, 'jotter/all_entries.html', context)

def category_search(request):
    if request.method != 'POST':
        form = CategoryForm()
    else:
        form = CategoryForm(data=request.POST)
        if form.is_valid():
            category = form.cleaned_data['category']
            entries = Entry.objects.filter(category__category=category).order_by('-date')
            context = {'entries': entries, 'category': category}
            return render(request, 'jotter/category_search.html', context)
    context = {'form': form}
    return render(request, 'jotter/category_search.html', context)

def hashtag_search(request):
    if request.method != 'POST':
        form = HashtagForm()
    else:
        form = HashtagForm(data=request.POST)
        if form.is_valid():
            tag = form.cleaned_data['tag']
            entries = Entry.objects.filter(tag__tag=tag).order_by('-date')
            context = {'entries': entries, 'tag': tag}
            return render(request, 'jotter/hashtag_search.html', context)
    context = {'form': form}
    return render(request, 'jotter/hashtag_search.html', context)
