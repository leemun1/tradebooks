from django import forms

from market.models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book

        fields = [
                 'course_code',
                 'title',
                 'author',
                 'description',
                 'price',
                 ]