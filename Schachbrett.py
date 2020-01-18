summe = 0

for feld in range(64):
    reiskorn = 2**feld 
    summe = summe + reiskorn
    print("Feld {}. = {:,} Reiskörner und damit gesamt {:,} Reiskörner" \
        .format(feld+1,reiskorn,summe))
