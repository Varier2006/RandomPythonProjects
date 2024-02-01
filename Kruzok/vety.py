veta = "Mucha sedela na stene. STOP Spadla.STOP"
nove = ""
skip = 0
for i in range(len(veta)):
    if skip == 0:
        if veta[i] == "S":
            if veta[i + 1] == "T":
                if veta[i + 2] == "O":
                    if veta[i + 3] == "P":
                        nove = nove + "\n"
                        skip = 5
    if skip == 0:
        nove = nove + veta[i]
    else:
        skip = skip - 1
print(nove)
