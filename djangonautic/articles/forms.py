from django import forms
from . import models

class CreateArticle(forms.ModelForm):
    class Meta:
        model=models.Article  #the model for which we need a form
        fields=['body','thumb'] #the fields we need to output in the form
    #a class like this can be created if any customizations are to be made. see documentation of modelforms for the customizations
    #if we want to create a form from the model as it is , then we can do CreateArticle=modelform_factory(Article,fields=('body','thumb'))
