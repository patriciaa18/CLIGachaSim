import time
import numpy as np

class GachaCharacter:
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
        
        prob = np.array([0.001, 0.001, 0.001, 0.001, 0.001, 0.001,
        0.0103333333333333, 0.0103333333333333, 0.0103333333333333,
        0.0013333333333333, 0.0013333333333333, 0.0013333333333333, 0.0013333333333333, 0.0013333333333333, 0.0013333333333333,
        0.0013333333333333, 0.0013333333333333, 0.0013333333333333, 0.0013333333333333, 0.0013333333333333,
        0.0013333333333333, 0.0013333333333333, 0.0013333333333333, 0.0013333333333333,
        0.0589375, 0.0589375, 0.0589375, 0.0589375,
        0.0589375, 0.0589375, 0.0589375, 0.0589375,
        0.0589375, 0.0589375, 0.0589375, 0.0589375,
        0.0589375, 0.0589375, 0.0589375, 0.0589375])
        
        roll = int(input("How much roll do you want?"))

        initialTime = time.time()

        gacha = np.random.choice(gacha_item, roll, p=prob)

        gacha_item, counts = np.unique(gacha, return_counts=True)
        for item, count in zip(gacha_item, counts):
            print(item, count)

        print("-----------------------------------------------------------------")

        print("Time taken: ", time.time() - initialTime, " seconds")

        self.gachaAgain()

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
