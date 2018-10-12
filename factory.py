from aiohttp import web
import json
import json_api
import pika

routes = web.RouteTableDef()

#Клиент запрашивает состояние
@routes.get('/')
async def get_handler(request):
	#data = {'some': 'data'}
	data = json_api.take('bd.json')
	return web.json_response(data)

#Клиент поставляет деталь
@routes.post('/')
async def post_handler(request):
	if request.body_exists:
		data = await request.text()
	data = json.loads(data)
	#отправляем деталь в склад
	json_api.put(data)
	print(json_api.take('bd.json'))
	#отправляем сигнал worker-у
	connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
	channel = connection.channel()
	channel.queue_declare(queue='signal')
	channel.basic_publish(exchange='',
                      routing_key='signal',
                      body=json.dumps(data))
	return web.Response( text="Принято")

app = web.Application()
app.router.add_routes(routes)

web.run_app(app)