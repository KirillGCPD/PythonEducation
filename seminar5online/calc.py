
def div(stri:str):
    if (stri.count("+")>0):
        n=stri.find("+")
        left=stri[:n]
        right=stri[n+1:]
        print(f"{left}+{right}")
        return div(left)+div(right)
    elif (stri.count("*")>0):
        n=stri.find("*")
        left=stri[:n]
        right=stri[n+1:]
        return div(left)*div(right)
    elif (stri.count("/")>0):
        n=stri.find("/")
        left=stri[:n]
        right=stri[n+1:]
        return div(left)/div(right)
    return int(stri)

stri = "1+4*6/2"

print(div(stri))