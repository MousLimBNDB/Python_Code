import re

def hashtages (string):
    hashs = re.findall(r"#\w+",string)
    if not hashs:
        print("thers is no hashtages")
        return 0
    else:
        print(f"your hashtage/s are : {hashs}")
        return hashs
    
hashtages("mqdhmlms#qmlsk#mqlskd")