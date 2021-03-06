#-*- coding: utf-8 -*-
import pygame, sys
from pygame.locals import *

pygame.init()

visor = pygame.display.set_mode((560,560))
pygame.display.set_caption("ajedrez")

casilla=[0,0,70,140,210,280,350,420,490,560,999]

ocupadas=[
[0,0,0,0,0,0,0,0,0],#esta linia y el 0 de mas es para kitar el 0 de los indices
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0]
]

def ud7(num):
	if num == 1:
		return 2
	if num == 2:
		return 7

def comepieza(pieza):
	pieza.cambiasilla(9,9)

def muevepieza(pieza,ncasx,ncasy):
	pieza.cambiasilla(ncasx,ncasy)

def	sacapieza(casillax,casillay):
	for b in range(1,9):
		if (casillax,casillay) == (peonegro[b].casx,peonegro[b].casy):
			return peonegro[b]
		elif (casillax,casillay) == (peonblanco[b].casx,peonblanco[b].casy):
			return peonblanco[b]
	for c in (1,2):
		if (casillax,casillay) == (caballonegro[c].casx,caballonegro[c].casy):
			return caballonegro[c]
		elif (casillax,casillay) == (caballoblanco[c].casx,caballoblanco[c].casy):
			return caballoblanco[c]
		elif (casillax,casillay) == (torrenegra[c].casx,torrenegra[c].casy):
			return torrenegra[c]
		elif (casillax,casillay) == (torreblanca[c].casx,torreblanca[c].casy):
			return torreblanca[c]
		elif (casillax,casillay) == (alfilnegro[c].casx,alfilnegro[c].casy):
			return alfilnegro[c]
		elif (casillax,casillay) == (alfilblanco[c].casx,alfilblanco[c].casy):
			return alfilblanco[c]
	if (casillax,casillay) == (reynegro.casx,reynegro.casy):
		return reynegro
	elif (casillax,casillay) == (reyblanco.casx,reyblanco.casy):
		return reyblanco
	elif (casillax,casillay) == (reinanegra.casx,reinanegra.casy):
		return reinanegra
	elif (casillax,casillay) == (reinablanca.casx,reinablanca.casy):
		return reinablanca
		
def sacasilla(posraton):
	for i in range(9):
		if casilla[i] < posraton[0] <= casilla[i+1]:
			x = i
		if casilla[i] < posraton[1] <= casilla[i+1]:
			y = i
	return x,y

class metapieza():
	def __init__(self,x,y,color):
		self.casx=x
		self.casy=y
		self.posx=casilla[x]
		self.posy=casilla[y]
		self.color=color
		if self.casx < 9 and self.casy < 9:
			ocupadas[self.casy][self.casx] = self.color
	def cambiasilla(self,x,y):
		ocupadas[self.casy][self.casx] = 0
		self.__init__(x,y)
	def casillaocupada(self):
		return self.casy,self.casx
	def movlineal(self,movmax=8):
		casi = 0
		oriz = 1
		ordr = 1
		vrar = 1
		vrab = 1
		casposibles=[]
		while casi < movmax:
			casi+=1
			if 0 < self.casy <= 8 and 0 < self.casx-casi <= 8 and oriz == 1:		
				if ocupadas[self.casy][self.casx-casi] == self.color:
					oriz = 0
				else:
					casposibles.append((self.casx-casi,self.casy))
					if ocupadas[self.casy][self.casx-casi] == 3-self.color:
						oriz = 0	
			if 0 < self.casy <= 8 and 0 < self.casx+casi <= 8 and ordr == 1:		
				if ocupadas[self.casy][self.casx+casi] == self.color:
					ordr = 0
				else:
					casposibles.append((self.casx+casi,self.casy))
					if ocupadas[self.casy][self.casx+casi] == 3-self.color:
						ordr = 0					
			if 0 < self.casy-casi <= 8 and 0 < self.casx <= 8 and vrab == 1:		
				if ocupadas[self.casy-casi][self.casx] == self.color:
					vrab = 0
				else:
					casposibles.append((self.casx,self.casy-casi))
					if ocupadas[self.casy-casi][self.casx] == 3-self.color:
						vrab = 0	
			if 0 < self.casy+casi <= 8 and 0 < self.casx <= 8 and vrar == 1:		
				if ocupadas[self.casy+casi][self.casx] == self.color:
					vrar = 0
				else:
					casposibles.append((self.casx,self.casy+casi))
					if ocupadas[self.casy+casi][self.casx] == 3-self.color:
						vrar = 0
		for casazul in casposibles:
			visor.blit(puntoazul,(casilla[casazul[0]],casilla[casazul[1]]))
		return casposibles
	def movdiagonal(self,movmax=8):
		casi = 0
		ariz = 1
		abdr = 1
		ardr = 1
		abiz = 1
		casposibles=[]
		while casi < movmax:
			casi+=1
			if 0 < self.casy-casi <= 8 and 0 < self.casx-casi <= 8 and ariz == 1:		
				if ocupadas[self.casy-casi][self.casx-casi] == self.color:
					ariz = 0
				else:
					casposibles.append((self.casx-casi,self.casy-casi))
					if ocupadas[self.casy-casi][self.casx-casi] == 3-self.color:
						ariz = 0	
			if 0 < self.casy+casi <= 8 and 0 < self.casx+casi <= 8 and abdr == 1:		
				if ocupadas[self.casy+casi][self.casx+casi] == self.color:
					abdr = 0
				else:
					casposibles.append((self.casx+casi,self.casy+casi))
					if ocupadas[self.casy+casi][self.casx+casi] == 3-self.color:
						abdr = 0	
			if 0 < self.casy-casi <= 8 and 0 < self.casx+casi <= 8 and ardr == 1:		
				if ocupadas[self.casy-casi][self.casx+casi] == self.color:
					ardr = 0
				else:
					casposibles.append((self.casx+casi,self.casy-casi))
					if ocupadas[self.casy-casi][self.casx+casi] == 3-self.color:
						ardr = 0	
			if 0 < self.casy+casi <= 8 and 0 < self.casx-casi <= 8 and abiz == 1:		
				if ocupadas[self.casy+casi][self.casx-casi] == self.color:
					abiz = 0
				else:
					casposibles.append((self.casx-casi,self.casy+casi))
					if ocupadas[self.casy+casi][self.casx-casi] == 3-self.color:
						abiz = 0
		for casazul in casposibles:
			visor.blit(puntoazul,(casilla[casazul[0]],casilla[casazul[1]]))
		return casposibles

