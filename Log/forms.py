import re

from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from django.utils.encoding import force_text

# def mobile_validate(value):
#     if value and '@' not in value:
#         patern = re.compile(r'^((13[0-9])|(14[5|7])|(15([0-3]|[5-9]))|(18[0,5-9]))\\d{8}$')
#         if not patern.match(value):
#             raise ValidationError('手机号码格式错误')
# class EmailPhoneValidate(EmailValidator):
#
#     def __call__(self, value):
#         if not value:
#             raise ValidationError(self.message, code=self.code)
#         if '@' not in value:
#             mobile_validate(value)
#
#         value = force_text(value)
#
#         if not value or '@' not in value:
#             raise ValidationError(self.message, code=self.code)
#
#         user_part, domain_part = value.rsplit('@', 1)
#
#         if not self.user_regex.match(user_part):
#             raise ValidationError(self.message, code=self.code)
#
#         if (domain_part not in self.domain_whitelist and
#                 not self.validate_domain_part(domain_part)):
#             # Try for possible IDN domain-part
#             try:
#                 domain_part = domain_part.encode('idna').decode('ascii')
#                 if self.validate_domain_part(domain_part):
#                     return
#             except UnicodeError:
#                 pass
#             raise ValidationError(self.message, code=self.code)



class LoginForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=254, required=True,
                            widget=forms.TextInput(attrs={
                                 'type': 'text',
                                 'name': 'email',
                                 'placeholder': '手机或者邮箱'}))
    user_name = forms.CharField(label='Username', max_length=100, required=True, widget=forms.TextInput(attrs={
                            'type': 'text',
                            'name': 'user_name',
                            'placeholder': '昵称'}))
    password = forms.CharField(label='Password', max_length=100, required=True, widget=forms.PasswordInput(attrs={
                            'name': 'password',
                            'placeholder': '密码'}))
    remember_me = forms.BooleanField(label='Remember me', required=True, widget=forms.CheckboxInput(attrs={
                            'name': 'remember_me', }))



