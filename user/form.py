"""
    用户管理由项目应用user实现，在项目应用user中创建form.py。
    该文件用于定义表单类MyUserForm，由表单类实现用户注册功能。
"""

# user的form.py
from django.contrib.auth.forms import UserCreationForm
from .models import MyUser
from django import forms

# 定义模型 MyUser 的数据表单
class MyUserCreationForm(UserCreationForm):
    # 重写初始化方法
    # 设置自定义字段 password1 和 password2 的样式和属性
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(
            attrs={'class': 'txt tabInput',
                   'placeholder': '密码, 4-16位数字/字母/符号(空格除外)'})
        self.fields['password2'].widget = forms.PasswordInput(
            attrs={'class': 'txt tabInput', 'placeholder': '重复密码'})

    class Meta(UserCreationForm.Meta):
        model = MyUser
        # 在注册页面添加模型字段：手机号码、头像
        fields = UserCreationForm.Meta.fields + ('mobile','avatar',)
        # 设置模型字段的样式和属性
        widgets = {
            'mobile': forms.widgets.TextInput(
                attrs={'class': 'txt tabInput', 'placeholder': '手机号'}),
            'username': forms.widgets.TextInput(
                attrs={'class': 'txt tabInput', 'placeholder': '用户名'}),
         }