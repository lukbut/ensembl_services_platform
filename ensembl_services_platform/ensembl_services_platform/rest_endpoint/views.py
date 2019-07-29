from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


class GeneMatcher(APIView):
    """
    A view that returns genes matching the partial gene name passed as path parameter "lookup".
    Optional query parameter "species" further filters the result set by matching the target species.
    e.g. {{url}}/gene_matcher/lookup/<partial_query>?species=<species_query>
    """
    renderer_classes = [JSONRenderer]

    def get(self, request, lookup):
        species = self.request.query_params.get('species', None)

        if species:
            return Response(species)
        return Response(lookup)