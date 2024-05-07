from django.contrib import admin

from taxonomy.models import (TaxonomyClass, TaxonomyFamily, TaxonomyGenus,
                            TaxonomyKingdom, TaxonomyOrder, TaxonomyPhylum,
                            TaxonomySpecies, TaxonomySubclass,
                            TaxonomySubfamily, TaxonomySubspecies)

admin.site.register(TaxonomyKingdom)
admin.site.register(TaxonomyPhylum)
admin.site.register(TaxonomyClass)
admin.site.register(TaxonomySubclass)
admin.site.register(TaxonomyOrder)
admin.site.register(TaxonomyFamily)
admin.site.register(TaxonomySubfamily)
admin.site.register(TaxonomyGenus)
admin.site.register(TaxonomySpecies)
admin.site.register(TaxonomySubspecies)
