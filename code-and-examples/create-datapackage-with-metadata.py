# ALIGNED-datapackages

# create a basic datapackage and schems for the ALIGNED lci data template


from pprint import pprint
from frictionless import Package, Resource

package = Package('data/*') # get all the inventories in the data folder
pprint(package) 

# alternatively, this
# package = Package(['data/dummy-lci-table-format.csv', 'data/seaweed-inventory.csv'])

# Now add specific metadatato the datapackage descriptor
# see here for syntax https://specs.frictionlessdata.io/data-package/#descriptor

package.name = 'aligned-template-datapackage'
package.description = 'A template datapackage used in the ALIGNED project'
package.licenses = [{
  "name": "CC BY-SA 4.0 DEED",
  "path": "https://creativecommons.org/licenses/by-sa/4.0/deed.en",
  "title": "Attribution-ShareAlike 4.0 International" 
  }]
package.sources = [{
  "title": "ALIGNED website",
  "path": "www.alignedproject.eu" 
  }]
package.contributors =[{
  "title": "Massimo Pizzol",
  "email": "massimo@plan.aau.dk",
  "path": "https://vbn.aau.dk/en/persons/117459",
  "role": "Author"
  }]

package.to_json('datapackage.json') # this exports the datapackage file in basic form.

pprint(package)

#testing that things worked as intended

package_check = Package('datapackage.json') # import the file we just created
package_check.name
package_check.resources
