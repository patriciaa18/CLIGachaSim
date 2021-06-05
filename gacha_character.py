import time
import numpy as np

class GachaCharacter:
    #inisialisasi, memanggil fungsi gachaSimulation
    def __init__(self):
        self.gachaSimulation()

    def gachaSimulation(self):
        gacha_item = np.array(['(*5) Eula', '(*5) Jean', '(*5) Diluc','(*5) Qiqi', '(*5) Keqing', '(*5) Mona',
        '(*4) Beidou', '(*4) Xingqiu', '(*4) Xinyan',
        '(*4) Kaeya', '(*4) Amber', '(*4) Lisa','(*4) Xiangling', '(*4) Barbara', '(*4) Ningguang',
        '(*4) Noelle', '(*4) Diona', '(*4) Fischl', '(*4) Yanfei', '(*4) Rosaria', 
        '(*4) Bennett', '(*4) Razor', '(*4) Chongyun', '(*4) Sucrose',
        '(*3) Harbinger of Dawn', '(*3) Black Tassel', '(*3) Debate Club', '(*3) Emerald Orb', 
        '(*3) Sharpshooter Oath', '(*3) Halberd', '(*3) White Tassel', '(*3) Raven Bow', 
        '(*3) Cool Steel', '(*3) Ferrous Shadow', '(*3) Slingshot', '(*3) Bloodstained Greatsword', 
        '(*3) Magic Guide', '(*3) Thrilling Tales of Dragon Slayers', '(*3) Dark Iron Sword', '(*3) Fillet Blade'])
        
        #sesuai urutan, masukkan probabilitas masing-masing elemen dalam desimal, jumlah semua probabilitas harus = 1
        prob = np.array([0.00166666666, 0.00166666666, 0.00166666666, 0.00166666666, 0.00166666666, 0.00166666666,
        0.01666666667, 0.01666666667, 0.01666666667,
        0.00266666666, 0.00266666666, 0.00266666666, 0.00266666666, 0.00266666666, 0.00266666666,
        0.00266666666, 0.00266666666, 0.00266666666, 0.00266666666, 0.00266666666,
        0.00266666666, 0.00266666666, 0.00266666666, 0.00266666666,
        0.05625, 0.05625, 0.05625, 0.05625,
        0.05625, 0.05625, 0.05625, 0.05625,
        0.05625, 0.05625, 0.05625, 0.05625,
        0.05625, 0.05625, 0.05625, 0.05625])

        #mengambil seberapa banyak roll yang diinginkan pemain
        roll = int(input("How much do roll you want?"))

        #mengambil waktu sebelum gacha dilakukan
        initialTime = time.time()

        #untuk mengundi (gacha) dari gacha item sebanyak roll dan peluang sesuai prob
        gacha = np.random.choice(gacha_item, roll, p=prob)

        #perulangan untuk print hasil gacha 
        # for i, gacha_result in enumerate(gacha):
        #     self.print_gacha_result(i, gacha_result)
        print(gacha)
        print("-----------------------------------------------------------------")
        #print waktu sekarang dikurangi waktu sebelumnya untuk mendapatkan lama program dijalankan
        print("Time taken: ", time.time() - initialTime, " seconds")
        #tanya apakah ingin gacha lagi
        self.gachaAgain()

    #fungsi untuk mencetak hasil gacha dengan warna dan ditambahi angka
    #warna kuning untuk *5
    #warna ungu untuk *4
    #warna biru(cyan) untuk *3
    # def print_gacha_result(i, gacha_result, self):
    #     gacha_result = gacha_result
    #     if '(*5)' in gacha_result:
    #         return print( str(i+1) + '.', '\033[33m' + gacha_result + '\x1b[0m')
    #     elif '(*4)' in gacha_result:
    #         return print(str(i+1) + '.', '\033[35m' + gacha_result + '\x1b[0m')
    #     else:
    #         return print(str(i+1) + '.', '\033[36m' + gacha_result + '\x1b[0m')

    # menanyakan apakah ingin gacha kembali
    # jika jawaban yes maka ulangi gacha jika no permainan berhenti
    def gachaAgain(self):
        print("Roll again?")
        yn = input('yes or no: ')

        for y in yn:
            if yn == 'yes':
                self.gachaSimulation()
                break
            else:
                print("Gacha ended thank you for playing.")
                break
