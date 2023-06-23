from django import forms
from .models import Post, Comment, UserProfile
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'photo', 'category')

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control'
            }),
            'photo': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'category': forms.Select(attrs={
                'class': 'form-select'
            })
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', max_length=150, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))


class RegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username'
    }))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Name'
    }))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Surname'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Confirm password'
    }))

    def save(self, commit=True):
        user = super().save(commit=False)

        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()
        return user


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('bio', 'address', 'phone', 'mobile', 'website', 'github', 'twitter', 'instagram', 'facebook')
        widgets = {
            'bio': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Bio'
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Address'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone'
            }),
            'mobile': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Mobile'
            }),
            'website': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Website'
            }),
            'github': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Github'
            }),
            'twitter': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Twitter'
            }),
            'instagram': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Instagram'
            }),
            'facebook': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Facebook'
            })
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Your comment text'
            })
        }
