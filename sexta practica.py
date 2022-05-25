
class persona:

   def __init__(self, nombre):
       self.nombre = nombre
       
    def avanza(self):
        print("ando caminando")


class ciclista(persona):

    def __init__(self, nombre): 
        super().__init__(nombre)

    def avanza(self):
        print("ando moviendome en mi bicicleta")

def main():
    persona = persona("david")
    persona.avanza()

    ciclista = ciclista("daniel")
    persona.avanza()

if __name__ == "__main__":
    main()
