from django import forms

from .models import Reader, Comment , Project


class GeneralCommentForm(forms.ModelForm):
    class Meta:
        model = Reader
        fields = "__all__"
        
        
        error_messages = {
            "Last_name":
                {"required": "Please enter your last name"},
            "First_name":
                {"required":"Please enter your first name" },
            "Email":{
                "required": "Please enter a valid email address"
            }
        }
        
        widgets = {
            'Last_name': forms.TextInput(attrs={'style': 'background-color: transparent;'}),
            'First_name': forms.TextInput(attrs={'style': 'background-color: transparent;'}),
            'Email': forms.EmailInput(attrs={'style': 'background-color: transparent;'}),
             'Comment': forms.Textarea(attrs={
                'style': 'background-color: transparent',  # light yellow
                'rows': 7,
                'cols': 40 })
             }
        
    
    
        
class CommentForm(forms.ModelForm):
    
    class Meta: 
        model = Comment
        fields = ["Last_name", "First_name", "Email", "comment"] 
        labels = {
            "Last_name": "Enter your last name:",
            "First_name":"Enter your first name: ",
            "Email": "Enter your email address:",
            "comment":"Enter your comment:"
        }
        
        error_messages = {
            "Last_name":
                {"required": "Please enter your last name"},
            "First_name":
                {"required":"Please enter your first name" },
            "Email":{
                "required": "Please enter a valid email address"
            },
            "comment":{
                "required": "Please enter a valid comment"
            }
        }
    
    






    
    