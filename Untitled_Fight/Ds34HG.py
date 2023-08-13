import random

def battle(e_hp, m_name):
    option = input("Attack || Item || Run\n> ").lower()
    if option == "attack":
        crit_num = (11, 25, 39, 76, 84, 56)
        for i in range(1):
            x = random.randint(1, 100)
            if x in crit_num:
                e_hp -= x
                print(f"Crit Hit Of {x} On The {m_name}")
                if e_hp <= 0:
                    print(f"{m_name} Defeated")
                    break
                else:
                    battle(e_hp, m_name)
            else:
                e_hp -= x
                print(f"Landed A Hit Of {x} On The {m_name}")
                if e_hp <= 0:
                    print(f"{m_name} Defeated")
                    break
                else:
                    battle(e_hp, m_name)
    if option == "item":
        items = ["Stone", "Dagger", "Slip of parchment"]
        print(items)
        item = input("> Use ").lower()
        if item in items[0:3]:
            print(f"You used a {item} and threw it.\nIt did nothing...")
            battle(e_hp, m_name)
    if option == "run":
        p = 0
        esc_num = (79, 60, 98, 76, 7, 5)
        while p < 3:
            for i in range(1):
                x = random.randint(1, 100)
                if x in esc_num:
                    print("You escaped with your life\nHow impressive")
                    quit()
                elif x not in esc_num:
                    p += 1
                    print("smth")
                    battle(e_hp, m_name)
                elif p == 3:
                        break
                else:
                    battle(e_hp, m_name)
        




monster_num = {47: "Shoca", 78: "Hantas", 29: "Tolas"}
e_hp, m_name = random.choice(list(monster_num.items()))
print(f"A wild {m_name} appears")
battle(e_hp, m_name)





    



