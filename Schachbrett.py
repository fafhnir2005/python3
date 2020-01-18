summe = 0

for feld in range(64):
    reiskorn = 2**feld 
    summe = summe + reiskorn
    print("Feld {}. = {:>30,} Reiskörner und damit gesamt {:>30,} Reiskörner" \
        .format(feld+1,reiskorn,summe))
gewicht = summe * 0.02 / 1000 / 1000

print()
print("Bei einem Gewicht von 0,02g je Korn wiegt das Brett {:,.0f} Tonnen".format(gewicht))
