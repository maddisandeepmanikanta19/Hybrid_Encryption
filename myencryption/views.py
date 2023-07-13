import random
import string

from cryptography.fernet import Fernet
from django.forms import JSONField
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse

from django.views.decorators.csrf import csrf_exempt
import json
from .encryption import *

def index(request):
    return render(request, 'encryption.html')

@csrf_exempt
def generate(request):
	if request.method == "POST":
		# Get the data from the request
		data = request.body.decode("utf-8")
		data = json.loads(data) 

		# Get the selected action
		action = data["action"]

		# Get the input text
		text = data["text"]

		# get number of algo's
		n = data.get('n', 3)

		
		algorithms = []
		for i in range(1, n + 1):
			algorithms.append({
				'name' : data.get(f"algorithm{i}"),
				'key'  : data.get(f"key{i}")
			})

		actions = {
			'encrypt' : {
				'caesar' : caesar_encrypt,
				'playfair': playfair_encrypt,
				'otp': otp_encrypt,
				'railfence': railfence_encrypt
			},
			'decrypt' : {
				'caesar' : caesar_decrypt,
				'playfair' : playfair_decrypt,
				'otp': otp_decrypt,
				'railfence': railfence_decrypt
			}
		}

		# Encrypt or decrypt the text based on the selected action
		output = text
		algo_type = actions[action]

		for algorithm in algorithms:
			func = algo_type[algorithm['name']]
			output = func(output, algorithm['key'])
		
		result = {
			'output': output,
			'algo': algorithms
		}
		# Return the output as a JSON response
		return HttpResponse(output)

	return HttpResponse("NONE")