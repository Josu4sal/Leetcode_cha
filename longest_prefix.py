
def longest_pre(strs, shortest):
    pre=''
    for i in range(len(shortest)):
        letter=shortest[i]
        for word in strs:
            if word[i]!=letter:
                return pre 
        pre+=letter
    return pre

strs = ["flower", "flow", "flight"]
mini = 100
shortest = ""

for i in strs:
    if len(i) < mini:
        mini = len(i)
        shortest = i

print(longest_pre(strs, shortest))  