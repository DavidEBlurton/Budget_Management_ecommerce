# Given a word w 
# and some text t, find whether w is in t. 
# For example: 
#w="nest", t="I built a nest and tested it."
#output: "here"
#example 2:
#w="runs", t="The dog"
#output: "not here"
#Example 3: 
#w="April", t="april showers bring may flowers"
#output: "not here"


# eval the word (w) and see if its in text (t)
def solution():
    input = w, t

    if w in t:
        return 'here'
    elif w not in t:
        return 'not here'
        
