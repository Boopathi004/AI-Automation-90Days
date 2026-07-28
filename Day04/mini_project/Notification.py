class Notification:
    def send(self):
        print("notification send")
class Emailnotification(Notification):
    def send(self):
        print("Email Notification send ")
class SMSnotification(Notification):
    def send(self):
        print("SMS Notification send")
class WhatsappNotification(Notification):
    def send(self):
        print("whatsappnotification send")

notification=[Emailnotification(),SMSnotification(),WhatsappNotification()]

for notify in notification:
    notify.send()