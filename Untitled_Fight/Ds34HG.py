import random

items = ["Stone", "Dagger", "Parchment"]
desc_pos = {"Stone":[0,1], "Dagger": [2,3,4], "Parchment": [5,6,7]}
crit_num = (11, 25, 39, 76, 84, 56)
p = 0
monster_num = {47: "Shoca", 78: "Hantas", 29: "Tolas"}
e_hp, m_name = random.choice(list(monster_num.items()))

def battle(e_hp, m_name, p):
    option = input("Attack || Item || Run\n> ").lower()
    if option == "attack":
        for i in range(1):
            x = random.randint(1, 100)
            if x in crit_num:
                e_hp -= x
                print(f"Crit Hit Of {x} On The {m_name}")
                print(e_hp)
                if e_hp <= 0:
                    print(f"{m_name} Defeated")
                    re_try()
                else:
                    battle(e_hp, m_name, p)
            else:
                e_hp -= x
                print(f"Landed A Hit Of {x} On The {m_name}")
                if e_hp <= 0:
                    print(f"{m_name} Defeated")
                    re_try()
                else:
                    battle(e_hp, m_name, p)
    
            break
    
    if option == "item":
        print(items)
        item_c = input("> ")
        item_d = item_c.split()
        num1_wrd = item_d[0]
        num2_wrd = item_d[1]
        if num1_wrd == "Use" or num1_wrd == "use" and num2_wrd in items:
                for key, value in desc_pos.items():
                    if num2_wrd in key:
                        file = open(r"Untitled_Fight\Ds34HG_text.txt")
                        for pos, l_num in enumerate(file):
                            if pos in value:
                                print(l_num.strip())
                battle(e_hp, m_name, p)
    
    if option == "run":
        esc_num = (79, 60, 98, 76, 7, 5)
        for i in range(1):
            x = random.randint(1, 100)
            if x in esc_num:
                print("You escaped with your life\nHow impressive")
                quit()
            if x not in esc_num and p < 2:
                p = p + 1
                print(f"You are trapped by the {m_name}'s claws")
                battle(e_hp, m_name, p)
            else:
                print(f"You died by the {m_name} while trying to flee")
                print("Game Over")
                re_try()
    else:
        battle(e_hp, m_name, p)

def start_menu():
    print("-"*39)
    print("     Welcome to the Untitled Fight\n")
    print("     Please type one to continue\n            Play || Quit\n")
    print("-"*39)
    while True:
        menu = input("> ").lower()
        if menu == "play":
            print(f"A wild {m_name} appears")
            battle(e_hp, m_name, p)
        if menu == "quit":
            quit()

def re_try():
    rt = input("Re-play? - y/n: ").lower()
    if rt == "y":
        start_menu()
    if rt == "n":
        quit()
    else:
        re_try()

start_menu()






    



