import random

def battle(e_hp, m_name, p):
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
                    battle(e_hp, m_name, p)
            else:
                e_hp -= x
                print(f"Landed A Hit Of {x} On The {m_name}")
                if e_hp <= 0:
                    print(f"{m_name} Defeated")
                    break
                else:
                    battle(e_hp, m_name, p)
    
    if option == "item":
        items = ["Stone", "Dagger", "Parchment"]
        print(items)
        item_c = input(">  ")
        if item_c in actions[0:1] and item_c in items[0:3]:
            item = item_c.replace("Use ", "")
            print(f"You used the {item} and threw it.\nIt did nothing...")
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
                quit()
        

p = 0
actions = ["Use "]
monster_num = {47: "Shoca", 78: "Hantas", 29: "Tolas"}
e_hp, m_name = random.choice(list(monster_num.items()))
print(f"A wild {m_name} appears")
battle(e_hp, m_name, p)





    



