from django.forms import ModelForm, CharField, DateTimeField, Textarea, DateInput

from blog.models import Post, Comments


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'published_date']
    title = CharField(label="Заголовок", max_length=100)
    text = CharField(label="Текст", widget=Textarea)
    published_date = DateTimeField(label="Дата публикации",
                                   widget=DateInput(attrs={'type': 'date'}))


class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ('text',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
        self.fields['text'].widget = Textarea(attrs={'rows': 5})
