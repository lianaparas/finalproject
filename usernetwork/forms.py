from django import forms

from person.models import Dataset, Centrality, Graph

class LoadGraph(forms.ModelForm):
	class Meta:
		model = person
		field = '__all__'

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		sel.field['centrality'].queryset = Centrality.objects.none()

		if 'dataset' in self.data:
			try:
				dataset_id = int(self.data.get('dataset'))
				self.fields['centrality'].queryset = Centrality.objects.filter(dataset_id=dataset_id).order_by('name')
				expect (ValueError, TypeError):
				pass #invalid input from the client; ignore and fallback to empty City queryset
			elif self.instance.pk:
				self.fields['centrality'].queryset = self.instance.dataset.centrality_set.order_by('name')