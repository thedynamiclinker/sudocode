#!/usr/bin/env python3

from pathlib import Path

FILES = {

# =======================
# psychology / MBTI
# =======================

"psychology/MBTI.md": """
Def: [[Person]], [[Type]], [[System]]
Def: [[Way]], [[To]], [[Group]], [[People]]
""",

"psychology/INTJ.md": """
Def: [[Person]], [[Who]], [[Think]], [[Long]], [[Time]]
Def: [[Person]], [[Who]], [[Build]], [[System]]
Def: [[Person]], [[Who]], [[Not]], [[Care]], [[If]], [[People]], [[Are]], [[Angry]]
""",

"psychology/ENTJ.md": """
Def: [[Person]], [[Who]], [[Want]], [[Power]]
Def: [[Person]], [[Who]], [[Make]], [[Other]], [[People]], [[Do]], [[Thing]]
Def: [[Person]], [[Who]], [[Start]], [[Organization]]
""",

"psychology/INFJ.md": """
Def: [[Person]], [[With]], [[Strong]], [[Inner]], [[Voice]]
Def: [[Person]], [[Who]], [[Feel]], [[Responsible]], [[For]], [[World]]
Def: [[Person]], [[Who]], [[Lead]], [[Without]], [[Want]], [[To]]
""",

"psychology/INTP.md": """
Def: [[Person]], [[Who]], [[Break]], [[Idea]]
Def: [[Person]], [[Who]], [[Ask]], [[Why]], [[Forever]]
Def: [[Person]], [[Who]], [[Cause]], [[Problem]], [[Then]], [[Leave]]
""",

"psychology/ISTJ.md": """
Def: [[Person]], [[Who]], [[Follow]], [[Rule]]
Def: [[Person]], [[Who]], [[Keep]], [[System]], [[Same]]
Def: [[Person]], [[Who]], [[Do]], [[Work]], [[Again]]
""",

"psychology/ISFJ.md": """
Def: [[Person]], [[Who]], [[Remember]], [[Old]], [[Way]]
Def: [[Person]], [[Who]], [[Keep]], [[Group]], [[Together]]
Def: [[Person]], [[Who]], [[Do]], [[Work]], [[Quiet]]
""",

"psychology/ESTJ.md": """
Def: [[Person]], [[Who]], [[Enforce]], [[Rule]]
Def: [[Person]], [[Who]], [[Tell]], [[People]], [[What]], [[To]], [[Do]]
Def: [[Person]], [[Who]], [[Like]], [[Order]]
""",

"psychology/ESFJ.md": """
Def: [[Person]], [[Who]], [[Care]], [[About]], [[People]]
Def: [[Person]], [[Who]], [[Organize]], [[Group]]
Def: [[Person]], [[Who]], [[Want]], [[Everyone]], [[Happy]]
""",

"psychology/INFP.md": """
Def: [[Person]], [[Who]], [[Care]], [[About]], [[Meaning]]
Def: [[Person]], [[Who]], [[Feel]], [[Deep]]
Def: [[Person]], [[Who]], [[Want]], [[World]], [[Good]]
""",

"psychology/ENFP.md": """
Def: [[Person]], [[With]], [[Many]], [[Idea]]
Def: [[Person]], [[Who]], [[Start]], [[Many]], [[Thing]]
Def: [[Person]], [[Who]], [[Talk]], [[About]], [[Meaning]]
""",

"psychology/ISFP.md": """
Def: [[Person]], [[Who]], [[Feel]], [[Inside]]
Def: [[Person]], [[Who]], [[Live]], [[By]], [[Feel]]
Def: [[Person]], [[Who]], [[Not]], [[Explain]], [[Much]]
""",

"psychology/ESFP.md": """
Def: [[Person]], [[Who]], [[Live]], [[Now]]
Def: [[Person]], [[Who]], [[Feel]], [[First]]
Def: [[Person]], [[Who]], [[Make]], [[Moment]], [[Big]]
""",

"psychology/ENTP.md": """
Def: [[Person]], [[Who]], [[Combine]], [[Idea]]
Def: [[Person]], [[Who]], [[Argue]], [[For]], [[Fun]]
Def: [[Person]], [[Who]], [[Invent]], [[Problem]]
""",

"psychology/ISTP.md": """
Def: [[Person]], [[Who]], [[Fix]], [[Thing]]
Def: [[Person]], [[Who]], [[Touch]], [[System]]
Def: [[Person]], [[Who]], [[Leave]], [[After]]
""",

"psychology/ESTP.md": """
Def: [[Person]], [[Who]], [[Take]], [[Risk]]
Def: [[Person]], [[Who]], [[Try]], [[Thing]]
Def: [[Person]], [[Who]], [[Act]], [[Fast]]
""",

"psychology/ENFJ.md": """
Def: [[Person]], [[Who]], [[Care]], [[About]], [[Group]]
Def: [[Person]], [[Who]], [[Lead]], [[People]]
Def: [[Person]], [[Who]], [[Want]], [[Good]], [[For]], [[All]]
""",

# =======================
# religion core
# =======================

"religion/Sect.md": """
Def: [[Group]], [[Of]], [[People]], [[With]], [[Shared]], [[Belief]]
Def: [[Group]], [[That]], [[Split]], [[From]], [[Bigger]], [[Group]]
""",

"religion/Sect-Founder.md": """
Def: [[Person]], [[Who]], [[Start]], [[Sect]]
Def: [[Person]], [[Who]], [[Not]], [[Normal]]
Def: [[Person]], [[Who]], [[Override]], [[Social]], [[Equilibrium]]
""",

"religion/Believer.md": """
Def: [[Person]], [[Who]], [[Join]], [[Sect]]
Def: [[Person]], [[Who]], [[Stay]]
Def: [[Person]], [[Who]], [[Follow]], [[Rule]]
""",

# =======================
# Christianity
# =======================

"religion/sects/Pentecostalism.md": """
Def: [[Christian]], [[Sect]]
Def: [[Group]], [[That]], [[Care]], [[About]], [[Spirit]]
Def: [[Group]], [[That]], [[Do]], [[Not]], [[Care]], [[About]], [[Order]]
""",

"religion/founders/William J. Seymour.md": """
Def: [[William]], [[J.]], [[Seymour]]
Def: [[Person]], [[With]], [[Moral]], [[Authority]]
Def: [[Person]], [[Who]], [[Let]], [[Chaos]], [[Happen]]
""",

"religion/believers/Pentecostal.md": """
Def: [[Person]], [[Who]], [[Feel]], [[God]], [[Now]]
Def: [[Person]], [[Who]], [[Do]], [[Not]], [[Read]], [[Long]], [[Book]]
""",

"religion/sects/Lutheranism.md": """
Def: [[Christian]], [[Sect]]
Def: [[Group]], [[That]], [[Split]], [[From]], [[Catholic]], [[Church]]
""",

"religion/founders/Martin Luther.md": """
Def: [[Martin]], [[Luther]]
Def: [[Person]], [[Who]], [[Read]], [[Book]], [[Hard]]
Def: [[Person]], [[Who]], [[Say]], [[No]], [[To]], [[Empire]]
""",

"religion/believers/Lutheran.md": """
Def: [[Person]], [[Who]], [[Like]], [[Order]]
Def: [[Person]], [[Who]], [[Trust]], [[Text]]
""",

"religion/sects/Methodism.md": """
Def: [[Christian]], [[Sect]]
Def: [[Group]], [[That]], [[Scale]]
""",

"religion/founders/John Wesley.md": """
Def: [[John]], [[Wesley]]
Def: [[Person]], [[Who]], [[Turn]], [[Faith]], [[Into]], [[Process]]
Def: [[Person]], [[Who]], [[Measure]], [[Soul]]
""",

"religion/believers/Methodist.md": """
Def: [[Person]], [[Who]], [[Like]], [[Group]]
Def: [[Person]], [[Who]], [[Do]], [[Good]], [[Work]]
""",

"religion/sects/Latter-day Saints.md": """
Def: [[Christian]], [[Sect]]
Def: [[Group]], [[With]], [[New]], [[Book]]
""",

"religion/founders/Joseph Smith.md": """
Def: [[Joseph]], [[Smith]]
Def: [[Person]], [[Who]], [[Invent]], [[Scripture]]
Def: [[Person]], [[Who]], [[Build]], [[City]]
""",

"religion/believers/Mormon.md": """
Def: [[Person]], [[Who]], [[Follow]], [[Hierarchy]]
Def: [[Person]], [[Who]], [[Knock]], [[On]], [[Door]]
""",

# =======================
# Judaism
# =======================

"religion/sects/Hasidic Judaism.md": """
Def: [[Jewish]], [[Sect]]
Def: [[Group]], [[That]], [[Feel]], [[Joy]]
""",

"religion/founders/Baal Shem Tov.md": """
Def: [[Baal]], [[Shem]], [[Tov]]
Def: [[Person]], [[With]], [[Charisma]]
Def: [[Person]], [[Who]], [[Make]], [[God]], [[Close]]
""",

"religion/believers/Hasid.md": """
Def: [[Person]], [[Who]], [[Live]], [[Tradition]]
Def: [[Person]], [[Who]], [[Dance]]
""",

"religion/sects/Reform Judaism.md": """
Def: [[Jewish]], [[Sect]]
Def: [[Group]], [[That]], [[Change]], [[Rule]]
""",

"religion/founders/Abraham Geiger.md": """
Def: [[Abraham]], [[Geiger]]
Def: [[Person]], [[Who]], [[Edit]], [[Religion]]
Def: [[Person]], [[Who]], [[Use]], [[History]], [[As]], [[Tool]]
""",

"religion/believers/Reform Jew.md": """
Def: [[Person]], [[Who]], [[Care]], [[About]], [[Ethic]]
Def: [[Person]], [[Who]], [[Do]], [[Not]], [[Care]], [[About]], [[Ritual]]
""",

# =======================
# Islam
# =======================

"religion/sects/Shia Islam.md": """
Def: [[Islam]], [[Sect]]
Def: [[Group]], [[About]], [[Who]], [[Lead]]
""",

"religion/founders/Ali ibn Abi Talib.md": """
Def: [[Ali]]
Def: [[Person]], [[With]], [[Moral]], [[Claim]]
Def: [[Person]], [[Who]], [[Lose]], [[Power]]
""",

"religion/believers/Shia.md": """
Def: [[Person]], [[Who]], [[Remember]], [[Pain]]
Def: [[Person]], [[Who]], [[Repeat]], [[Ritual]]
""",

"religion/sects/Wahhabism.md": """
Def: [[Islam]], [[Sect]]
Def: [[Group]], [[That]], [[Delete]], [[Other]], [[Idea]]
""",

"religion/founders/Muhammad ibn Abd al-Wahhab.md": """
Def: [[Muhammad]], [[ibn]], [[Abd]], [[al-Wahhab]]
Def: [[Person]], [[Who]], [[Reduce]], [[Religion]]
Def: [[Person]], [[Who]], [[Merge]], [[With]], [[State]]
""",

"religion/believers/Wahhabi.md": """
Def: [[Person]], [[Who]], [[Follow]], [[Rule]]
Def: [[Person]], [[Who]], [[Hate]], [[Ambiguity]]
""",

# =======================
# Buddhism
# =======================

"religion/sects/Buddhism.md": """
Def: [[Religion]]
Def: [[System]], [[For]], [[End]], [[Suffering]]
""",

"religion/founders/Buddha.md": """
Def: [[Buddha]]
Def: [[Person]], [[Who]], [[Sit]]
Def: [[Person]], [[Who]], [[See]], [[Pattern]]
""",

"religion/believers/Buddhist.md": """
Def: [[Person]], [[Who]], [[Practice]]
Def: [[Person]], [[Who]], [[Accept]], [[Silence]]
""",

# =======================
# New Religions
# =======================

"religion/sects/Scientology.md": """
Def: [[Religion]]
Def: [[Organization]], [[With]], [[Lawyers]]
""",

"religion/founders/L. Ron Hubbard.md": """
Def: [[L.]], [[Ron]], [[Hubbard]]
Def: [[Person]], [[Who]], [[Sell]], [[System]]
Def: [[Person]], [[Who]], [[Control]], [[Narrative]]
""",

"religion/believers/Scientologist.md": """
Def: [[Person]], [[Who]], [[Follow]], [[Procedure]]
Def: [[Person]], [[Who]], [[Pay]]
""",

"religion/sects/Theosophy.md": """
Def: [[Religion]]
Def: [[Idea]], [[Soup]]
""",

"religion/founders/Helena Blavatsky.md": """
Def: [[Helena]], [[Blavatsky]]
Def: [[Person]], [[Who]], [[Combine]], [[Everything]]
Def: [[Person]], [[Who]], [[Not]], [[Care]], [[If]], [[Contradiction]]
""",

"religion/believers/Theosophist.md": """
Def: [[Person]], [[Who]], [[Read]], [[Weird]], [[Book]]
Def: [[Person]], [[Who]], [[Never]], [[Finish]]
""",
}

def main():
    root = Path.cwd()
    for rel_path, content in FILES.items():
        path = root / rel_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content.strip() + "\n", encoding="utf-8")
        print(f"wrote {path}")

if __name__ == "__main__":
    main()

