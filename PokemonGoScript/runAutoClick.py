import os
import time
import sys,md5

oldfile = ''

def clickAction():
	os.system("./autoClicker -x 1433 -y 536")
	os.system("./autoClicker -x 1433 -y 588")
	time.sleep(1)
	print "clicking!!"

def start():
	global oldfile
	while True:
		f = open('/Users/virgilwu/Downloads/PokemonGoControllerSuite-master/PokemonHandler/PokemonHandler/pokemonLocation.gpx','r')
		md5New = md5.new(f.read()).digest()
		if oldfile == '' or md5New != oldfile:
			oldfile = md5New
			clickAction()
		else:
			time.sleep(1)

start()