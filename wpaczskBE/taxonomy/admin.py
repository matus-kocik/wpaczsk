from django.contrib import admin
from taxonomy.models import TaxonomySubspecies, TaxonomyClass, TaxonomyFamily, TaxonomyGenus, TaxonomyKingdom, TaxonomyOrder, TaxonomyPhylum, TaxonomySpecies, TaxonomySubclass, TaxonomySubfamily

admin.site.register([TaxonomyKingdom, TaxonomyPhylum, TaxonomyClass, TaxonomySubclass, TaxonomyOrder, TaxonomyFamily, TaxonomySubfamily, TaxonomyGenus, TaxonomySpecies, TaxonomySubspecies,])
