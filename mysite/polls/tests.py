from django.test import TestCase

# Create your tests here.

count = 0
while True:
    if count == 10:
        print("Yup")
        break
    for x in range(10):
        print(x)
        if x > 7:
            count = 10
            break
    print("Hello")
    
