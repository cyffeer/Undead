import os

class Undead:
    
    def __init__(self, name = None, hp = None):
        if name != None and hp != None:
            self.__hp = hp
            self.__name = "Undead" + name
        else:
            self.__hp = 100
            self.__name = "Undead"
            self.__isDead = False
    


    
    # dead is a boolean
    def isDead(self, dead = None):
        if dead == None:
            return self.__isDead
        else:
            self.__isDead = dead
        



    def getName(self):
        return self.__name
    
    def getType(self):
        return "Undead"
          
    def getHP(self):
        return self.__hp
        
    def setName(self, name):
        self.__name = name
    
    def setHP(self, hp = None, multiplier = None):
        if multiplier == None:
            self.__hp = hp
        else:
            self.__hp = self.__hp * multiplier
            

class Zombie(Undead):
    def __init__(self):
        super().__init__()
        self.abilities = ["attack","eat"]
    
    def execute_ability(self,ability, target = None):
        if ability == "attack":
            if self.getHP() < 50:
                print("Due to its ineffective HP, the zombie is no longer able to attack.")
                return 0
            
            else:
                if target.getType() == "Ghost":
                    attack_damage = int(self.getHP() / 2) # attack damage is half of its HP
                    realattack = attack_damage * 0.1
                    health = target.getHP() - realattack
                    healthcheck = target.setHP(health) 
                    return f"{self.getName()} attacks {target.getName()} for {realattack} damage!"
                else:
                    attack_damage = int(self.getHP() / 2) # attack damage is half of its HP
                    attack = target.getHP() - attack_damage
                    healthcheck = target.setHP(attack) 
                    return f"{self.getName()} attacks {target.getName()} for {attack_damage} damage HP!"
                    

        elif ability == "eat":
                

            if target.getType() == "Ghost":
                    gain = self.getHP() + (target.getHP() /2)
                    healthgain = self.setHP(gain)
                    return f"{self.getName()} casts {target.getName()} and gains {gain} HP!"
                    
            else:
                    gain = self.getHP() + (target.getHP() /2)
                    healthgain = self.setHP(gain)
                    return f"{self.getName()} casts {target.getName()} and gains {gain} HP!"
        else:
            return f"{self.getName} didn't do anything!"
        
            
    def getType(self):
        return "Zombie"

            
class Vampire(Undead):
    
    def __init__(self):
        super().__init__()
        super().setHP(multiplier = 1.2) 
        self.abilities = ["attack", "bite"]
        
    
    def execute_ability(self, ability, target=None):
        if ability == "attack":
            if self.getHP() <= 0:
                return f"Due to its ineffective HP, the Vampire is no longer able to attack."
            else:
                if target.getType() == "Ghost":
                    attack_damage = int(self.getHP())
                    realattack = attack_damage * 0.1   
                    attack = target.getHP() - realattack
                    healthcheck = target.setHP(attack) 
                    return f"{self.getName()} attacks {target.getName()} for {realattack} damage that set for {healthcheck} HP!"
                else: 
                    attack_damage = int(self.getHP())   
                    attack = target.getHP() - attack_damage
                    healthcheck = target.setHP(attack) 
                    return f"{self.getName()} attacks {target.getName()} for {attack_damage} damage that set for {healthcheck} HP!"
                

                
        elif ability == "bite":
            if self.getHP() <= 0:
                return f"Due to its ineffective HP, the Vampire is no longer able to bite."
            else:
                gain = self.getHP() + (target.getHP() * 0.8)
                healthgain = self.setHP(gain)
                return f"{self.getName()} bits {target.getName()} and gains {gain} HP!"

                

        else:
            return f"{self.name} didn't do anything!"

    def getType(self):
        return "Vampire"
        
