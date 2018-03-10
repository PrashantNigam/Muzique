from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.views.generic import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Album, Song
from .forms import UserForm, UserLoginForm


class IndexView(generic.ListView):
    template_name = 'music/index.html'

    def get_queryset(self):
        return Album.objects.all()


def login_view(request):
    title = "login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
    return render(request, "music/login_form.html", {"form": form, "title": title})


def logout_view(request):
    return render(request, "form_template", {})


# class IndexView(generic.ListView):
#     template_name = 'music/index.html'
#
#     def get_queryset(self, request):
#
#         album_list = Album.objects.all()
#         paginator = Paginator(album_list, 10)
#         page = request.GET.get('page')
#         album_set = paginator.get_page(page)
#         return render(request, 'music/index.html', {'album_set': album_set})


class DetailView(generic.DetailView):

    model = Album
    template_name = 'music/detail.html'


class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'albumTitle', 'genre', 'albumLogo']


class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'albumTitle', 'genre', 'albumLogo']


class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')


class UserFormView(View):
    form_class = UserForm
    template_name = 'music/registration_form.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            # cleaned and normalised data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            # returns user objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    request.user
                    return redirect('music:index')

        return render(request, self.template_name, {'form': form})