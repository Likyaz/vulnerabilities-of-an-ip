# -*- coding:utf-8 -*-

import os
import datetime
import shodan

SHODAN_API_KEY = "Your key shodan"

api = shodan.Shodan(SHODAN_API_KEY)

try:
		ip = input("Entrer l'ip : ")
		result = api.host(ip)
		
		date = datetime.datetime.now()
		fichier = open("vulns " + ip + ".txt", "a")

		if result.get("vulns", 0) != 0 :
			print("vulnerability :")
			print(result["vulns"])
			fichier.write(str(date) + " : " + str(result["vulns"]) + "\n")
		else :
			print("No vulnerability")
			fichier.write(str(date) + " : No vulnerability!\n")

		fichier.close()

except shodan.APIError as e:
		print('Error:t {}'.format(e))
		exit(1)