class metaballo():
	def movcaballo(self):
		casposibles=[]
		listaprobar=[-2,-1,1,2]
		num = 0
		for x in listaprobar:
			for y in [-(3-abs(x)),3-abs(x)]:#idea de papa + eficiente
				if 0 < self.casy+y <= 8 and 0 < self.casx+x <= 8:
					if ocupadas[self.casy+y][self.casx+x] == 0 or ocupadas[self.casy+y][self.casx+x] == 3-self.color:
						visor.blit(puntoazul,(casilla[self.casx+x],casilla[self.casy+y]))
						casposibles.append((self.casx+x,self.casy+y))
						num += 1
		return casposibles

class metapeon():
	def movpeon(self):
		casposibles=[]
		lpeon=[0,-1,1,7,2,5,4]
		if 0 < self.casy+lpeon[self.color] <= 8 and 0 < self.casx <= 8:
			if ocupadas[self.casy+lpeon[self.color]][self.casx] < 1:	
				casposibles.append((self.casx,self.casy+lpeon[self.color]))
				if self.casy == lpeon[self.color+2] and ocupadas[lpeon[self.color+4]][self.casx] < 1:
					casposibles.append((self.casx,lpeon[self.color+4]))
		if 0 < self.casy+lpeon[self.color] <= 8 and 0 < self.casx+1 <= 8:
			if ocupadas[self.casy+lpeon[self.color]][self.casx+1] == 3-self.color:
				casposibles.append((self.casx+1,self.casy+lpeon[self.color]))
		if 0 < self.casy+lpeon[self.color] <= 8 and 0 < self.casx-1 <= 8:
			if ocupadas[self.casy+lpeon[self.color]][self.casx-1] == 3-self.color:
				casposibles.append((self.casx-1,self.casy+lpeon[self.color]))
		for casazul in casposibles:
			visor.blit(puntoazul,(casilla[casazul[0]],casilla[casazul[1]]))
		return casposibles
			
class creapeonegro(metapieza,metapeon):
	def __init__(self,x,y=2):
		self.foto = pygame.image.load('peonegro.png')
		metapieza.__init__(self,x,y,2)
	def puedemovera(self):
		return metapeon.movpeon(self)

class creapeonblanco(metapieza,metapeon):
	def __init__(self,x,y=7):
		self.foto = pygame.image.load('peonblanco.png')
		metapieza.__init__(self,x,y,1)
	def puedemovera(self):
		return metapeon.movpeon(self)

class creacaballonegro(metapieza,metaballo):
	def __init__(self,x,y=1):
		self.foto = pygame.image.load('caballonegro.png')
		metapieza.__init__(self,x,y,2)
	def puedemovera(self):
		return metaballo.movcaballo(self)

class creacaballoblanco(metapieza,metaballo):
	def __init__(self,x,y=8):
		self.foto = pygame.image.load('caballoblanco.png')
		metapieza.__init__(self,x,y,1)
	def puedemovera(self):
		return metaballo.movcaballo(self)

