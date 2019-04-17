import os

from pulpcore.plugin.models import Artifact, RemoteArtifact
from pulp_2to3_migrate.app.models import Pulp2To3Map
from pulp_file.app.models import FileContent


def handle(pulp2_db):
   iso_collection = pulp2_db.get_collection('units_iso')

   # mongo: get storage path and entry from catalog
   # pulp3: create artifact aand remote artifact
   # only then create a hard link and add unit to Pulp2To3Map

   # noticably slow to do it one by one.
   # suggestion: load all necessary pulp2 data into postgres temp table and do bulk operations and
   # or diff to track progress/starting point