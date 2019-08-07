# Ensembl Services Platform
<h3>Introduction</h3>
This guide provides a brief overview of the Ensembl Services Platform, 
which implements the <code>genes</code> endpoint. It describes the 
endpoint's use, including accepted parameters.

<h3>Genes Endpoint Example</h3>

<code>/genes/lookup/hel?species=homo_sapiens</code>

* "hel" is a mandatory gene lookup query, passed as a path parameter
* "homo_sapiens" is an optional query parameter to filter on species

<h3>Example Response</h3>

    [
        {
            "display_label": "HELB",
            "location": "12:66302545-66347645",
            "stable_id": "ENSG00000127311",
            "species": "homo_sapiens"
        },
        {
            "display_label": "HELLPAR",
            "location": "12:102197585-102402596",
            "stable_id": "ENSG00000281344",
            "species": "homo_sapiens"
        },
        {
            "display_label": "HELLS",
            "location": "10:94501434-94613905",
            "stable_id": "ENSG00000119969",
            "species": "homo_sapiens"
        },
        {
            "display_label": "HELQ",
            "location": "4:83407343-83455855",
            "stable_id": "ENSG00000163312",
            "species": "homo_sapiens"
        },
        {
            "display_label": "HELT",
            "location": "4:185018841-185020804",
            "stable_id": "ENSG00000187821",
            "species": "homo_sapiens"
        },
        {
            "display_label": "HELZ",
            "location": "17:67070444-67245989",
            "stable_id": "ENSG00000198265",
            "species": "homo_sapiens"
        },
        {
            "display_label": "HELZ2",
            "location": "20:63558086-63574239",
            "stable_id": "ENSG00000130589",
            "species": "homo_sapiens"
        }
    ]

<h3>Known limitations</h3>

* The gene lookup query is mandatory.
* All parameters must be at least three characters long (if provided).

<h3>Implementation</h3>
This REST API endpoint was created using Django and Django Rest Framework. 

A Django project named `ensembl_services_platform` contains a 
`rest_endpoint` app. The `rest_endpoint` app contains the implementation 
of the `genes` endpoint.

The