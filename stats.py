
def word_count(file):
    wc = file.split()
    wc1 = len(wc)
    return f"Found {wc1} total words"


def character_count(file):
    h = {}
    file = file.lower()
    for i in file:
        if h == {} or i not in h.keys():
            h[i] = 1
        elif i in h.keys():
            h[i] += 1
    return h

def sort_on(diction):
    return diction["num"]

def sort_dict(diction): 
    l = []
    for i in diction:
        l.append({"char":i,"num":diction[i]})
    l.sort(reverse=True, key = sort_on)
    return l
