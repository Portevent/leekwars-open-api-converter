# leekwars-open-api-converter
Convert Leekwars api documentation into OpenAPI specifications.
- Leekwars api documentation can be fetched at https://leekwars.com/api/service/get-all, and a local version can be found at [input.json](./input.json) (fetched 10th of December 2025)
- OpenAPI convertion can be found at [output.json](./output.json)

# How to run it 
If you want to try it out localy
- clone the project
- fetch the new version of [leekwars docs](https://leekwars.com/api/service/get-all)
- replace old input.json with your new version
- optionnal : create your venv and install json : `python -m venv venv` and `pip install json`
- run main.py : `python main.py`
- updated open api docs should be in `output.json`