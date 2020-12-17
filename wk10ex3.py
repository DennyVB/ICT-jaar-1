# wk10ex3.py
#
# Naam:
#


# functie #1
#
def create_dictionary(filename):
    #bestand lezen
    f = open(filename)
    text = f.read()
    f.close()

    
    words = text.split()
    

    d = {}
    pw = '$'

    for nw in words:
        if pw not in d:
            d[pw] = [nw]
        else:
            d[pw] += [nw]  

        
        pw = nw  
        if pw[-1] == '.' or pw[-1] == '?' or pw[-1] == '!':
            pw = '$'

    
    return d
   

    # controleer hierna of de nieuwe pw eindigt op een
    # leesteken -- als dat _wel_ zo is zet dan pw op '$'


# functie #2
#
def generate_text(d, n):
    import random
    filename = input('filename')
    d = create_dictionary(filename)  
    start = '$'

    for nw in range(n):
        



#
# Je gegenereerde essay van ongeveer 500 woorden (plak in de onderstaande triple-quoted strings):
#
"""



"""
#
#
