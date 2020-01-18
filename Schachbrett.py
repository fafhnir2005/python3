import matplotlib.pyplot as plt
summe = 0
feldliste = []

for feld in range(64):
    reiskorn = 2**feld 
    feldliste.append(reiskorn)
    summe += reiskorn
    print(f"Feld {feld+1}. = {reiskorn:>30,} Reiskörner und damit gesamt {summe:>30,} Reiskörner")
gewicht = summe * 0.02 / 1000 / 1000

print()
print(f"Bei einem Gewicht von 0,02g je Korn wiegt das Brett {gewicht:,.0f} Tonnen")

plt.plot(feldliste)
plt.show()