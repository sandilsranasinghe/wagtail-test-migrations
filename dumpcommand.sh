python manage.py dumpdata --natural-foreign --indent 2 \
    -e wagtailsearch.indexentry -e contenttypes -e auth.permission \
    -e wagtailcore.groupcollectionpermission -e wagtailcore.grouppagepermission \
    -e wagtailsearch.sqliteftsindexentry \
    -e wagtailimages.rendition -e sessions > fixtures/fixture1.json