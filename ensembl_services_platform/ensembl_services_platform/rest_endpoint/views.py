from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from ensembl_services_platform.rest_endpoint.models import GeneAutocomplete
from ensembl_services_platform.rest_endpoint.serializers import GeneAutocompleteSerializer


class GeneMatcher(APIView):
    """
    A view that returns genes matching the partial gene name passed as path parameter "lookup".
    Optional query parameter "species" further filters the result set by matching the target species.
    e.g. {{url}}/gene_matcher/lookup/<partial_query>?species=<species_query>
    """
    renderer_classes = [JSONRenderer]

    def get(self, request, lookup):
        species = self.request.query_params.get('species', None)

        matching_genes = GeneAutocompleteSerializer(GeneAutocomplete.objects.filter(display_label__iregex=r'^'+lookup),
                                                    many=True)

        if species:
            return Response(species)
        return Response(matching_genes.data)