class Skeleton(Undead):
    
    def __init__(self):
        super().__init__()
        super().setHP(multiplier = 0.8) 
        self.abilities = ["attack", "shoot"]
        
    def execute_ability(self, ability, target=None):
        if ability == "attack":
            if self.getHP() <= 0:
                return f"Due to its ineffective HP, the Skeleton is no longer able to attack."
            else:
                if target.getType() == "Ghost":
                    attack_damage = int(self.getHP() * 0.7)   
                    realattack = attack_damage * 0.1
                    attack = target.getHP() - realattack
                    healthcheck = target.setHP(attack) 
                    return f"{self.getName()} attacks {target.getName()} for {realattack} damage!"
                else:
                    attack_damage = int(self.getHP() * 0.7)   
                    attack = target.getHP() - attack_damage
                    healthcheck = target.setHP(attack) 
                    return f"{self.getName()} attacks {target.getName()} for {attack_damage} damage!"

                
        elif ability == "shoot":
            if self.getHP() <= 0:
                return f"Due to its ineffective HP, the Skeleton is no longer able to shoot an arrow."
            else:
                if target.getType() == "Ghost":
                    attack_damage = int(self.getHP() * 0.7)   
                    realattack = attack_damage * 0.1
                    attack = target.getHP() - realattack
                    healthcheck = target.setHP(attack) 
                    return f"{self.getName()} shoots an arrow at {target.getName()} for {realattack} damage!"
                else:
                    attack_damage = int(self.getHP() * 0.7)   
                    attack = target.getHP() - attack_damage
                    healthcheck = target.setHP(attack) 
                    return f"{self.getName()} shoots an arrow at {target.getName()} for {attack_damage} damage!"
                
                
        else:
            return f"{self.name} didn't do anything!"
        

        
    def getType(self):
        return "Skeleton"
        
class Ghost(Undead):
    
    def __init__(self):
        super().__init__()
        super().setHP(multiplier = 0.5) 
        self.abilities = ["attack", "haunt"]
        
    def execute_ability(self, ability, target=None):
        if ability == "attack":
            if self.getHP() <= 0:
                return f"Due to its ineffective HP, the Vampire is no longer able to attack."
            else:
                if target.getType() == "Ghost":
                    attack_damage = int(self.getHP() * 0.2)   
                    realattack = attack_damage * 0.1
                    attack = target.getHP() - realattack
                    healthcheck = target.setHP(attack) 
                    return f"{self.getName()} attacks {target.getName()} for {realattack} damage!"
                else:
                    attack_damage = int(self.getHP() * 0.2)   
                    attack = target.getHP() - attack_damage
                    healthcheck = target.setHP(attack) 
                    return f"{self.getName()} attacks {target.getName()} for {attack_damage} damage!"
                
                
        elif ability == "haunt":
            if self.getHP() <= 0:
                return f"Due to its ineffective HP, the Vampire is no longer able to bite."
            else:
                gain = self.getHP() + (target.getHP() * 0.1)
                healthgain = self.setHP(gain)
                return f"{self.getName()} haunts {target.getName()} and gains {gain} HP!"

        else:
            return f"{self.name} didn't do anything!"
    
        
    def getType(self):
        return "Ghost"


class Lich(Undead):
    
    def __init__(self):
        super().__init__()
        super().setHP(multiplier = 0.8) 
        self.abilities = ["attack","cast"]
        
    
    def execute_ability(self, ability, target=None):
        if ability == "attack":
            if self.getHP() <= 0:
                return f"Due to its ineffective HP, the Lich is no longer able to attack."
            else:
                if target.getType() == "Ghost":
                    attack_damage = self.getHP() * 0.7 # attack damage is half of its HP
                    realattack = attack_damage * 0.1
                    health = target.getHP() - realattack
                    healthcheck = target.setHP(health) 
                    return f"{self.getName()} attacks {target.getName()} for {realattack} damage!"
                else:
                    attack_damage = self.getHP() * 0.7 # attack damage is half of its HP
                    attack = target.getHP() - attack_damage
                    healthcheck = target.setHP(attack) 
                    return f"{self.getName()} attacks {target.getName()} for {attack_damage} damage HP!"

                
        elif ability == "cast":
            if self.getHP() <= 0:
                return f"Due to its ineffective HP, the Lich is no longer able to cast a spell."
            else:
                if target.getType() == "Ghost":
                    gain = self.getHP() + (target.getHP() * 0.1)
                    healthgain = self.setHP(gain)
                    return f"{self.getName()} casts {target.getName()} and gains {gain} HP!"
                    
                else:
                    gain = self.getHP() + (target.getHP() * 0.1)
                    healthgain = self.setHP(gain)
                    return f"{self.getName()} casts {target.getName()} and gains {gain} HP!"
            

        else:
            return f"{self.name} didn't do anything!"
        
    def getType(self):
        return "Lich"


