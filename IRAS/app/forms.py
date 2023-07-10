# 可能在使用中用不到！！！！
# 使用Django原生的表单处理
# 通过对html进行封装，提供基础的样式展示 
# e.g 在html中，post方法返回的context包含form参数
# 直接输出 {{form.as_p}}，将按照内置样式渲染表单
# 以用户表单为例 
from models import Interviewee # 从models模块中引入所需模型
from django import forms
class IntervieweeForm(forms.ModelForm):
    class Meta:
        model = Interviewee #表示以用户为模型设计表单
        fields = ['title','text']# 渲染到界面中的属性（以models对应属性为准）
        labels = {'title':'','text':''}# label （属性展示），此处设置为空，不展示属性名称
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
        # 通过小组件对form的样式进行约束
        # 也可直接采用bootsrap等组件库设置css样式，不使用 {{form.as_p}}
        # 提交表单时，注意input标签内的name属性要与表单属性对应即可