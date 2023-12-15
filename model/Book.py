class Book:

    def __init__(self,titulo,autor,anyo,description):   
        self.titulo = titulo
        self.autor = autor
        self.anyo = anyo
        self.description = description

    def toDBCollection(self):
        return {
            "titulo" : self.titulo,
            "autor" : self.autor,
            "anyo" : self.anyo,
            "description" : self.description
            }

    def __str__(self):
        return "Titulo: %s - Autor: %s - Anyo: %s - description: %s"%(self.titulo,
            self.autor,self.anyo,self.description)