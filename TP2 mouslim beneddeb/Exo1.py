import re
def alphabets_only(phrase):

    alphabet = re.findall(r"\W",phrase)
    return not alphabet
# i used the r here ------^ to get rid of this warning
#c:\A.Mous_Lim\code mslm\A.PYTHON CODE\TP2 mouslim beneddeb\Exo1.py:3: SyntaxWarning: invalid escape sequence '\W'
# alphabet = re.findall("\W",phrase)
"""
    if len(alphabet) == 0 :
        print("the phrase contains only alphabets")
        return True
    else:
        print("there is a special characters in the phrase")
        return False
"""


print(alphabets_only("mouslimbeneddeb"))