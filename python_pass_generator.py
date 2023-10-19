import random
import subprocess
numb = ['1','2','3','4','5','6','7','8','9','0']
letter = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split(' ')
symbols = "! # $ % & \ ' ( ) * + , - . / : ; < = >? @ [ \ \ ] ^ _ ` { |  } ~".split(' ')

rndom = [numb,letter,symbols]

len_of_pass = 20

password = ''

while len(password) < len_of_pass:
    intrand = random.randint(0,2)
    selected_ar = rndom[intrand]
    password += selected_ar[random.randint(0,len(selected_ar)-1)]


subprocess.run(['clip'], universal_newlines=True, input=password)
