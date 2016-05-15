# Slide-by-slide Viewer

## Dependencies
git
[Conda](http://conda.pydata.org/docs/intro.html)

## Installation
* Clone repo and install python packages
```
git clone <this-repo>
cd path/
conda env create -f environment.yml
source activate slide-by-slide
```
* Generate image tiles and thumbnails:
```
mkdir tiles/
mv <image-file> tiles/
python dzi.py tiles/<image-file>
python thumbgen.py tiles/<image-file>
```
* Add image paths to server.py.  
* Run: `python server.py`

## To do
* Load slide data from JSON rather than hardcoded in server.py
