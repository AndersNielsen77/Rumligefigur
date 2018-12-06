#Importerer Tkinter.
import tkinter
from tkinter import *

#Giver matplotlib understøttelse for Tkinter.
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#impoterer numpy som "np"
import numpy as np

#importerer de nødvendige matplotlib moduler, "axes3d" er ikke.
#brugt til andet end at fortælle python at det er 3D grafer vi arbjeder i.
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as axes3d

fig = plt.figure()

#Vi giver programmet en class
class Program:
    def __init__(self, master):

        #laver et vindue
        frame = tkinter.Frame(master)
        
        #Laver 3 knapper der har hver sin funktion, de bruges til at sætte kvaliteten på 3D modellen
        self.button_1 = tkinter.Button(frame,text="Lav kvalitet",command=self.lavere)
        self.button_1.pack(side="left")
        self.button_2 = tkinter.Button(frame,text="Standard kvalitet", command=self.standard)
        self.button_2.pack(side="left")
        self.button_3 = tkinter.Button(frame,text="Høj kvalitet", command=self.højere)
        self.button_3.pack(side="left")

        #tekst box og knap til radius
        self.textbox=tkinter.Text(frame, height=1, width=10)
        self.textbox.pack()
        self.buttonsend=Button(frame, text="Enter radius", command=lambda: self.radius())
        self.buttonsend.pack()
        
        #Dette får matplotlib til at vise sig i Tkinter
        self.canvas = FigureCanvasTkAgg(fig,master=master)
        self.canvas.get_tk_widget().pack(side='top', fill='both', expand=1)

        #Bruges senere i programmet, det fortæller at for eksempel "u" er lig med værdier fra 0 til 12 med 12/60 (0.2) imellem hver værdi.
        self.u = np.linspace(0, 12, 60)
        self.v = np.linspace(0, 2*np.pi, 60)
        self.U, self.V = np.meshgrid(self.u, self.v)
        self.u1 = np.linspace(12, 26, 60)
        self.v1 = np.linspace(0, 2*np.pi, 60)
        self.U1, self.V1 = np.meshgrid(self.u1, self.v1)
        self.u2 = np.linspace(26, 32, 60)
        self.v2 = np.linspace(0, 2*np.pi, 60)
        self.U2, self.V2 = np.meshgrid(self.u2, self.v2)
        self.X = self.U
        self.X1 = self.U1
        self.X2 = self.U2

        #Bruger vi senere i koden
        self.integer=1

        #".pack()" får tingene til at vise sig i tkinter.
        frame.pack()

    def radius(self):
        self.inputvalue=self.textbox.get("1.0", "end-1c")
        self.integer=int(self.inputvalue)
        ax = fig.add_subplot(1, 1, 1, projection='3d')
        self.Y1 = (1.49*np.cos(0.34*self.U)+7.85)*np.cos(self.V)*self.integer
        self.Z1 = (1.49*np.cos(0.34*self.U)+7.85)*np.sin(self.V)*self.integer
        self.Y2 = (((-21599 / 302702400)*self.U1**6) + ((71843 / 8648640)*self.U1**5) - ((39878297 / 100900800)*self.U1**4) + ((118897967 / 12108096)*self.U1**3) - ((2903465249 / 21621600)*self.U1**2) + (268899149 / 280280)*self.U1 - (16145189 / 5775))*np.cos(self.V1)*self.integer
        self.Z2 = (((-21599 / 302702400)*self.U1**6) + ((71843 / 8648640)*self.U1**5) - ((39878297 / 100900800)*self.U1**4) + ((118897967 / 12108096)*self.U1**3) - ((2903465249 / 21621600)*self.U1**2) + (268899149 / 280280)*self.U1 - (16145189 / 5775))*np.sin(self.V1)*self.integer

        self.Y3 = (((0.23671)*self.U2**2) - (13.7463*self.U2) + 207.391)*np.cos(self.V2)*self.integer
        self.Z3 = (((0.23671)*self.U2**2) - (13.7463*self.U2) + 207.391)*np.sin(self.V2)*self.integer
        ax.plot_surface(self.X, self.Y1, self.Z1, alpha=1, color='red', rstride=10, cstride=10)
        ax.plot_surface(self.X1, self.Y2, self.Z2, alpha=1, color='blue', rstride=10, cstride=10)
        ax.plot_surface(self.X2, self.Y3, self.Z3, alpha=1, color='green', rstride=10, cstride=10)
        self.canvas.draw()

    def lavere(self):
        ax = fig.add_subplot(1, 1, 1, projection='3d')
        self.Y1 = (1.49*np.cos(0.34*self.U)+7.85)*np.cos(self.V)*self.integer
        self.Z1 = (1.49*np.cos(0.34*self.U)+7.85)*np.sin(self.V)*self.integer
        self.Y2 = (((-21599 / 302702400)*self.U1**6) + ((71843 / 8648640)*self.U1**5) - ((39878297 / 100900800)*self.U1**4) + ((118897967 / 12108096)*self.U1**3) - ((2903465249 / 21621600)*self.U1**2) + (268899149 / 280280)*self.U1 - (16145189 / 5775))*np.cos(self.V1)*self.integer
        self.Z2 = (((-21599 / 302702400)*self.U1**6) + ((71843 / 8648640)*self.U1**5) - ((39878297 / 100900800)*self.U1**4) + ((118897967 / 12108096)*self.U1**3) - ((2903465249 / 21621600)*self.U1**2) + (268899149 / 280280)*self.U1 - (16145189 / 5775))*np.sin(self.V1)*self.integer

        self.Y3 = (((0.23671)*self.U2**2) - (13.7463*self.U2) + 207.391)*np.cos(self.V2)*self.integer
        self.Z3 = (((0.23671)*self.U2**2) - (13.7463*self.U2) + 207.391)*np.sin(self.V2)*self.integer
        ax.plot_surface(self.X, self.Y1, self.Z1, alpha=1, color='red', rstride=15, cstride=15)
        ax.plot_surface(self.X1, self.Y2, self.Z2, alpha=1, color='blue', rstride=15, cstride=15)
        ax.plot_surface(self.X2, self.Y3, self.Z3, alpha=1, color='green', rstride=15, cstride=15)
        self.canvas.draw()

    def standard(self):
        ax = fig.add_subplot(1, 1, 1, projection='3d')
        self.Y1 = (1.49*np.cos(0.34*self.U)+7.85)*np.cos(self.V)*self.integer
        self.Z1 = (1.49*np.cos(0.34*self.U)+7.85)*np.sin(self.V)*self.integer
        self.Y2 = (((-21599 / 302702400)*self.U1**6) + ((71843 / 8648640)*self.U1**5) - ((39878297 / 100900800)*self.U1**4) + ((118897967 / 12108096)*self.U1**3) - ((2903465249 / 21621600)*self.U1**2) + (268899149 / 280280)*self.U1 - (16145189 / 5775))*np.cos(self.V1)*self.integer
        self.Z2 = (((-21599 / 302702400)*self.U1**6) + ((71843 / 8648640)*self.U1**5) - ((39878297 / 100900800)*self.U1**4) + ((118897967 / 12108096)*self.U1**3) - ((2903465249 / 21621600)*self.U1**2) + (268899149 / 280280)*self.U1 - (16145189 / 5775))*np.sin(self.V1)*self.integer

        self.Y3 = (((0.23671)*self.U2**2) - (13.7463*self.U2) + 207.391)*np.cos(self.V2)*self.integer
        self.Z3 = (((0.23671)*self.U2**2) - (13.7463*self.U2) + 207.391)*np.sin(self.V2)*self.integer
        ax.plot_surface(self.X, self.Y1, self.Z1, alpha=1, color='red', rstride=10, cstride=10)
        ax.plot_surface(self.X1, self.Y2, self.Z2, alpha=1, color='blue', rstride=10, cstride=10)
        ax.plot_surface(self.X2, self.Y3, self.Z3, alpha=1, color='green', rstride=10, cstride=10)
        self.canvas.draw()

    def højere(self):
        ax = fig.add_subplot(1, 1, 1, projection='3d')
        self.Y1 = (1.49*np.cos(0.34*self.U)+7.85)*np.cos(self.V)*self.integer
        self.Z1 = (1.49*np.cos(0.34*self.U)+7.85)*np.sin(self.V)*self.integer
        self.Y2 = (((-21599 / 302702400)*self.U1**6) + ((71843 / 8648640)*self.U1**5) - ((39878297 / 100900800)*self.U1**4) + ((118897967 / 12108096)*self.U1**3) - ((2903465249 / 21621600)*self.U1**2) + (268899149 / 280280)*self.U1 - (16145189 / 5775))*np.cos(self.V1)*self.integer
        self.Z2 = (((-21599 / 302702400)*self.U1**6) + ((71843 / 8648640)*self.U1**5) - ((39878297 / 100900800)*self.U1**4) + ((118897967 / 12108096)*self.U1**3) - ((2903465249 / 21621600)*self.U1**2) + (268899149 / 280280)*self.U1 - (16145189 / 5775))*np.sin(self.V1)*self.integer

        self.Y3 = (((0.23671)*self.U2**2) - (13.7463*self.U2) + 207.391)*np.cos(self.V2)*self.integer
        self.Z3 = (((0.23671)*self.U2**2) - (13.7463*self.U2) + 207.391)*np.sin(self.V2)*self.integer
        ax.plot_surface(self.X, self.Y1, self.Z1, alpha=1, color='red', rstride=5, cstride=5)
        ax.plot_surface(self.X1, self.Y2, self.Z2, alpha=1, color='blue', rstride=5, cstride=5)
        ax.plot_surface(self.X2, self.Y3, self.Z3, alpha=1, color='green', rstride=5, cstride=5)
        self.canvas.draw()

root = tkinter.Tk()
app = Program(root)
root.mainloop()

