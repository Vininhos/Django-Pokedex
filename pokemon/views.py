from django.shortcuts import render
from django.views.generic import ListView, DetailView

from pokemon.forms import PokemonForm
from pokemon.models import Pokemon, Tipo


class PokemonListView(ListView):
    model = Pokemon


class PokemonEvolutionsListView(ListView):
    model = Pokemon

    def get_queryset(self):
        qs = super().get_queryset()
        slug = self.kwargs['slug']
        p = Pokemon.objects.get(slug=slug)
        qs = qs.filter(involucao__pk=p.pk)
        print(qs)
        return qs


class PokemonInvolutionListView(DetailView):
    model = Pokemon

    def get_object(self):
        slug = self.kwargs['slug']
        p = Pokemon.objects.get(slug=slug)
        return p.involucao


class PokemonPorTipoListView(ListView):
    model = Pokemon

    def get_queryset(self):
        qs = super().get_queryset()
        nome = self.kwargs['nome'].capitalize()
        t = Tipo.objects.get(nome=nome)
        qs = qs.filter(tipos=t)
        return qs


class PokemonDetailView(DetailView):
    model = Pokemon


class TipoListView(ListView):
    model = Tipo


def PokemonAdd(request):
    if request.method == "GET":
        form = PokemonForm()
        context = {'form': form}
        return render(request, "pokemon/pokemon_add.html", context=context)
    else:
        form = PokemonForm(request.POST)
        formvalue = False
        if form.is_valid():
            formvalue = form.is_valid()
            pokemon = form.save()
            form = PokemonForm()
        context = {'form': form, 'formvalue': formvalue}
        return render(request, "pokemon/pokemon_add.html", context=context)
