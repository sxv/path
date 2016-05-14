from bottle import get, post, redirect, run, request, response, static_file, jinja2_view
import functools

view = functools.partial(jinja2_view)


@get('/slides/')
@view('slides.html')
def slides():
  slides = [{
    'label': 'original',
    'slide1': '/tiles/original.dzi',
    'slide2': '/tiles/heatmap.dzi',
    'thumb': '/tiles/original.thumb.jpg'
  },{
    'label': 'streets',
    'slide1': '/tiles/streets.dzi',
    'slide2': '/tiles/oval.dzi',
    'thumb': '/tiles/streets.thumb.png'
  }, {
    'label': 'globe',
    'slide1': '/tiles/globe.dzi',
    'slide2': '/tiles/oval.dzi',
    'thumb': '/tiles/globe.thumb.jpg'
  }]
  return {'slides': slides}


# Static
@get('/lib/<filepath:path>')
def static_lib(filepath):
  return static_file(filepath, root='lib')

@get('/tiles/<filepath:path>')
def static_tiles(filepath):
  return static_file(filepath, root='tiles')

run(host='0.0.0.0', port=8000, debug=True, reloader=True)
