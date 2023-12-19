# ALIGNED-datapackages

# Create a basic resource descriptor for one ALIGNED lci dataset

from pprint import pprint
from frictionless import Resource

resource = Resource("data/dummy-lci-table-format.csv")
resource.infer(stats=True)
pprint(resource)

resource.schema = "aligned-schema.json" # change the schema to use the aligned one.
resource.to_json("data/dummy-lci-table-format.json") # export the descriptor

resource_check = Resource("data/dummy-lci-table-format.json")
pprint(resource_check)

# attempting a validation
from frictionless import describe

resource = describe('seaweed-inventory.csv')
pprint(resource)
resource.to_json('seaweed.resource.json')

from frictionless import validate

report = validate('seaweed.resource.json')
print(report.to_summary())
report


# attempting a validation to see if it matches with the ALIGNED schema
# make sure the aligned-schema is in the same directory as the script.

from frictionless import describe
from frictionless import validate


resource = describe('data/seaweed-inventory.csv')
resource.schema = "aligned-schema.json" # change the schema to use the aligned one.
pprint(resource)
resource.to_json('seaweed.resource-as.json') # as = "aligned schema" need to expo

report = validate('seaweed.resource-as.json')
print(report.to_summary()) # a lot of mistakes because the schema is missing the fields about pedigree.

print(report) # an even more extensive report. 



resource2.custom['UUID'] = 'd62756fe-a94b-11ed-afa1-0242ac120002'
#resource.custom["customKey2"] = "Value2"
resource2.to_json("resource-updated.json")

pprint(resource2)
xxx = Resource("resource-updated.json")

print(xxx)
