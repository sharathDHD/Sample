def _convert(dna,config={"G":"C","C":"G","T":"A","A":"U"}):
    return "".join([config[x]  if x in config else return "Invalid Input" for x in list(dna) ])
    

#print(_convert(input()))

