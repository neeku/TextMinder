from pyramid.paster import get_app, setup_logging
ini_path = '/sites/taur.is/textminder/test/production.ini'
setup_logging(ini_path)
application = get_app(ini_path, 'main')
