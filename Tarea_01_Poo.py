
'''clase_01'''

# clase padre 

class Electrodomestico():
    def __init__(self, nombre):
        self.nombre = nombre
        self.estado = False
    
    def encenderE(self):
        if self.estado == False:
            self.estado = True
            print('se ha encendido ', self.nombre)
        else:
            print('El electrodomestio ya estaba encendido')

    def apagarE(self):
        if self.estado == True:
            self.estado =False
            print('se ha apagado ', self.nombre)
        else:
            print('el electrdomestico ya estab encendido')

# clase hijo

class Televisin(Electrodomestico):
    def cambiar_canal(self):
        if self.estado == True:
            print('cambiado de canal')

# instanciar

tel = Televisin("Television LG")
tel.encenderE()
tel.cambiar_canal()
tel.apagarE()

'''clase_02'''

# clase padre 

class Persona():
    def __init__(self, nombre, ci, año_nacimiento):
        self.nombre = nombre
        self.ci = ci
        self.año_nacimiento = año_nacimiento
    def edad(self):
        return 2020-self.año_nacimiento

    def __str__(self):
        return 'nombre: {}, ci: {}, año de ancimietno: {}'.format(self.nombre, self.ci, self.año_nacimiento)

#clase hijo

class Jugador(Persona):
    def CiDelJugador(self):
        return self.ci

#istanciar

p1 = Persona('juan', 999999, 1990)
print(p1)
print(p1.edad())

ju1 = Jugador('mario', 555555, 1999)
print(ju1)
print(ju1.CiDelJugador())