class creatorrenegra(metapieza):
	def __init__(self,x,y=1):
		self.foto = pygame.image.load('torrenegra.png')
		metapieza.__init__(self,x,y,2)
	def puedemovera(self):
		return metapieza.movlineal(self)			

class creatorreblanca(metapieza):
	def __init__(self,x,y=8):
		self.foto = pygame.image.load('torreblanca.png')
		metapieza.__init__(self,x,y,1)
	def puedemovera(self):
		return metapieza.movlineal(self)	

class crealfilnegro(metapieza):
	def __init__(self,x,y=1):
		self.foto = pygame.image.load('alfilnegro.png')
		metapieza.__init__(self,x,y,2)
	def puedemovera(self):
		return metapieza.movdiagonal(self)	

class crealfilblanco(metapieza):
	def __init__(self,x,y=8):
		self.foto = pygame.image.load('alfilblanco.png')
		metapieza.__init__(self,x,y,1)
	def puedemovera(self):
		return metapieza.movdiagonal(self)

largo = 2
class creareynegro(metapieza):
	def __init__(self,x=5,y=1):
		self.foto = pygame.image.load('reynegro.png')
		metapieza.__init__(self,x,y,2)
	def puedemovera(self):
		posimov=[]
		posimov.append(metapieza.movlineal(self,1))
		posimov.append(metapieza.movdiagonal(self,1))
		casposibles=[]
		global largo
		if self.casx == 5 and self.casy == 1:
			if sacapieza(8,1) == torrenegra[2] and \
			ocupadas[self.casy][self.casx+2] == 0 and ocupadas[self.casy][self.casx+1] == 0:
				visor.blit(puntoazul,(casilla[self.casx+2],casilla[self.casy]))
				casposibles.append((self.casx+2,self.casy)) 
				largo = 0
			if sacapieza(1,1) == torrenegra[1] and \
			ocupadas[self.casy][self.casx-3] == 0 and ocupadas[self.casy][self.casx-2] == 0 \
			and ocupadas[self.casy][self.casx-1] == 0:
				visor.blit(puntoazul,(casilla[self.casx-2],casilla[self.casy]))
				casposibles.append((self.casx-2,self.casy))
				largo = 1 
		posimov.append(casposibles)
		return posimov

class creareyblanco(metapieza):
	def __init__(self,x=5,y=8):
		self.foto = pygame.image.load('reyblanco.png')
		metapieza.__init__(self,x,y,1)
	def puedemovera(self):
		posimov=[]
		posimov.append(metapieza.movlineal(self,1))
		posimov.append(metapieza.movdiagonal(self,1))
		casposibles=[]
		global largo
		if self.casx == 5 and self.casy == 8:
			if sacapieza(8,8) == torreblanca[2] and \
			ocupadas[self.casy][self.casx+2] == 0 and ocupadas[self.casy][self.casx+1] == 0:
				visor.blit(puntoazul,(casilla[self.casx+2],casilla[self.casy]))
				casposibles.append((self.casx+2,self.casy))
				largo = 0
			if sacapieza(1,8) == torreblanca[1] and \
			ocupadas[self.casy][self.casx-3] == 0 and ocupadas[self.casy][self.casx-2] == 0 \
			and ocupadas[self.casy][self.casx-1] == 0:
				visor.blit(puntoazul,(casilla[self.casx-2],casilla[self.casy]))
				casposibles.append((self.casx-2,self.casy))
				largo = 1 
		posimov.append(casposibles)
		return posimov

class creareinanegra(metapieza):
	def __init__(self,x=4,y=1):
		self.foto = pygame.image.load('reinanegra.png')
		metapieza.__init__(self,x,y,2)
	def puedemovera(self):
		posimov=[]
		posimov+=metapieza.movlineal(self)
		posimov+=metapieza.movdiagonal(self)
		return posimov

class creareinablanca(metapieza):
	def __init__(self,x=4,y=8):
		self.foto = pygame.image.load('reinablanca.png')
		metapieza.__init__(self,x,y,1)
	def puedemovera(self):
		posimov=[]
		posimov+=metapieza.movlineal(self)
		posimov+=metapieza.movdiagonal(self)
		return posimov
			
puntoazul = pygame.image.load('puntoazul.png')
gblancas = pygame.image.load('gblancas.png')
gnegras = pygame.image.load('gnegras.png')

peonegro = [None]
peonblanco = [None]
caballonegro = [None]
caballoblanco = [None]
torrenegra = [None]
torreblanca = [None]
alfilnegro = [None]
alfilblanco = [None]

for p in range(1,9):#1-8
	peonegro.append(creapeonegro(p))
	peonblanco.append(creapeonblanco(p))

