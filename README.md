# Ensembl Services Platform
<h3>Introduction</h3>

This guide provides a brief overview of the Ensembl Services Platform, 
which implements the <code>genes</code> endpoint. It describes the 
endpoint's use, including accepted parameters.

<h3>Genes Endpoint</h3>

The putative "Ensembl Services Platform" allows users to search for a gene by its name. One web
REST service is available on this platform to get all gene names corresponding to a pattern.
The entry point accepts a string as parameter and return the list of matching genes in our
database.

For example, if the user submit brc a list of suggested gene names may be:
• BRCA1
• BRCA2
• BRCC3
• BRCC3P1

Filtering on the gene's species is also available.

<h3>Genes Endpoint Request Example</h3>

<code>/genes/lookup/hel?species=homo_sapiens</code>

* "hel" is a mandatory gene `lookup` example query, passed as a path parameter
* "homo_sapiens" is an optional example query parameter to filter on `species`

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

<h3>Endpoint usage limitations</h3>

* The gene `lookup` path parameter is mandatory.
* All parameters must be at least three characters long (if provided).
* Only GET requests are accepted.
* The `lookup` parameter matching is case insensitive.
* The `species` parameter matching is exact.

<h3>Postman collection</h3>

A [Postman](https://www.getpostman.com) Collection has been published to assist with querying the API.
The collection can be accessed from the following link:
`https://www.getpostman.com/collections/ab2e10897deb4d350c43`

<h3>Implementation Notes</h3>

This REST API endpoint was created using 
[Django](https://www.djangoproject.com) and 
[Django Rest Framework](https://www.django-rest-framework.org). 

A Django project named `ensembl_services_platform` contains a 
`rest_endpoint` app. The `rest_endpoint` app contains the implementation 
of the `genes` endpoint. All files were automatically generated using
inbuilt commands, and unused stubs were retained (including comments with
instructions). 

The data source of the application is the publicly available 
[Ensembl MySQL Database](https://www.ensembl.org/info/data/mysql.html). 
The Django utility `inspectdb` was used to generate models automatically
for all tables in this Database for use with this project. 
A database router was defined to ensure all operations of the 
`GeneAutocomplete` model are piped to the `ensembl_website_97` database.

<h3>Setting up the environment</h3>

The following notes will assist a user in setting up the endpoint on a
MacOS computer for testing purposes.

A `requirements.txt` file is available for easy setup of a site specific
Python virtual environment.

`mysql`, `openssl` and `mysql-connector-c` need to be installed via
[Homebrew](https://brew.sh).

`mysql-connector-c` currently has a bug when used on MacOS. The settings
file needs to be modified, as described in this link: 
<https://pypi.org/project/mysqlclient/>

The following additional commands need to be typed into bash to set up `OpenSSL` on MacOS Mojave 
onwards:

    export CPPFLAGS="-I/usr/local/opt/openssl/include"
    export LDFLAGS="-L/usr/local/opt/openssl/lib"
    export PATH="/usr/local/opt/openssl/bin:$PATH"

<h3>Known issues and assumptions</h3>

1. ```display_name``` field was not found in the ```gene_autocomplete``` 
table, so ```display_label``` was used instead.
2. ```stable_id``` was manually set as the primary key of the model 
```GeneAutocomplete```. Other models had primary keys automatically 
denoted by the ```inspectdb``` command.
3. It is assumed that both parameters need to be at least three 
characters long.
4. Species parameter was assumed to be an exact match only.
5. Assumption that a list of JSON objects is an appropriate format. The
fields returned were not renamed in any way (e.g. ```display_label``` 
field was not renamed to "gene names").

<h3>References</h3>

1. Setting up Django project and Apps: 
<https://www.django-rest-framework.org/tutorial/quickstart/>
2. Connecting Django with a remote MySQL DB: 
<https://gist.github.com/nathanielove/c51f5c4ee1d79045ffa629237e835157>
3. Using Django with an existing legacy database:
<https://datascience.blog.wzb.eu/2017/03/21/using-django-with-an-existinglegacy-database/>
