# slide viewer

## Dependencies
[Conda](http://conda.pydata.org/docs/intro.html)

## Installation
```
cd path
conda env create -f environment.yml
source activate slide-by-slide
```
Generate image tiles and thumbnail
```
mkdir tiles
mv <image-file> tiles
python dzi.py tiles/<image-file>
python thumbgen.py tiles/<image-file>
```
Add image paths to server.py  
Run: `python server.py`

## TODO:
1. Autogenerate JSON file with image paths