for c in (1,2):
	caballonegro.append(creacaballonegro(ud7(c)))
	caballoblanco.append(creacaballoblanco(ud7(c)))
	torrenegra.append(creatorrenegra(pow(c,3)))
	torreblanca.append(creatorreblanca(pow(c,3)))
	alfilnegro.append(crealfilnegro(c*3))
	alfilblanco.append(crealfilblanco(c*3))

reynegro = creareynegro()
reyblanco = creareyblanco()

reinanegra = creareinanegra()
reinablanca = creareinablanca()

tablero=pygame.image.load('tablero-ajedrez.png')

cliked=[]

fichamover=""
turno="blancas"
print "empiezan las blancas"

while True:
	for evento in pygame.event.get():
		if evento.type == QUIT:
			pygame.quit()
			sys.exit()
		if evento.type == MOUSEBUTTONDOWN:
			cliked.append(pygame.mouse.get_pos())
			if len(cliked) > 1:
				cliked[0] = cliked[1]

	visor.blit(tablero,(0,0))

	if len(cliked) == 1:#primer click
		posraton = cliked[0]
		casillax,casillay=sacasilla(posraton)
		rey=0
		fichamover=sacapieza(casillax,casillay)
		if (fichamover == None) or (fichamover.color == 1 and turno == "negras") or (fichamover.color == 2 and turno == "blancas"):
			fichamover=""#anula movimientos del otro turno
		else:
			posimov = fichamover.puedemovera()
		if fichamover == reynegro or fichamover == reyblanco:
			rey=1
		if fichamover=="":
			cliked=[]

	if len(cliked) == 2:#segundo click
		posraton = cliked[0]
		nuevacasillax,nuevacasillay = sacasilla(posraton)
		if rey == 0:
			if (nuevacasillax,nuevacasillay) in posimov:
				if ocupadas[nuevacasillay][nuevacasillax] != 0:
					comepieza(sacapieza(nuevacasillax,nuevacasillay))
				muevepieza(fichamover,nuevacasillax,nuevacasillay)
				if fichamover.color == 1:
					turno = "negras"
				else:
					turno = "blancas"
		else:
			if (nuevacasillax,nuevacasillay) in posimov[0] or \
			(nuevacasillax,nuevacasillay) in posimov[1] or \
			(nuevacasillax,nuevacasillay) in posimov[2]:
				if ocupadas[nuevacasillay][nuevacasillax] != 0:
					comepieza(sacapieza(nuevacasillax,nuevacasillay))
				
				if fichamover == reynegro:
					if (nuevacasillax,nuevacasillay) in posimov[2]:
						if largo == 0:
							muevepieza(torrenegra[2],6,1)
						else:
							muevepieza(torrenegra[1],4,1)
					muevepieza(reynegro,nuevacasillax,nuevacasillay)
					turno = "blancas"
				
				if fichamover == reyblanco:
					if (nuevacasillax,nuevacasillay) in posimov[2]:
						if largo == 0:
							muevepieza(torreblanca[2],6,8)
						else:
							muevepieza(torreblanca[1],4,8)
					muevepieza(reyblanco,nuevacasillax,nuevacasillay)
					turno = "negras"

	#refrescos y representaciones
	for d in range(1,9):
		visor.blit(peonblanco[d].foto, (peonblanco[d].posx,peonblanco[d].posy))
		visor.blit(peonegro[d].foto, (peonegro[d].posx,peonegro[d].posy))
		
	for e in (1,2):
		visor.blit(torrenegra[e].foto, (torrenegra[e].posx,torrenegra[e].posy))
		visor.blit(torreblanca[e].foto, (torreblanca[e].posx,torreblanca[e].posy))
		
		visor.blit(alfilnegro[e].foto, (alfilnegro[e].posx,alfilnegro[e].posy))
		visor.blit(alfilblanco[e].foto, (alfilblanco[e].posx,alfilblanco[e].posy))
		
		visor.blit(caballoblanco[e].foto, (caballoblanco[e].posx,caballoblanco[e].posy))
		visor.blit(caballonegro[e].foto, (caballonegro[e].posx,caballonegro[e].posy))
	
	visor.blit(reynegro.foto, (reynegro.posx,reynegro.posy))
	visor.blit(reyblanco.foto, (reyblanco.posx,reyblanco.posy))
	
	visor.blit(reinanegra.foto, (reinanegra.posx,reinanegra.posy))
	visor.blit(reinablanca.foto, (reinablanca.posx,reinablanca.posy))
	
	if reynegro.casx > 8:
		visor.blit(gblancas,(0,0))
	elif reyblanco.casx > 8:
		visor.blit(gnegras,(0,0))

	pygame.display.update()
	if len(cliked) > 1:
		cliked=[]
		fichamover=""
	
	pygame.time.wait(20)#limita a 50 fps para ahorrar cpu
