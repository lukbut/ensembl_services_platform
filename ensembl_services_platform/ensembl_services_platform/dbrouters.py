# Inspired from https://datascience.blog.wzb.eu/2017/03/21/using-django-with-an-existinglegacy-database/
def decide_on_model(model):
    """Helper function to ensure all operations of the GeneAutocomplete model are piped to
     the ensembl_website_97 database """
    return 'ensembl_website_97' if model._meta.app_label == 'rest_endpoint' else None


class EnsemblWebsite97DbRouter:
    """
    Implements a database router so that:

    * Django related data - DB alias 'default' - sqlite3 db
    * Existing public "gene_autocomplete" DB table data - DB alias 'ensembl_website_97' - MySQL DB 'ensembl_website_97'
    """
    def db_for_read(self, model, **hints):
        return decide_on_model(model)

    def db_for_write(self, model, **hints):
        return decide_on_model(model)

    def allow_relation(self, obj1, obj2, **hints):
        # Allow any relation if both models are part of the rest_endpoint app
        if obj1._meta.app_label == 'rest_endpoint' and obj2._meta.app_label == 'rest_endpoint':
            return True
        # Allow if neither is part of rest_endpoint app
        elif 'rest_endpoint' not in [obj1._meta.app_label, obj2._meta.app_label]:
            return True
        # by default return None - "undecided"

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        # allow migrations on the "default" (django related data) DB
        if db == 'default' and app_label != 'rest_endpoint':
            return True

        # don't allow migrations on the legacy database too:
        # this will stop us from actually altering the database schema of the ensembl_website_97 DB
        if db == 'ensembl_website_97' and app_label == "rest_endpoint":
            return False

        return False
