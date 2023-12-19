# ALIGNED-datapackages

# Create a basic schema for the ALIGNED lci data template

from pprint import pprint
from frictionless import Schema


schema = Schema.describe('data/dummy-lci-table-format.csv') # we start from an existing file
schema.to_json("data/aligned-schema.json") # use schema.to_json for JSON

pprint(schema)

# Modify the schema to add a more extensive description. 
# modificaiton method found here: https://carpentries-incubator.github.io/frictionless-data-agriculture/03-frictionless-tables/index.html

#schema.get_field('Activity database').title = "Some title"
schema.get_field('Activity database').description = "An identifier for the dataset. In principle, a UUID can be used. However, we recommend a readable but sufficiently unique name. "
schema.get_field('Activity code').description = "Given either product exchange or environmental exchange  'ε', this is The UUID of the production exchange of the foreground activity where ε is located. Or the UUID of the environmental exchange"
schema.get_field('Activity name').description = "The name of the foreground activity where ε is located. While multiple activities can in principle have the same name, e.g. “electricity production” as produced by different technologies. We suggest being as specific as possible. Name should be readable and understandable."
schema.get_field('Activity unit').description = "The unit of the production exchange of the foreground activity where ε is located. Or the unit of the environmental exchange"
schema.get_field('Activity type').description = "Two types: “process” for product exchanges (technology matrix) and “biosphere” for environmental exchanges (intervention matrix)"
schema.get_field('Exchange database').description = "The identifier of the database where the exchange ε is located."
schema.get_field('Exchange input').description = "The UUID of ε. A computer generated UUIDs created by the user for foreground exchanges and taken from an existing list for background exchanges."
schema.get_field('Exchange amount').description = "The value of ε"
schema.get_field('Exchange unit').description = "The unit of ε"
schema.get_field('Exchange type').description = "Must be 'production' for the main output (reference flow, there must be one production exchange for each activity). 'Technosphere' for product exchanges other than the main output (e.g. Inputs and co-product outputs). 'Biosphere' for environmental exchanges."
schema.get_field('Exchange uncertainty type').description = "See the stats_arrays package documentation here: https://stats-arrays.readthedocs.io/en/latest/#id22"
schema.get_field('Exchange loc').description = "See the stats_arrays package documentation here: https://stats-arrays.readthedocs.io/en/latest/#id22"
schema.get_field('Exchange scale').description = "See the stats_arrays package documentation here: https://stats-arrays.readthedocs.io/en/latest/#id22"
schema.get_field('Exchange negative').description = "'True', unless the 'amount' field is a negative number then use 'False'"
#schema.get_field('Simapro name').description = "Name of the exchange in Simapro software, e.g. the name used to identify an ecoinvent dataset"
#schema.get_field('Simapro unit').description = "Unit used in SimaPro"
#schema.get_field('Simapro type').description = 'Use "Raw", "Air", "Water", "Soil", "Waste", "Social", "Economic" to indicate exchanges. Use "Wastetotreatment" to indicate database processes of the waste treatment category'



schema.to_json("data/aligned-schema.json") # use schema.to_json for JSON

pprint(schema)

# check that it worked

schema_check = Schema('data/aligned-schema.json') # use schema.to_json for JSON
pprint(schema_check)
schema_check = Schema.from_descriptor('data/aligned-schema.json')
print(schema_check.fields)
print(schema_check.field_names)
print(schema_check.field_types)

# we also validate the schema

from pprint import pprint
from frictionless import validate

report = validate('data/aligned-schema.json')
pprint(report) # all good


