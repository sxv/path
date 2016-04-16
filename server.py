from bottle import get, post, redirect, run, request, response, static_file, jinja2_view
import functools

view = functools.partial(jinja2_view)


@get('/slides/')
@view('slides.html')
def slides():
  slides = [{
    'label': 'streets',
    'tiles': '/tiles/streets.dzi',
    'thumb': '/tiles/streets.png'
  }, {
    'label': 'birds',
    'tiles': '/tiles/birds.dzi',
    'thumb': '/tiles/birds.jpg'
  },{
    'label': 'world',
    'tiles': '/tiles/world.dzi',
    'thumb': '/tiles/world.png'
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
