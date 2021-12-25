import django_filters
from .models import Boat

# Filter function to filter down all boats
# @param:   django_filters.FilterSet -> Django built-in Filter to generate filters
class BoatFilter(django_filters.FilterSet):
	class Meta:
		model = Boat
		fields = ('model', 'current_step')