from mailtm import Email

def listener(message):
  print("\nSubject: " + message['subject'])
  print("Content: " + message['text'] if message['text'] else message['html'])


#Domain
mail = Email()
print("\nDomain; " + mail.domain)

#new email address
mail.register()
print("\nEmail Address; " + str(mail.address))

#start mail
mail.start(listener)
print("\nWaiting for new emails: ")