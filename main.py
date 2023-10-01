
import tkinter as tk
from tkinter import messagebox
#output color #B99B6B

class GUI():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("800x500")
        self.root.configure(bg='#D8C49F')
        self.root.title("Character Creator! by DICHOSA")

        #Title Label
        self.title = tk.Label(self.root, text="CHARACTER CREATOR", font=('Arial', 14), bg='#F1DBBF', 
        borderwidth=2, relief="solid", width=30)
        self.title.pack(padx=10, pady=15)

        #Char Class Label
        self.class_label = tk.Label(self.root, text="Class", font=('Arial', 14), bg='#F1DBBF', 
        borderwidth=2, relief="solid", width=15)
        self.class_label.place(x=40, y=80)

        #Char Class Choices/input
        self.classVar = tk.IntVar()
        self.C1 = tk.Radiobutton(self.root, text="Wizard", variable=self.classVar, value=1, 
        font=('Arial', 12), bg='#D8C49F', command=self.wizardAbility)
        self.C1.place(x=60, y=120)
        self.C2 = tk.Radiobutton(self.root, text="Knight", variable=self.classVar, value=2, 
        font=('Arial', 12), bg='#D8C49F', command=self.knightAbility)
        self.C2.place(x=250, y=120)
        self.C3 = tk.Radiobutton(self.root, text="Archer", variable=self.classVar, value=3, 
        font=('Arial', 12), bg='#D8C49F', command=self.archerAbility)
        self.C3.place(x=440, y=120)
        self.C4 = tk.Radiobutton(self.root, text="Assassin", variable=self.classVar, value=4, 
        font=('Arial', 12), bg='#D8C49F', command=self.assasinAbility)
        self.C4.place(x=630, y=120)

        #Char Weapon Label
        self.weapon_label = tk.Label(self.root, text="Weapon", font=('Arial', 14), bg='#F1DBBF', 
        borderwidth=2, relief="solid", width=15)
        self.weapon_label.place(x=40, y=190)

        #Char Weapon Choices/input
        self.weaponVar = tk.IntVar()
        self.W1 = tk.Radiobutton(self.root, text="Wizard Staff", variable=self.weaponVar, value=1, 
        font=('Arial', 12), bg='#D8C49F')
        self.W1.place(x=60, y=230)
        self.W2 = tk.Radiobutton(self.root, text="Sword", variable=self.weaponVar, value=2, 
        font=('Arial', 12), bg='#D8C49F')
        self.W2.place(x=250, y=230)
        self.W3 = tk.Radiobutton(self.root, text="Bow & Arrow", variable=self.weaponVar, value=3, 
        font=('Arial', 12), bg='#D8C49F')
        self.W3.place(x=440, y=230)
        self.W4 = tk.Radiobutton(self.root, text="Katar", variable=self.weaponVar, value=4, 
        font=('Arial', 12), bg='#D8C49F')
        self.W4.place(x=630, y=230)

        #Char Abilities Label
        self.ability_label = tk.Label(self.root, text="Abilities", font=('Arial', 14), bg='#F1DBBF', 
        borderwidth=2, relief="solid", width=15)
        self.ability_label.place(x=40, y=300)

        #Char Ability Choices/input
        self.abilityVar1 = tk.StringVar()
        self.abilityVar2 = tk.StringVar()
        self.abilityVar3 = tk.StringVar()
        self.abilityVar4 = tk.StringVar()

        self.C1 = tk.Checkbutton(self.root, text = "Ability1", variable = self.abilityVar1, onvalue = "null", 
        offvalue = "", font=('Arial', 12), bg='#D8C49F')
        self.C1.place(x=60, y=340)
        self.C2 = tk.Checkbutton(self.root, text = "Ability2", variable = self.abilityVar2, onvalue = "null", 
        offvalue = "", font=('Arial', 12), bg='#D8C49F')
        self.C2.place(x=250, y=340)
        self.C3 = tk.Checkbutton(self.root, text = "Ability3", variable = self.abilityVar3, onvalue = "null", 
        offvalue = "", font=('Arial', 12), bg='#D8C49F')
        self.C3.place(x=440, y=340)
        self.C4 = tk.Checkbutton(self.root, text = "Ability4", variable = self.abilityVar4, onvalue = "null", 
        offvalue = "", font=('Arial', 12), bg='#D8C49F')
        self.C4.place(x=630, y=340)

        #Submit Button
        self.button1 = tk.Button(self.root, text="Submit", font=('Arial', 14), width=20, 
        bg='#9F8C76', command=self.charOutput)
        self.button1.pack(side='bottom', pady=40)

        self.root.mainloop()

    def charOutput(self):
        #Character Class
        classVar = self.classVar.get()
        if classVar == 1:
            charClass = "Wizard"
        elif classVar == 2:
            charClass = "Knight"
        elif classVar == 3:
            charClass = "Archer"
        elif classVar == 4:
            charClass = "Assasin"

        #Character Weapon
        weaponVar = self.weaponVar.get()
        if weaponVar == 1:
            charWeapon = "Wizzard Staff"
        elif weaponVar == 2:
            charWeapon = "Sword"
        elif weaponVar == 3:
            charWeapon = "Bow & Arrow"
        elif weaponVar == 4:
            charWeapon = "Katar"

        #Character Ability
        charAbility1 = self.abilityVar1.get()
        charAbility2 = self.abilityVar2.get()
        charAbility3 = self.abilityVar3.get()
        charAbility4 = self.abilityVar4.get()

        if charAbility1 != "" and charAbility2 != "" and charAbility3 != "" and charAbility4 != "":
            messagebox.showinfo("Error!", "Please Only Select 3 Abilities")
        else:
            #Final Output
            messagebox.showinfo("Character", f"You Character is a {charClass} with a {charWeapon} for a weapon. Your Abilities are: {charAbility1}, {charAbility2}, {charAbility3}, {charAbility4}")
        
    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):
            self.root.destroy()
    
    def wizardAbility(self):
        self.C1['text'] = 'Energy Ball'
        self.C2['text'] = 'Dragons of Breath'
        self.C3['text'] = 'Crown of Flame'
        self.C4['text'] = 'Hail Storm'

        self.C1['onvalue'] = 'Energy Ball'
        self.C2['onvalue'] = 'Dragons of Breath'
        self.C3['onvalue'] = 'Crown of Flame'
        self.C4['onvalue'] = 'Hail Storm'
    
    def knightAbility(self):
        self.C1['text'] = 'Fire Slash'
        self.C2['text'] = 'Power Slash'
        self.C3['text'] = 'Gigantic Storm'
        self.C4['text'] = 'Chaotic Disaster'

        self.C1['onvalue'] = 'Fire Slash'
        self.C2['onvalue'] = 'Power Slash'
        self.C3['onvalue'] = 'Gigantic Storm'
        self.C4['onvalue'] = 'Chaotic Disaster'

    def archerAbility(self):
        self.C1['text'] = 'Take Aim'
        self.C2['text'] = 'Quick Shot'
        self.C3['text'] = 'Blazing Arrow'
        self.C4['text'] = 'Frost Arrow'

        self.C1['onvalue'] = 'Take Aim'
        self.C2['onvalue'] = 'Quick Shot'
        self.C3['onvalue'] = 'Blazing Arrow'
        self.C4['onvalue'] = 'Frost Arrow'

    def assasinAbility(self):
        self.C1['text'] = 'Cloaking'
        self.C2['text'] = 'Enchant Poison'
        self.C3['text'] = 'Sonic Acceleration'
        self.C4['text'] = 'Meteor Assault'

        self.C1['onvalue'] = 'Cloaking'
        self.C2['onvalue'] = 'Enchant Poison'
        self.C3['onvalue'] = 'Sonic Acceleration'
        self.C4['onvalue'] = 'Meteor Assault'

GUI()