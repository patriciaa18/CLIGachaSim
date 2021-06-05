#import class
from gacha_character import GachaCharacter
from gacha_artifact import GachaArtifact

def main():
    #buat menu untuk memilih ingin gacha character atau artifact
    print("Genshin Impact Gacha Simulation")
    print("----------------------------------------------------")
    print(f"Menu: \n 1. Character Gacha\n 2. Artifact Gacha")
    user_choice = int(input("Pick your menu: "))

    if user_choice == 1:
        GachaCharacter()
    elif user_choice == 2:
        GachaArtifact()

if __name__ == "__main__":
    main()
    
