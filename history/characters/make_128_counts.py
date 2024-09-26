import os
import random

dynasty_name = [
	"dynn_Anogaryen", "dynn_Atroksiarys", "dynn_Daomiorys", "dynn_Embaryen", "dynn_Gelenkys",
	"dynn_Gelionar", "dynn_Gryvetheon", "dynn_Hoskagys", "dynn_Haedaryen", "dynn_Ilirigys",
	"dynn_Jelmazeon", "dynn_Jentys", "dynn_Kastaryen", "dynn_Kostagar", "dynn_Mazigonys",
	"dynn_Namorghulilaryen", "dynn_Ondoryen", "dynn_Perzys", "dynn_Qogrorys", "dynn_Syzeon",
	"dynn_Tresys", "dynn_Belaerys", "dynn_Zaldrizyen", "dynn_Manaereon", "dynn_Urnebar",
	"dynn_Sonaryen", "dynn_Kessatheon", "dynn_Bevilar", "dynn_Ezimatheon", "dynn_Laeseon",
	"dynn_Jenqeleon", "dynn_Pirtiryen", "dynn_Sytivilar", "dynn_Tistaleon", "dynn_Qupteneon",
	"dynn_Nuqiryen", "dynn_Orbareon", "dynn_Quvyar", "dynn_Valzyren", "dynn_Ilontheon",
	"dynn_Boniryen", "dynn_Jorraezys", "dynn_Quptys", "dynn_Tyvar", "dynn_Jomozar",
	"dynn_Huretheon", "dynn_Ruakys", "dynn_Celereon", "dynn_Jaeganyon", "dynn_Arranion",
	"dynn_Vezenkar", "dynn_Unendia", "dynn_Voksia", "dynn_Galgaeron", "dynn_Laergyr",
	"dynn_Enreos", "dynn_Merntys", "dynn_Maznareon", "dynn_Henaeris", "dynn_Ronnon",
	"dynn_Haeteros", "dynn_Gevgarys", "dynn_Hurys", "dynn_Pyllyr", "dynn_Raegaros"
]
name = [
    "Aemon", "Daeron", "Jaehaerys", "Viserys", "Bearaxes", "Bearlerion", "Beargar",
    "Aegor", "Aelor", "Aelyx", "Aenar", "Aenys", "Aerion", "Aeryn", "Aerys", "Aethan",
    "Baelon", "Baelor",
    "Daemion", "Daemon",
    "Gaemon",
    "Haegon",
    "Maegon", "Maekar", "Maelor", "Maelys", "Maenar", "Matarys",
    "Rhaegar", "Rhaegel",
    "Vaegon", "Valarr", "Valerion",
    "Aemond", "Maegor"
]

def create_counts():
    count_number = 1
    lines = []
    
    while count_number < 127:
        lines.append('mrcount_' + str(count_number) + ' = {')
        lines.append('\tname = ' + random.choice(name))
        lines.append('\tdynasty = ' + random.choice(dynasty_name) + '\n')
        lines.append('\treligion = valyrian')
        lines.append('\tculture = high_valyrian\n')
        lines.append('\t' + str(random.randint(7838, 7872)) + '.' + str(random.randint(1, 12)) + '.' + str(random.randint(1, 29)) + ' = {')
        lines.append('\t\tbirth = yes')
        lines.append('\t}')
        lines.append('}')
        count_number += 1

    return '\n'.join(lines)




script_dir = os.path.dirname(os.path.abspath(__file__))

count_document = os.path.join(script_dir, 'vf_counts.txt')

actual_text = create_counts()


with open(count_document, 'w', encoding='utf-8') as file:
    file.write(actual_text)
