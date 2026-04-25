# O --> Las clases tienen que estra abiertas para la extension y cerrada oar la modificción

class Notificador:
    def __init__(self, usuario, mensaje):
        self.usuario = usuario
        self.mensaje = mensaje
        
    def notificar(self):
        raise NotImplementedError
    
    
class NotificadorEmail(Notificador):
    def notificar(self):
        print(f"Enviando mensaje por MAIL a {self.usuario.email}")
        
class NotificadorSMS(Notificador):
    def notificar(self):
        print(f"Enviando mensaje por SMS a {self.usuario.sms}")
        
        
class NotificadorWhatsApp(Notificador):
    def notificar(self):
        print(f"Enviando mensaje por WhatsApp a {self.usuario.WhatsApp}")