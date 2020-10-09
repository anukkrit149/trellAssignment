"""
Copyrights Reserved 
Developed By- Anukkrit Shanker
"""
from .models import *
from django import forms
from .models import *


class addMovieForm(forms.ModelForm):
    class Meta:
        model = movieData
        fields = '__all__'


class addShowForm(forms.ModelForm):
    class Meta:
        model = shows
        fields = '__all__'

    def clean(self):
        cleaned_data = self.cleaned_data
        movie = cleaned_data.get('movie')
        time = cleaned_data.get('timeSlots')
        matching_row = shows.objects.filter(movie=movie, timeSlots=time)
        if self.instance:
            matching_row = matching_row.exclude(pk=self.instance.pk)
        if matching_row.exists():
            msg = u"Show: %s has already exist." % movie
            raise forms.ValidationError(msg)
        else:
            return self.cleaned_data


class buyTicketsForm(forms.ModelForm):
    class Meta:
        model = tickets
        fields = '__all__'
    #
    # def save(self, commit=True):
    #     show = self.cleaned_data['movieShow']
    #     showObj = shows.objects.get(show)
    #     showObj.ticketsSold += self.cleaned_data['nTickets']
    #     showObj.save()
    #     return super().save(commit)

    # TODO-Validation
    # def clean(self):
    #     cleaned_data = self.cleaned_data
    #     nTicket = cleaned_data.get('nTickets')
    #     show = cleaned_data.get('movieShow')
    #     matching_row = shows.objects.get(show)
    #     if (matching_row.totalTickets - matching_row.ticketsSold)-nTicket < 0:
    #         msg = u"Tickets Not Available, only %s tickets available" % str(matching_row.totalTickets - matching_row.ticketsSold)
    #         raise forms.ValidationError(msg)
    #     else:
    #         return self.cleaned_data



class searchForm(forms.Form):
    text = forms.CharField(max_length=150)
