from random import choice, random

class node:
    def __init__ (self, data, next=None): 
        self.data = data
        self.next = next

class singleLL:
    def __init__(self):
        self.head = None 
    
    def add_end(self, data): 
        if self.head == None:
            self.head = node(data) 
            return 
        itr = self.head 
        
        while itr.next: 
            itr = itr.next
        itr.next = node(data) 

    def add_front(self, data):
        new_node = node(data)
        new_node.next = self.head
        self.head = new_node

    def print(self):
        if self.head == None:
            print("Linked list kosong")
        else:
            itr = self.head
            while itr is not None:
                print(itr.data, end=" ")
                itr = itr.next
    
    def getLength(self): 
        count = 0
        itr = self.head
        while itr is not None:
            itr = itr.next
            count += 1
        return count
    
    def edit(self,old,new):
        itr = self.head

        if itr == None:
            print("Linked list kosong")
        
        while itr != None:
            if itr.data == old:
                itr.data = new
                print("")
                return
            itr = itr.next
        print("Tidak Di temukan")

    def delete_at(self,index):
        if index > self.getLength():
            print("Index tidak ada")
            return
        if index == 0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            count += 1
            itr = itr.next


coba = singleLL()
arr = []
b = []

while True:
    print("Roussian Roulete")
    print("Welcome players to Roussian Roulette games, choose your fate now or never")
    print("1. Play")
    print("2. Skip ")

    menu = int(input("Choose your fate: "))

    if menu == 1:
        peluru = int(input("Masukkan berapa banyak peluru yang diinginkan : "))

        for i in range(peluru):
            angka = int(input("Input angka : "))
            if angka > 50:
                arr.insert(0,angka)
                coba.add_front(angka)
            elif angka <= 50:
                arr.append(angka)
                coba.add_end(angka)
        print(arr)

        a = len(arr)//2

        count2 = 0
        while(True):
            import random
            rndm = random.randint(0,len(arr)-1)
            cek1 = False
            for j in b:
                if j == arr[rndm]:
                    cek1 = True
                
            if cek1 == False:
                b.append(arr[rndm])
                count2 += 1

            if count2 == a:
                break
        print(b)


        print("Apakah ada angka yang ingin diganti?")
        jawaban = input("Masukkan yes atau no : ")
        
        while(True):
            if jawaban == "yes":
                isTrue = False
                angkalama = int(input("Masukkan angka lama yang ingin diganti : "))
                angkabaru = int(input("Masukkan angka pengganti : "))
                for j in range(len(b)):
                    if angkalama == b[j]:
                        isTrue = True
                        break

                if(isTrue):
                    coba.edit(angkalama,angkabaru)
                    b[j] = angkabaru
                    if angkabaru > 50:      
                        b.insert(0,angkabaru)
                        coba.add_front(angkabaru)
                        coba.delete_at(j+1)
                        b.pop(j+1)

                    coba.print()
                    print()
                
                else:
                    print("Angka Tidak di Temukan")

                print("Apakah masih ada angka yang ingin diganti lagi?")
                jawaban = input("Masukkan yes atau no : ")
                           
            elif jawaban == "no":
                for i in range(len(b)):
                    bilangan = choice(b)
                print("Memilih Secara Acak Peluru Zonk")
                print("Peluru Zonk yaitu : ", bilangan)

                count = 0
                while len(b) > 1:
                    cek  = False
                    PilihAngka = int(input("Masukkan Ingin Memilih Peluru Yang Mana : "))
                    for j in range(len(b)):
                        if PilihAngka == b[j]:
                            cek = True
                            break
                    if(cek):
                        if bilangan == b[j]:
                            print("Maaf Anda Kalah. Silahkan coba lagi.")
                            break

                        count += 1
                        coba.delete_at(j)
                        b.pop(j)
                        print(b)

                        if count == 2:
                            angkabaru2 = int(input("Input angka : "))
                            rndm1 = random.randint(0,len(b)-1)
                            b.insert(rndm1,angkabaru2)
                            print(b)
                    
                    else:
                        print("Angka Yang di Inputkan Tidak sesuai")

                if len(b) == 1:
                    print("Selamat Anda Menang. Silahkan Claim Hadiah Anda")           
                break
        break
    
    elif menu == 2:
        break