class Mummy(Undead):
    
    def __init__(self):
        super().__init__()
        self.abilities = ["attack", "revive"]
        
        
    def execute_ability(self, ability, target=None):
        if ability == "attack":
            if self.getHP() <= 0:
                return f"Due to its ineffective HP, the Vampire is no longer able to attack."
            else:
                if self.getType() == target.getType():
                    return f"The Mummy cannot attack is own kind."
                else:
                    if target.getType() == "Ghost":
                        attack_damage = int(self.getHP()/2) 
                        attack = (target.getHP() * 0.1) + attack_damage
                        realattack = attack * 0.1
                        health = target.getHP() - realattack
                        healthcheck = target.setHP(health) 
                        return f"{self.getName()} attacks {target.getName()} for {realattack} damage!"
                    else:
                        attack_damage = int(self.getHP()/2) 
                        attack = (target.getHP() * 0.1) + attack_damage
                        health = target.getHP() - attack
                        healthcheck = target.setHP(health) 
                        return f"{self.getName()} attacks {target.getName()} for {attack} damage!"
                        
                
        elif ability == "revive":
            if self.getHP() <= 0:
                self.setHP(100)
                self.isDead(False)
                return f"{self.getName()} possessed {target.getName()} and revived itself!"
                        
    def getType(self):
        return "Mummy"
        
undead_list = []


while True:
    print("-----------------------------")
    print("====== UNDEAD BATTLE ROYALE ======")
    print("1. Create Undead")
    print("2. Command Undead")
    print("3. Display Undead")
    print("4. Quit")
    
    choice = input("Enter choice: ")
    os.system('cls')
    
    if choice == "1":
        print("====== CREATE UNDEAD ======")
        print("1. Zombie")
        print("2. Vampire")
        print("3. Skeleton")
        print("4. Ghost")
        print("5. Lich")
        print("6. Mummy")
        undead_choice = input("Enter your choice: ")

        if undead_choice == "1":
            name = input("Enter Zombie name: ")
            zombie = Zombie()
            zombie.setName(name)
            undead_list.append(zombie)
            print(f"Zombie {name} created.")
    
        elif undead_choice == "2":
            name = input("Enter Vampire name: ")
            vampire = Vampire()
            vampire.setName(name)
            undead_list.append(vampire)
            print(f"Vampire {name} created.")
    
        elif undead_choice == "3":
            name = input("Enter Skeleton name: ")
            skeleton = Skeleton()
            skeleton.setName(name)
            undead_list.append(skeleton)
            print(f"Skeleton {name} created.")
        
        elif undead_choice == "4":
            name = input("Enter Ghost name: ")
            ghost = Ghost()
            ghost.setName(name)
            undead_list.append(ghost)
            print(f"Ghost {name} created.")
        
        elif undead_choice == "5":
            name = input("Enter Lich name: ")
            lich = Lich()
            lich.setName(name)
            undead_list.append(lich)
            print(f"Lich {name} created.")
    
        elif undead_choice == "6":
            name = input("Enter Mummy name: ")
            mummy = Mummy()
            mummy.setName(name)
            undead_list.append(mummy)
            print(f"Mummy {name} created.")
        else:
            print("Invalid choice.")
        
    elif choice == "2":
        if not undead_list:
            print("There are no undead to command.")
            continue
                

        print("List of Undead:")
        for i, undead in enumerate(undead_list):
            print(f"{i+1}.{undead.getName()} ({undead.__class__.__name__}) - HP: {int(undead.getHP())} - Dead?: {undead.isDead()}")
        attacker = int(input("Enter the number of the undead to command: ")) - 1
        undead = undead_list[attacker]
                
        # Get the ability and target undead
        print(f"Available abilities for {undead.getName()}:")
        print(*undead.abilities, sep="\n")
        ability = input("Enter the ability: ")
        target = None
        print("List of Undead that can be targeted:")
        for i, target_undead in enumerate(undead_list):           
            if target_undead != undead:
                print(f"{i+1}. {target_undead.getName()} ({target_undead.__class__.__name__}) - HP: {target_undead.getHP()}")
        receiver = int(input("Enter the number of the undead to target: ")) - 1
        target = undead_list[receiver]
        result = undead.execute_ability(ability, target)
        print (result)
                    
        if target.getHP() <= 0:
            if target.getType() == "Lich":
                target.isDead(False)
                print(f"{target.getName()} ({target.getType()}) has 0 HP but still alive")
            elif target.getType() == "Vampire":
                target.isDead(False)
                print(f"{target.getName()} ({target.getType()}) has 0 HP but still alive")
            else:
                target.isDead(True)
                print(f"{target.getName()} is dead!")

                   
                    
    elif choice == "3":
        # display all created undead
        print("\nCreated undead:")
        for undead in undead_list:
            print(f"{undead.getName()} ({undead.__class__.__name__}) - HP: {undead.getHP()} - Dead?: {undead.isDead()}")
     
    elif choice == "4":
        print("Exiting program...")
        print("Created by: Cyfer Nikolai Supleo & Theodore Karlyle Igot")
        break
    
    else:
        print("Invalid choice.")