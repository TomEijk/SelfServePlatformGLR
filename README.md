# Self-Serve Platform MODELS

This repository / data set contains coded models and data from a qualitative study on the self-serve platform principle in Data Mesh. 

**IMPORTANT:** Please note that the Code in the repository only regenerates the PlantUML models and the Latex tables used in the paper. Mainly, this artifact contains the data on the open and axial coding, as well as the formal coding in Python.
This repository / data set contains the following elements:

*	The open coding data for each of the sources can be found a separate .md file in the folder:`field_notes_open_coding_axial_coding`
*	In each file we also documented the axial coding steps performed in the coded models, to ensure traceability between open coding and formal coding in Python
*	All classes and instances are in the `self_serve_platform_models` folder
  -	The file `self_serve_platform_models.py` contains all models of ADDs
*	The `generators` folder contains generators for Plant UML models. These are generated into `_generated'.


## Getting Started

In order to generate the files, [Codeable Models](https://github.com/uzdun/CodeableModels/)  and [PlantUML](http://plantuml.com/download) must be downloaded and installed.

Take a look at:

```
generators/generate_all.py
```

which generates all figures for the models and .md/latex files. Run it in the `generators` directory using:

```
python .\generate_all.py
```

### Prerequisites / Installing

[PlantUML](http://plantuml.com/download)'s jar file and  
[Codeable Models](https://github.com/uzdun/CodeableModels/) 
are required and the PYTHONPATH must be correctly set:

* The directory containing `codeableModels` and `plantUMLRenderer` must be on the PYTHONPATH.
* The directory containing this project must be on the PYTHONPATH.

See plant_uml_renderer directory in [Codeable Models](https://github.com/uzdun/CodeableModels/) for instructions how
to set up the plant UML jar. Without further configuration it is assumed to be in the default directory:

```
self.directory = "../_generated"
self.plant_uml_jar_path = "../../libs/plantuml.jar"
```

## Running the tests

TBD

## Deployment

TBD

## Built With

* [Codeable Models](https://github.com/uzdun/CodeableModels/) - Modelling platform
* [PlantUML](http://plantuml.com/download) - Generate figures

## Author

* **Tom van Eijk** - [https://github.com/TomEijk/](https://github.com/TomEijk/)

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE)
file for details

