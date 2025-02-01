def count_letters(text):
  """Рахує кількість букв у тексті."""
  count = 0
  for char in text:
    if char.isalpha():
      count += 1
  return count

def count_h(text):
    """Рахує кількість букв h у тексті."""
    count = 0
    for char in text:
        if char=="d" or char=="D":
            count += 1
    return count

text = "Zkhq d pdvvlyh vwdu froodsvhv xqghu lwv rzq judylwb, lw irupv d eodfn kroh wkdw lv vr khdyb wkdw lw fdswxuhv hyhubwklqj wkdw sdvvhv lwv hyhqw krulcrq. Qrw hyhq oljkw fdq hvfdsh. Dw wkh hyhqw krulcrq, wlph uhsodfhv vsdfh dqg srlqwv rqob iruzdug. Wkh iorz ri wlph fduulhv hyhubwklqj wrzdugv d vlqjxodulwb ixuwkhvw lqvlgh wkh eodfn kroh, zkhuh ghqvlwb lv lqilqlwh dqg wlph hqgv. Urjhu Shqurvh – dzdughg wkh Qreho Sulch lq Skbvlfv – lqyhqwhg lqjhqlrxv pdwkhpdwlfdo phwkrgv wr hasoruh Doehuw Hlqvwhlq’v jhqhudo wkhrub ri uhodwlylwb. Kh vkrzhg wkdw wkh wkhrub ohdgv wr wkh irupdwlrq ri eodfn krohv, wkrvh prqvwhuv lq wlph dqg vsdfh wkdw fdswxuh hyhubwklqj wkdw hqwhuv wkhp."
num_letters = count_letters(text)
num_h = count_h(text)

print(f"Кількість букв у тексті: {num_letters}")
print(f"Кількість букв у тексті: {num_h}")