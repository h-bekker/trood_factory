import pika
import json
import json_api

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='signal')

def callback(ch, method, properties, body):
    print("[x] Received %r" % (body,))
    data = json.loads(body)
    for key, value in data.items():
    	part = value
    db = json_api.take('bd.json')
    product = True
    for key, value in part.items():
    	if key in db:
    		if db[key] < part[key]:
    			product = False
    			break
    	else:
    		product = False
    		break
    if product:
    	for key, value in part.items():
    		db[key] -= part[key]
    		json_api.put(dict({key:db[key]}))
    		if db[key]==0:
    			json_api.delete(key)
    else:
    	for key, _ in data.items():
    		json_api.delete(key)
    db = json_api.take('bd.json')
    for key, value in db.items():
    	print(key, value)

channel.basic_consume(callback,
                      queue='signal',
                      no_ack=True)

channel.start_consuming()