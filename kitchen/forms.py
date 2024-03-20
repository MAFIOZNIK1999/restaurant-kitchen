from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator

from kitchen.models import Dish, Cook


class DishForm(forms.ModelForm):
    cooks = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple(),
    )

    class Meta:
        model = Dish
        fields = "__all__"


class CookForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = UserCreationForm.Meta.fields + (
            "years_of_experience",
            "first_name",
            "last_name"
        )


class CookExperienceUpdateForm(forms.ModelForm):
    MIN_YEAR_OF_EXPERIENCE = 1
    years_of_experience = forms.IntegerField(
        required=True,
        validators=[MinValueValidator(MIN_YEAR_OF_EXPERIENCE)]
    )

    class Meta:
        model = Cook
        fields = ["years_of_experience"]
