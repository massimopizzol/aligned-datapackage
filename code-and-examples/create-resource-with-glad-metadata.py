# ALIGNED-datapackages

# Create a resource descriptor for one ALIGNED lci dataset and add GLAD metadata

from pprint import pprint
from frictionless import Resource

resource = Resource("data/dummy-lci-table-format.csv")
resource.infer(stats=True)
pprint(resource)

resource.custom['g_uuid'] = 'String, The unique identifier of the data set, usually a UUID (can be generated from https://www.uuidgenerator.net/)'
resource.custom['g_process_name'] = 'String, The name of the data set (Activity name)'
resource.custom['g_sector'] = 'String, "The sector of the dataset Use "","" to separate multiple values. e.g. Mining, Oher"'
resource.custom['g_process_type'] = 'Enum, The type of process (unit, system, etc.)'
resource.custom['g_description'] = 'String, The description of the data set'
resource.custom['g_valid_from_year'] = 'Ineger, The year of the start of the validity of the data set'
resource.custom['g_valid_until_year'] = 'Integer, The year of the end of the validity of the data set'
resource.custom['g_regional_code'] = 'String (ISO code), The location of the data set'
resource.custom['g_data_format'] = 'Enum, The data format the data set is available in (e.g. ECOSPOLD1, ECOSPOLD2, ILCD,.csv)'
resource.custom['g_lci_modeling'] = 'Enum, The LCI modeling type (attributional, consequential, before modeling)'
resource.custom['g_method_multif'] = 'Enum, Substitution or Allocation'
resource.custom['g_bioc_carbon'] = 'Enum'
resource.custom['g_eol_model'] = 'Enum'
resource.custom['g_water_model'] = 'Enum'
resource.custom['g_infras_model'] = 'Enum'
resource.custom['g_emission_model'] = 'Enum'
resource.custom['g_carbon_storage'] = 'Enum'
resource.custom['g_source_realiability'] = 'Enum'
resource.custom['g_reviewers'] = 'List of strings, A list of the names of the reviewers of the data set Use "","" to separate multiple values. e.g. Bethany Hardy, Ryanne Washington'
resource.custom['g_representativeness'] = 'Double, The percentage of variation coefficient, s/(arithm mean)'
resource.custom['g_deviation_balance'] = 'Double, The deviation in mass and energy balance'
resource.custom['g_copyright_protected'] = 'Boolean, Indicates if the data set is copyright protected'
resource.custom['g_copyright_holder'] = 'String, The owner of the copyright of the data set if applicable'
resource.custom['g_public_accessible'] = 'Boolean, Indicates if the data set can be downloaded from the given dataSetUrl without further login'
resource.custom['g_available_free'] = 'Boolean, Indicates if the data set is available for free'
resource.custom['g_license'] = 'String, The license the data set is released under'
resource.custom['g_contact'] = 'String, A contact person for infomation on the data set'
resource.custom['g_url'] = 'String, A url to download the complete data set, or alternatively, the website of the data provider'



pprint(resource)

resource.to_json("data/dummy-lci-table-format-glad.json") # export the descriptor


# check it's readable
resource_check = Resource("data/dummy-lci-table-format-glad.json")
pprint(resource_check)

resource_check.fields
