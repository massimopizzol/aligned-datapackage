# Readme

## aligned-datapackage

Using the frictionless framework to create data packages, resources, and schema for Life Cycle Inventory (LCI) data generated in the ALIGNED project.



### (Wait, I am not a programmer!)

You can still use the material in this repository. All files can be opened and edited manually using a text editor (Notepad, TextEdit, etc.). You can modify the schema.json, datapackage.json, and resource.json files manually and use them as a starting point for documenting your data.

## About this repository


- Includes code and templates to share, report, and document LCI data. 

- Is designed primarily for foreground LCI data, i.e. new primary data about the product and biosphere exchanges of a relatively restricted number of activities, ideally linked to a background database of secondary data. 

- Is based on the [frictionless standards](https://specs.frictionlessdata.io/) for describing data. The python scripts use the [frictionless framework](https://framework.frictionlessdata.io/) and related libraries.

- Uses the LCI data structure decribed in detail in this [zenodo archive](). This tabular structure mirrors the nomenclature and fields used in the [Brightway open LCA software framework](https://docs.brightway.dev/en/latest/).

- It is intended for both python and non-python users.

- Targets as primary audience the Life Cycle Assessment and Industrial Ecology communities. 

- Allows to include GLAD metadata. GLAD is the [Global LCA Data Access Network](https://www.globallcadataaccess.org/).


- Was developed within the ALIGNED project, [wwww.alignedproject.eu](wwww.alignedproject.eu) Horizon Europe grant agreement N° 101059430. [^1]


 ## Structure of the repository:


Folder [aligned-schema](https://github.com/massimopizzol/aligned-datapackage/tree/main/aligned-schema): 

- includes a base schema for the LCI data structure, the same documented in the [zenodo archive]().
-  In plain words, a [schema](https://specs.frictionlessdata.io/table-schema/#concepts) is here intended as a description of each column of a table of data. This allows to understand the type of data and what the table of data contains. 
-  This schema includes only the recommended, minimal fields to be used to share LCI data. Other fields can be added if needed.
-  Once you have put your LCI data in table format, use this schema to document their structure.

Folder [example-package](https://github.com/massimopizzol/aligned-datapackage/tree/main/example-package):

- Is essentially a template for a [datapackage](https://specs.frictionlessdata.io/data-package/#language) of LCI data.
- Includes a ```datapackage.json``` file, a ```schema.json``` file, and the data (in this context called "resources", in practice these are .csv files) in a separate subfolder. 
- It is thus compliant with [the frictionless framework recommended structure](https://specs.frictionlessdata.io/data-package/#illustrative-structure)
- The ```datapackage.json```file tells which data are included in the package and provides metadata such as author, license, contributors, sources, and description.
- Use this folder as a template to organize and document the LCI data you have.


Folder [code-and-examples](https://github.com/massimopizzol/aligned-datapackage/tree/main/code-and-examples):

- Is primarily for python users. 
- Uses pythorn libraries from the [frictionless framework](https://framework.frictionlessdata.io/) 
- Contains code that can be used to create descriptors for schema, datapackage, and resources.
- In particular [create-resource-with-glad-metadata.py](https://github.com/massimopizzol/aligned-datapackage/blob/main/code-and-examples/create-resource-with-glad-metadata.py) shows how to add GLAD metadata to a LCI tabular resource.

## How to use

The suggested procedure is this

1. Download a copy of the [example-package](https://github.com/massimopizzol/aligned-datapackage/tree/main/example-package) folder. 

2. Prepare LCI data in tabular format using information in the [zenodo archive]() or in the ```aligned-schema.json``` file, example tables available in the repository [aligned-converter repositor](link) or in the [example-package/data](https://github.com/massimopizzol/aligned-datapackage/tree/main/example-package/data) folder. Save the files in .csv format in the ```Data``` subfolder.

4. If needed, based on the tabular structure of the data modify manually the ```schema.json``` file or create one automatically as shown in [create-schema.py](https://github.com/massimopizzol/aligned-datapackage/blob/main/code-and-examples/create-schema.py)

5. Modify manually the datapackage.json file or create one automatically as shown in [ccreate-datapackage-with-metadata.py](https://github.com/massimopizzol/aligned-datapackage/blob/main/code-and-examples/create-datapackage-with-metadata.py)

6. Optionally (but recommended!) create a resource descriptor for each data file using the GLAD metadata fields. See [create-resource-with-glad-metadata.py](https://github.com/massimopizzol/aligned-datapackage/blob/main/code-and-examples/create-resource-with-glad-metadata.py)

7. Share the data in a repository.


### At this point you will have LCI data:

- formatted in a way that can be imported in open source LCA software 

- whose format is clearly documented in a schema, that can be used to validate the datasets and spot errors but alsoo to properly read the data.

- organized in files and directories with a standard structure

- shared and accesible to others (if in a public repository)

- that include essential standard metadata as well as domain-specific GLAD metadata that are recongnized by and relevant for the LCA community


## Contact & info

[Massimo Pizzol](mailto:massimo@plan.aau.dk)


[^1]: _Views and opinions expressed are however those of the author(s) only and do not necessarily reflect those of the European Union or the European Research Executive Agency. Neither the European Union nor the granting authority can be held responsible for them._
