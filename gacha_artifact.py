import numpy as np

class GachaArtifact:
    def __init__(self):
        #inisialisasi method
        self.artifactSimulation()

    # untuk memilih domain artefak mana yang akan dipilih, setelah dipilih akan merujuk ke fungsi gacha setiap domain
    def artifactSimulation(self):
        print(f'Artifact Domain List:\n 1. Domain of Guyun\n 2. Midsummer Courtyard\n 3. Peak of Vindagnyr\n 4. Hidden Palace of Zhou Formula\n 5. Valley of Remembrance\n 6. Ridge Watch\n 7. Clear Pool and Mountain Cavern')

        domain_choice = int(input('Pick one Domain (type number): '))
        if domain_choice == 1:
            self.guyunPull()
        elif domain_choice == 2:
            self.midsummerPull()
        elif domain_choice == 3:
            self.vindagnyrPull()
        elif domain_choice == 4:
            self.zhouPull()
        elif domain_choice == 5:
            self.valleyPull()
        elif domain_choice == 6:
            self.ridgePull()
        elif domain_choice == 7:
            self.clearPull()

    def guyunPull(self):
        #menyimpan nama-nama artefak yang ada di domain of guyun
        #memiliki dua set artefak dengan dua jenis rarity *4 dan *5
        guyun = np.array(['(*5) Flower of Creviced Cliff', '(*5) Feather of Jagged Peaks', '(*5) Sundial of Enduring Jade',
        '(*5) Goblet of Chiseled Crag', '(*5) Mask of Solitude Basalt',
        '(*5) Summer Night Bloom', '(*5) Summer Night Finale', '(*5) Summer Night Moment', 
        '(*5) Summer Night Waterballoon', '(*5) Summer Night Mask',
        '(*4) Flower of Creviced Cliff', '(*4) Feather of Jagged Peaks', '(*4) Sundial of Enduring Jade',
        '(*4) Goblet of Chiseled Crag', '(*4) Mask of Solitude Basalt',
        '(*4) Summer Night Bloom', '(*4) Summer Night Finale', '(*4) Summer Night Moment', 
        '(*4) Summer Night Waterballoon', '(*4) Summer Night Mask'])

        #menyimpan probabilitas setiap artefak
        prob = np.array([0.025, 0.025, 0.025,
        0.025, 0.025,
        0.025, 0.025, 0.025,
        0.025, 0.025,
        0.075, 0.075, 0.075,
        0.075, 0.075,
        0.075, 0.075, 0.075,
        0.075, 0.075])

        #roll sebanyak 5 kali
        roll = 5

        #gacha menggunakan np.random.choice berdasarkan array, roll, dan probabilitasnya
        #kemudian tanya apakah ingin gacha lagi
        gacha = np.random.choice(guyun, roll, p=prob)
        print(f'Domain of Guyun\n------------------------------------------------------')
        print(gacha)
        self.gachaAgainArti()

    def midsummerPull(self):
        #menyimpan nama-nama artefak yang ada di midsummer courtyard
        #memiliki dua set artefak dengan dua jenis rarity *4 dan *5
        midsummer = np.array(['(*5) Thunderbird Mercy', '(*5) Survivor of Catastrophe', '(*5) Hourglass of Thunder',
        '(*5) Omen of Thunderstorm', '(*5) Thunder Summoner Crown',
        '(*5) Thundersoother Heart', '(*5) Thundersoother Plume', '(*5) Hour of Soothing Thunder',
        '(*5) Thundersoother Goblet', '(*5) Thundersoother Diadem',
        '(*4) Thunderbird Mercy', '(*4) Survivor of Catastrophe', '(*4) Hourglass of Thunder',
        '(*4) Omen of Thunderstorm', '(*4) Thunder Summoner Crown',
        '(*4) Thundersoother Heart', '(*4) Thundersoother Plume', '(*4) Hour of Soothing Thunder',
        '(*4) Thundersoother Goblet', '(*4) Thundersoother Diadem'])
        
        #menyimpan probabilitas setiap artefak
        prob = np.array([0.025, 0.025, 0.025,
        0.025, 0.025,
        0.025, 0.025, 0.025,
        0.025, 0.025,
        0.075, 0.075, 0.075,
        0.075, 0.075,
        0.075, 0.075, 0.075,
        0.075, 0.075])

        #roll sebanyak 5 kali
        roll = 5
        #gacha menggunakan np.random.choice berdasarkan array, roll, dan probabilitasnya
        #kemudian tanya apakah ingin gacha lagi
        gacha = np.random.choice(midsummer, roll, p=prob)
        print(f'Midsummer Courtyard\n-----------------------------------------------------')
        print(gacha)
        self.gachaAgainArti()

    def vindagnyrPull(self):
        #menyimpan nama-nama artefak yang ada di midsummer peak of vindagnyr
        #memiliki dua set artefak dengan dua jenis rarity *4 dan *5
        vindagnyr = np.array(["(*5) Gilded Corsage", "(*5) Gust of Nostalgia", "(*5) Copper Compass", 
        "(*5) Goblet of Thundering Deep", "(*5) Wine-Stained Tricorne",
        "(*5) Snowswept Memory", "(*5) Icebreaker's Resolve", "(*5) Frozen Homeland's Demise", 
        "(*5) rost-Weaved Dignity", "(*5) Broken Rime's Echo",
        "(*4) Gilded Corsage", "(*4) Gust of Nostalgia", "(*4) Copper Compass", 
        "(*4) Goblet of Thundering Deep", "(*4) Wine-Stained Tricorne",
        "(*4) Snowswept Memory", "(*4) Icebreaker's Resolve", "(*4) Frozen Homeland's Demise", 
        "(*4) Frost-Weaved Dignity", "(*4) Broken Rime's Echo"])

        #menyimpan probabilitas setiap artefak
        prob = np.array([0.025, 0.025, 0.025,
        0.025, 0.025,
        0.025, 0.025, 0.025,
        0.025, 0.025,
        0.075, 0.075, 0.075,
        0.075, 0.075,
        0.075, 0.075, 0.075,
        0.075, 0.075])

        roll = 5
        #gacha menggunakan np.random.choice berdasarkan array, roll, dan probabilitasnya
        #kemudian tanya apakah ingin gacha lagi
        gacha = np.random.choice(vindagnyr, roll, p=prob)
        print(f'Peak of Vindagnyr\n-----------------------------------------------------')
        print(gacha)
        self.gachaAgainArti()

    def zhouPull(self):
        #menyimpan nama-nama artefak yang ada di hidden palace of zhou formula
        #memiliki dua set artefak dengan dua jenis rarity *4 dan *5
        zhou = np.array(["(*5) Witch's Flower of Blaze", "(*5) Witch's Ever-Burning Plume", "(*5) Witch's End Time", 
        "(*5) Witch's Heart Flames", "(*5) Witch's Scorching Hat",
        "(*5) Lavawalker's Resolution", "(*5) Lavawalker's Salvation", "(*5) Lavawalker's Torment", 
        "(*5) Lavawalker's Epiphany", "(*5) Lavawalker's Wisdom", 
        "(*4) Witch's Flower of Blaze", "(*4) Witch's Ever-Burning Plume", "(*4) Witch's End Time", 
        "(*4) Witch's Heart Flames", "(*4) Witch's Scorching Hat", 
        "(*4) Lavawalker's Resolution", "(*4) Lavawalker's Salvation", "(*4) Lavawalker's Torment", 
        "(*4) Lavawalker's Epiphany", "(*4) Lavawalker's Wisdom"])
        
        #menyimpan probabilitas setiap artefak
        prob = np.array([0.025, 0.025, 0.025,
        0.025, 0.025,
        0.025, 0.025, 0.025,
        0.025, 0.025,
        0.075, 0.075, 0.075,
        0.075, 0.075,
        0.075, 0.075, 0.075,
        0.075, 0.075])

        roll = 5
        #gacha menggunakan np.random.choice berdasarkan array, roll, dan probabilitasnya
        #kemudian tanya apakah ingin gacha lagi
        gacha = np.random.choice(zhou, roll, p=prob)
        print(f'Hidden Palace of Zhou Formula\n-----------------------------------------------------')
        print(gacha)
        self.gachaAgainArti()

    def valleyPull(self):
        #menyimpan nama-nama artefak yang ada di valley of remembrance
        #memiliki dua set artefak dengan dua jenis rarity *4 dan *5
        valley = np.array(["(*5) In Remembrance of Viridescent Fields", "(*5) Viridescent Arrow Feather", "(*5) Viridescent Venerer's Determination",
        "(*5) Viridescent Venerer's Vessel", "(*5) Viridescent Venerer's Diadem",
        "(*5) Maiden's Distant Love", "(*5) Maiden's Heart-stricken Infatuation", "(*5) Maiden's Passing Youth",
        "(*5) Maiden's Fleeting Leisure", "(*5) Maiden's Fading Beauty",
        "(*4) In Remembrance of Viridescent Fields", "(*4) Viridescent Arrow Feather", "(*4) Viridescent Venerer's Determination",
        "(*4) Viridescent Venerer's Vessel", "(*4) Viridescent Venerer's Diadem",
        "(*4) Maiden's Distant Love", "(*4) Maiden's Heart-stricken Infatuation", "(*4) Maiden's Passing Youth",
        "(*4) Maiden's Fleeting Leisure", "(*4) Maiden's Fading Beauty"])

        #menyimpan probabilitas setiap artefak
        prob = np.array([0.025, 0.025, 0.025,
        0.025, 0.025,
        0.025, 0.025, 0.025,
        0.025, 0.025,
        0.075, 0.075, 0.075,
        0.075, 0.075,
        0.075, 0.075, 0.075,
        0.075, 0.075])

        roll = 5
        #gacha menggunakan np.random.choice berdasarkan array, roll, dan probabilitasnya
        #kemudian tanya apakah ingin gacha lagi
        gacha = np.random.choice(valley, roll, p=prob)
        print(f'Valley of Remembrance\n-----------------------------------------------------')
        print(gacha)
        self.gachaAgainArti()

    def ridgePull(self):
        #menyimpan nama-nama artefak yang ada di ridge watch
        #memiliki dua set artefak dengan dua jenis rarity *4 dan *5
        ridge = np.array(["(*5) Flower of Accolades", "(*5) Ceremonial War-Plume", "(*5) Orichalceous Time-Dial",
        "(*5) Noble's Pledging Vessel", "(*5) General's Ancient Helm",
        "(*5) Stainless Bloom", "(*5) Wise Doctor's Pinion", "(*5) Moment of Cessation",
        "(*5) Surpassing Cup", "(*5) Mocking Mask",
        "(*4) Flower of Accolades", "(*4) Ceremonial War-Plume", "(*4) Orichalceous Time-Dial",
        "(*4) Noble's Pledging Vessel", "(*4) General's Ancient Helm",
        "(*4) Stainless Bloom", "(*4) Wise Doctor's Pinion", "(*4) Moment of Cessation",
        "(*4) Surpassing Cup", "(*4) Mocking Mask"])

        #menyimpan probabilitas setiap artefak
        prob = np.array([0.025, 0.025, 0.025,
        0.025, 0.025,
        0.025, 0.025, 0.025,
        0.025, 0.025,
        0.075, 0.075, 0.075,
        0.075, 0.075,
        0.075, 0.075, 0.075,
        0.075, 0.075])

        roll = 5
        #gacha menggunakan np.random.choice berdasarkan array, roll, dan probabilitasnya
        #kemudian tanya apakah ingin gacha lagi
        gacha = np.random.choice(ridge, roll, p=prob)
        print(f'Ridge Watch\n-----------------------------------------------------')
        print(gacha)
        self.gachaAgainArti()

    def clearPull(self):
        #menyimpan nama-nama artefak yang ada di clear pool and mountain cavern
        #memiliki dua set artefak dengan dua jenis rarity *4 dan *5
        clear = np.array(["(*5) Bloodstained Flower of Iron", "(*5) Bloodstained Black Plume", "(*5) Bloodstained Final Hour",
        "(*5) Bloodstained Chevalier's Goblet", "(*5) Bloodstained Iron Mask",
        "(*5) Royal Flora", "(*5) Royal Plume", "(*5) Royal Pocket Watch",
        "(*5) Royal Silver Urn", "(*5) Royal Masque",
        "(*4) Bloodstained Flower of Iron", "(*4) Bloodstained Black Plume", "(*4) Bloodstained Final Hour",
        "(*4) Bloodstained Chevalier's Goblet", "(*4) Bloodstained Iron Mask",
        "(*4) Royal Flora", "(*4) Royal Plume", "(*4) Royal Pocket Watch",
        "(*4) Royal Silver Urn", "(*4) Royal Masque"])

        #menyimpan probabilitas setiap artefak
        prob = np.array([0.025, 0.025, 0.025,
        0.025, 0.025,
        0.025, 0.025, 0.025,
        0.025, 0.025,
        0.075, 0.075, 0.075,
        0.075, 0.075,
        0.075, 0.075, 0.075,
        0.075, 0.075])

        roll = 5
        #gacha menggunakan np.random.choice berdasarkan array, roll, dan probabilitasnya
        #kemudian tanya apakah ingin gacha lagi
        gacha = np.random.choice(clear, roll, p=prob)
        print(f'Clear Pool and Mountain Cavern\n-----------------------------------------------------')
        print(gacha)
        self.gachaAgainArti()
    
    def gachaAgainArti(self):
        print("Roll again?")
        yn = input('yes or no: ')

        for y in yn:
            if yn =='yes':
                self.artifactSimulation()
                break
            else:
                print("Gacha ended thankyou for playing.")
                break