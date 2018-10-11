from aiohttp import web
import json

routes = web.RouteTableDef()

@routes.get('/')
async def get_handler(request):
	data = {'some': 'data'}
	return web.json_response(data)

@routes.post('/')
async def post_handler(request):
	if request.body_exists:
		data = await request.text()
	data = json.loads(data)
	
	return web.Response( text="hello")

app = web.Application()
app.router.add_routes(routes)

web.run_app(app)