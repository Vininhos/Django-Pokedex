from django.forms import ModelForm

from pokemon.models import Pokemon


class PokemonForm(ModelForm):
    class Meta:
        model = Pokemon
        fields = "__all__"
