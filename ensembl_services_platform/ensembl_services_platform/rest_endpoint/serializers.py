from rest_framework import serializers
from ensembl_services_platform.rest_endpoint.models import GeneAutocomplete


class GeneAutocompleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneAutocomplete
        fields = ['species', 'stable_id', 'display_label', 'location']
