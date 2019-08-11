"dosent work with invalid chars"

def _convert1(dna,config={"G":"C","C":"G","T":"A","A":"U"}):
    return "".join([config[x]  if x in config else x for x in list(dna) ])

def _convert(dna,config={"G":"C","C":"G","T":"A","A":"U"}):
    "sort them first then solve"
    mod = list(sorted(set(dna)))
    for x i mod:
        if x not in config:
                return "Invalid Input"
    return "".join([config[x] for x in list(dna) ])        
    

#print(_convert(input()))
print(_convert("AGG"))

