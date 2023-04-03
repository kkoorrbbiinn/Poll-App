from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Event, Group, Poll

# Create your views here.
events = []
# Home view


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def events_index(request):
    # We pass data to a template very much like we did in Express!
    return render(request, 'events/index.html', {
        'events': events
    })

# *************** Group Views ****************


class GroupList(ListView):
    model = Group


class GroupDetail(DetailView):
    model = Group


class GroupCreate(CreateView):
    model = Group
    fields = '__all__'


class GroupUpdate(UpdateView):
    model = Group
    fields = '__all__'


class GroupDelete(DeleteView):
    model = Group
    success_url = '/groups/'


def assoc_group(request, event_id, group_id):
    Event.objects.get(id=event_id).groups.add(group_id)
    return redirect('home')
  # delete line above and uncomment line below to redirect to events details page once created
    # return redirect('detail', event_id=event_id)


def remove_group(request, event_id, group_id):
    Event.objects.get(id=event_id).groups.remove(group_id)
    return redirect('home')
  # delete line above and uncomment line below to redirect to events details page once created
    # return redirect('detail', event_id=event_id)return redirect('detail', event_id=event_id)


def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in via code
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)