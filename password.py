# this program allows user to genrate password
import random
chars= ('a b c d e f g h i j k l m n o p q r s t u v w x y z  B C D E F G H I J K L M N O P Q R S T U V W X Y Z 1 2 3 4 5 6 7 8 9 0')
password=(input('enter password'))
password= '  '
for c in range (10):
  password += random.choice(chars)
print(password)




