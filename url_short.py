import pyshorteners

url = input("Enter your url below:")
type_tiny = pyshorteners.Shortener()
s_url = type_tiny.tinyurl.short(url)
print("The new URL is: " + s_url)
