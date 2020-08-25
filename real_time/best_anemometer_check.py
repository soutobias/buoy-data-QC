def tempos(boias):

    lines = open('anemometros.txt', 'rb')

    boia2,epocaini,epocafim,anemo=[],[],[],[]
    for line in lines:
        dataline = line.strip()
        columns = dataline.split()
        if columns[0].decode('ascii')==boias:
            epocaini.append(columns[1].decode('ascii'))
            epocafim.append(columns[2].decode('ascii'))
            anemo.append(columns[3].decode('ascii'))

    anemomet=[epocaini,epocafim,anemo]

    return anemomet


anemomet=tempos(boias)
