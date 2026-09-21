# Jannat Translator - Al Maarifa Ait Melloul
# Software Engineering Project for GKS Scholarship
# Author: Jannat - 18/20 French

dictionary = [
    {"fr":"bonjour","en":"hello","ar":"سلام","ko":"안녕하세요"},
    {"fr":"merci","en":"thank you","ar":"شكرا","ko":"감사합니다"},
    {"fr":"maison","en":"house","ar":"دار","ko":"집"},
    {"fr":"ecole","en":"school","ar":"مدرسة","ko":"학교"},
    {"fr":"livre","en":"book","ar":"كتاب","ko":"책"},
    {"fr":"famille","en":"family","ar":"عائلة","ko":"가족"},
    {"fr":"amour","en":"love","ar":"حب","ko":"사랑"},
    {"fr":"eau","en":"water","ar":"ماء","ko":"물"},
    {"fr":"ordinateur","en":"computer","ar":"حاسوب","ko":"컴퓨터"},
    {"fr":"reussite","en":"success","ar":"نجاح","ko":"성공"},
    # زيدي هنا 90 كلمة حقيقية خرين اللي عندك
]

def translate(word, src='fr', tgt='ar'):
    word = word.lower().strip()
    for entry in dictionary:
        if entry.get(src) == word:
            return entry.get(tgt, "Not found")
    return None

def main():
    print("=== Jannat Translator | 1000 Words Project ===")
    print("FR - EN - AR - KO | Made for Korean Scholarship")
    print(f"Total words: {len(dictionary)}")

    while True:
        print("\n1: FR->AR 2: FR->EN 3: FR->KO 4: Search 5: Exit")
        c = input("Choice: ")
        if c == '5':
            print("شكرا! من أيت ملول إلى كوريا!")
            break
        if c == '4':
            q = input("Search FR: ").lower()
            found = [e for e in dictionary if q in e['fr']]
            for e in found:
                print(f"{e['fr']} | {e['en']} | {e['ar']} | {e['ko']}")
            continue

        map_choice = {'1':('fr','ar'),'2':('fr','en'),'3':('fr','ko')}
        if c in map_choice:
            src,tgt = map_choice[c]
            w = input(f"Word in {src}: ")
            res = translate(w, src, tgt)
            print(f"=> {res}" if res else "Not found")

if __name__ == "__main__":
    main()s