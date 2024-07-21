from django import forms
from .models import Pizza, Size
#class PizzaForm(forms.Form):
    #topping1 = forms.CharField(label="Topping 1", max_length=100, widget = forms.PasswordInput) #widget = forms.Textarea te3tina textarea espace kbira bach neketbo fiha,
                                                                                                #widget = forms.PasswordInput te3tina input kima ki tbghi dekhel password fl facebook les lettres maybanoch ywelo n9ati. 
    #toppings = forms.MultipleChoiceField(choices=[('pep','Pepperoni'), ('cheese','Cheese'), ('olives','Olives')],widget = forms.CheckboxSelectMultiple) #widget = forms.CheckboxSelectMultiple biha tekhrejlek input checks ta3 Pepperoni cheese ...
    #topping1 = forms.CharField(label="Topping 1", max_length=100)
    #topping2 = forms.CharField(label="Topping 2", max_length=100)
    #size = forms.ChoiceField(label="size", choices=[('Small','Small'), ('Medium','Medium'), ('Large','Large')])

class PizzaForm(forms.ModelForm): #ModelForm allows you to create forms from your existing models 
    #size = forms.ModelChoiceField(queryset=Size.objects, empty_label=None, widget=forms.RadioSelect) #queryset=Size.objects me3netha queryset tedi ga3 objects li zayedhom l'admin, empty_label=None me3netha mkach empty label displayed, widget=forms.RadioSelect me3netha input hna rahi b RadioSelect chghol kima check bsh matigch tdir select 3la multi options tdir ghi whda brk.
    #image = forms.ImageField()
    #email = forms.EmailField() #ki dernaha nzadet wehedha m3a topping 1 w 2 w size fl la page ta3na.
    #url = forms.URLField() #ki dernaha nzadet wehedha m3a topping 1 w 2 w size fl la page ta3na.
    class Meta:
        model = Pizza
        fields = ['topping1', 'topping2', 'size'] #gle3na li kant lfog w derna hadi drna run lserver ro7na la page affichatlna ghi kifkif
        labels = {'topping1' : 'Topping 1', 'topping2' : 'Topping 2'}    

class MultiplePizzaForm(forms.Form):
    number = forms.IntegerField(min_value=2, max_value=6)
        
