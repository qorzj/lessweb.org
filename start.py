from lessweb_org.index import app


if __name__ == '__main__':
    from aiohttp import web
    from aiohttp_wsgi import WSGIHandler

    aioapp = web.Application()

    aioapp.router.add_static('/static/', path='static')
    aioapp.router.add_route("*", "/{path_info:.*}", WSGIHandler(app.wsgifunc()))

    web.run_app(aioapp, port=8080)