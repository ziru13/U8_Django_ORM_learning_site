from django import forms
from . import models


class QuizForm(forms.ModelForm):
    class Meta:
        model = models.Quiz
        fields = [
            'title',
            'description',
            'order',
            'total_questions', ]


# 4.6 创建自定义form media
class QuestionForm(forms.ModelForm):
    class Media:
        css = {'all': ('courses/css/order.css',)}
        js = (
            'courses/js/vendor/jquery.fn.sortable.min.js',
            'courses/js/order.js'
        )


class TrueFalseQuestionForm(QuestionForm):  # 4.6 改成QuestionForm
    class Meta:
        model = models.TrueFalseQuestion
        fields = ['order', 'prompt']


class MultipleChoiceQuestionForm(QuestionForm):  # 4.6 改成QuestionForm
    class Meta:
        model = models.MultipleChoiceQuestion
        fields = ['order', 'prompt', 'shuffle_answers']


class AnswerForm(forms.ModelForm):
    class Meta:
        model = models.Answer
        fields = ['order', 'text', 'correct']


# 4.1
AnswerFormSet = forms.modelformset_factory(
    models.Answer,
    form=AnswerForm,
    extra=2,  # 在原有的答案基础上再添加两个可填的答案
    # max_count=4,/min_count=4 还可以添加最大/最小数量, 可以控制forms的数量
)

AnswerInlineFormSet = forms.inlineformset_factory(
    models.Question,   # inline将会在这个模型中出现,,用于保存的模型
    models.Answer,     # 在form中中编辑的模型
    extra=2,
    fields=('order', 'text', 'correct'),
    formset=AnswerFormSet,
    min_num=1,
)
