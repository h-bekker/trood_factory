import unittest
import requests

class ClientTest(unittest.TestCase):
	def test1(self):
		r = requests.get('http://127.0.0.1:8080/reset')

		data = {"суперштучка":{"часы":2, "шоколад": 1}}
		r = requests.post('http://127.0.0.1:8080', json=data)

		r = requests.get('http://127.0.0.1:8080')
		print(r.text.encode('utf-8').decode('unicode-escape'))
		self.assertEqual(r.text.encode('utf-8').decode('unicode-escape'), '{"абырвалг": 10, "ручка": 5, "greenfield": 7, "шоколад": 3, "часы": 1}')

	def test2(self):
		r = requests.get('http://127.0.0.1:8080/reset')

		data = {"суперштучка":{"абырвалг":7, "greenfield": 5}}
		r = requests.post('http://127.0.0.1:8080', json=data)

		r = requests.get('http://127.0.0.1:8080')
		print(r.text.encode('utf-8').decode('unicode-escape'))
		self.assertEqual(r.text.encode('utf-8').decode('unicode-escape'), '{"абырвалг": 3, "ручка": 5, "greenfield": 2, "шоколад": 3, "часы": 1, "суперштучка": {"абырвалг": 7, "greenfield": 5}}')

	def test3(self):
		r = requests.get('http://127.0.0.1:8080/reset')

		data = {"суперштучка":{"ручка":3, "шоколад": 3, "greenfield": 7}}
		r = requests.post('http://127.0.0.1:8080', json=data)

		r = requests.get('http://127.0.0.1:8080')
		print(r.text.encode('utf-8').decode('unicode-escape'))
		self.assertEqual(r.text.encode('utf-8').decode('unicode-escape'), '{"абырвалг": 10, "ручка": 2, "часы": 1, "суперштучка": {"ручка": 3, "шоколад": 3, "greenfield": 7}}')

if __name__ == '__main__':
	unittest.main()