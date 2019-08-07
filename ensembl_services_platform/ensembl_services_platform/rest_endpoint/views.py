from django.core.exceptions import SuspiciousOperation
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
        # Retrieving query parameter, species
        species = self.request.query_params.get('species', None)

        # Validating parameters' length
        if len(lookup) < 3 or species and len(species) < 3:
            raise SuspiciousOperation('Parameter values require a length of 3 or more.')

        # Filtering on lookup value using case insensitive regex matching
        matching_genes = GeneAutocomplete.objects.filter(display_label__iregex=r'^'+lookup)

        # Adding further filtering
        if species:
            matching_genes = matching_genes.filter(species=species)
        # Serializing the result
        return Response(GeneAutocompleteSerializer(matching_genes, many=True).data)
