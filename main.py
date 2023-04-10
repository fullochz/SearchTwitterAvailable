from faker import Faker
import sys
from termcolor import colored
import requests
from googletrans import Translator
translator = Translator()


def menu():
 print ('============================')
 print ('Username Checker by fullochz')
 print ('============================')
 print ('[1]. Manual')
 print ('[2]. Otomatis (EN)')
 print ('[3]. Otomatis (ID)')
 print ('[4]. 0xword')
 print ('[5]. Number')
 print ('[6]. Exit')
 x = int(input('Silahkan pilih\t\t: '))

 if x == 1 :
   def manual():
     username = input('Cek username\t\t: ')
     response = requests.get(f'https://api.twitter.com/i/users/username_available.json?username={username}').json()

     if response['valid']:
         with open('available.txt','a')as f:
              f.write('{0}\n'.format(username))
         print (colored(f'Tersedia\t\t: {username}','green'))

     else :
         print (colored(f'Sudah Terpakai\t\t: {username}','red'))

     print ('\nApakah ingin mencoba lagi?')
     print ('[1]. Ya ')
     print ('[2]. Tidak ')
     print ('[3]. Kembali ke Menu\n')
     lagi = int(input('Pilihan\t\t\t: '))

     if lagi == 1 :
        manual()

     elif lagi == 2 :
        print ('Terimakasih!')
        sys.exit()
        
     elif lagi == 3 :
         menu()
        
     else :
        print (colored('Waduh! pilihan salah, coba lagi bos..\n','red'))
        sys.exit()

   manual()


 elif x == 2 :
  try :
     fake = Faker()
     i = 1

     while True:
         username = fake.word()
         response = requests.get(f'https://api.twitter.com/i/users/username_available.json?username={username}').json()

         if response['valid']:
             with open('available.txt','a')as f:
              f.write('{0}\n'.format(username))
             print(colored(f'{i}. Tersedia\t\t: {username}', 'green'))
             i += 1

         else:
             print(colored(f'{i}. Sudah Terpakai\t: {username}', 'red'))
             i += 1
  except KeyboardInterrupt:
    print("\nProgram dihentikan.")


 elif x == 3 :
   try :
      fake = Faker()
      i = 1

      while True:

          teks = fake.word()
          terjemahan = translator.translate(teks, src='en', dest='id')
          username = terjemahan.text

          response = requests.get(f'https://api.twitter.com/i/users/username_available.json?username={username}').json()

          if response['valid']:
              with open('available.txt','a')as f:
               f.write('{0}\n'.format(username))
              print(colored(f'{i}. Tersedia\t\t: {username}', 'green'))
              i += 1

          else:
              print(colored(f'{i}. Sudah Terpakai\t: {username}', 'red'))
              i += 1
   except KeyboardInterrupt:
     print("\nProgram dihentikan.")

 elif x == 4 :
   try :
     fake = Faker()
     i = 1

     while True:
         username = "0x" + fake.word()
         response = requests.get(f'https://api.twitter.com/i/users/username_available.json?username={username}').json()

         if response['valid']:
             with open('available.txt','a')as f:
              f.write('{0}\n'.format(username))
             print(colored(f'{i}. Tersedia\t\t: {username}', 'green'))
             i += 1
         else:
             print(colored(f'{i}. Sudah Terpakai\t: {username}', 'red'))
             i += 1
   except KeyboardInterrupt:
    print("\nProgram dihentikan.")
    
    
 elif x == 5 :
   try :
     i = 1
     print('Biarkan jika kosong')
     y = input('masukan awalan\t\t: ')
     print('Biarkan jika kosong')
     b = input('masukan akhiran\t\t: ')
     
     while True:
         username = y + str(i) + b
         response = requests.get(f'https://api.twitter.com/i/users/username_available.json?username={username}').json()

         if response['valid']:
             with open('available.txt','a')as f:
              f.write('{0}\n'.format(username))
             print(colored(f'{i}. Tersedia\t\t: {username}', 'green'))
             i += 1
         else:
             print(colored(f'{i}. Sudah Terpakai\t: {username}', 'red'))
             i += 1
   except KeyboardInterrupt:
    print("\nProgram dihentikan.")
    

 elif x == 6 :
     print ('Terimakasih!')
     sys.exit()


 else :
     print (colored('Waduh! pilihan salah, coba lagi bos..\n','red'))
     menu()



menu()
