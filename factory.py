from aiohttp import web
import json
import json_api
import pika

routes = web.RouteTableDef()

@routes.get('/')
async def get_handler(request):
	#data = {'some': 'data'}
	data = json_api.take('bd.json')
	return web.json_response(data)

@routes.post('/')
async def post_handler(request):
	if request.body_exists:
		data = await request.text()
	data = json.loads(data)
	json_api.put(data)
	print(json_api.take('bd.json'))

	connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
	channel = connection.channel()
	channel.queue_declare(queue='signal')
	channel.basic_publish(exchange='',
                      routing_key='signal',
                      body=data)
	return web.Response( text="Принято")

app = web.Application()
app.router.add_routes(routes)

web.run_app(app)