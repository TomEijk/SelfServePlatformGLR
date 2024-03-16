# Self-Serve Platform MODELS

This repository / data set contains coded models and data from a qualitative study on the self-serve platform principle in Data Mesh. 

**IMPORTANT:** Please note that the Code in the repository only regenerates the PlantUML models and the Latex tables used in the paper. Mainly, this artifact contains the data on the open and axial coding, as well as the formal coding in Python.
This repository / data set contains the following elements:

*	The open coding data for each of the sources can be found a separate .md file in the folder:`field_notes_open_coding_axial_coding`
*	In each file we also documented the axial coding steps performed in the coded models, to ensure traceability between open coding and formal coding in Python
*	All classes and instances are in the `self_serve_platform_models` folder
  -	The file `self_serve_platform_models.py` contains all models of ADDs
*	The `generators` folder contains generators for Plant UML models. These are generated into `_generated'.

### Prerequisites / Installing

At first, make sure the Self_Serve_Platform_GLR is set as your working directory. 

Next, the correct PYTHONPATH must be set. 
Run the following command in your terminal:

For Windows:

```
set PYTHONPATH=%PYTHONPATH%;..\CodeableModels
```

For MacOS:

```
export PYTHONPATH=$PYTHONPATH:../CodeableModels   
```

## Getting Started

Make sure you have python3 installed in your terminal and run the following command:

```
python3 self_serve_platform_codeablemodels/generators
```

## Built With

* [Codeable Models](https://github.com/uzdun/CodeableModels/) - Modelling platform
* [PlantUML](http://plantuml.com/download) - Generate figures

## Author

* **Tom van Eijk** - [https://github.com/TomEijk/](https://github.com/TomEijk/)

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE)
file for details

