from collections import Counter
import re

alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
shift = 3
ciphered_text = "Zkhq d pdvvlyh vwdu froodsvhv xqghu lwv rzq judylwb, lw irupv d eodfn kroh wkdw lv vr khdyb wkdw lw fdswxuhv hyhubwklqj wkdw sdvvhv lwv hyhqw krulcrq. Qrw hyhq oljkw fdq hvfdsh. Dw wkh hyhqw krulcrq, wlph uhsodfhv vsdfh dqg srlqwv rqob iruzdug. Wkh iorz ri wlph fduulhv hyhubwklqj wrzdugv d vlqjxodulwb ixuwkhvw lqvlgh wkh eodfn kroh, zkhuh ghqvlwb lv lqilqlwh dqg wlph hqgv."
letter_count = Counter(''.join(char.upper() for char in ciphered_text if char.isalpha())).most_common()
print("regex",len(re.findall(r'[a-zA-Z]', ciphered_text)))
total = len([x for x in ciphered_text if x.isalpha()])
print("total",total)
for i in range(len(letter_count)):
    if letter_count[i][0] in alphabet_upper:
        print(letter_count[i][0], letter_count[i][1], f"{round(letter_count[i][1] / total * 100, 2)}%")