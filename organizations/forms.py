from django import forms
from organizations.models import Organization
from common.models import Comment


class OrganizationForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        assigned_users = kwargs.pop('assigned_to', [])
        super(OrganizationForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs = {"class": "form-control"}
        self.fields['description'].widget.attrs.update({
            'rows': '6'})
        self.fields['assigned_to'].queryset = assigned_users
        self.fields['assigned_to'].required = False
        self.fields['teams'].required = False

    class Meta:
        model = Organization
        fields = (
            'assigned_to', 'teams', 'name',
            'phone', 'email', 'website', 'status', 'source',  'address', 'description'
                  )

class OrganizationCommentForm(forms.ModelForm):
    comment = forms.CharField(max_length=64, required=True)

    class Meta:
        model = Comment
        fields = ('comment', 'organization', 'commented_by')