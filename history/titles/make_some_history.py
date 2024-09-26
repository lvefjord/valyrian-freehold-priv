import os
import random
import re

county_list = [
	"c_aelzor",
	"c_velys",
	"c_daelthor",
	"c_rhaenor",
	"c_naeryth",
	"c_valthar",
	"c_oelyth",
	"c_qaenor",
	"c_gaelthor",
	"c_haelyx",
	"c_maenor",
	"c_xaeryth",
	"c_vaelythor",
	"c_yrnith",
	"c_zhaenor",
	"c_laerion",
	"c_saelzor",
	"c_paelion",
	"c_erythor",
	"c_qaelyx",
	"c_aerith",
	"c_raelyx",
	"c_daenyth",
	"c_vaelor",
	"c_maelrion",
	"c_jaelys",
	"c_zhaeryth",
	"c_faenys",
	"c_oelryth",
	"c_qaelyth",
	"c_brythor",
	"c_xaelyth",
	"c_ilythar",
	"c_haenith",
	"c_aelion",
	"c_zaelthor",
	"c_vaenor",
	"c_jaenyth",
	"c_laenith",
	"c_elythar",
	"c_naelrion",
	"c_paenor",
	"c_vaelion",
	"c_zhaelyth",
	"c_xaelor",
	"c_ulenor",
	"c_saelion",
	"c_ilyzor",
	"c_maelyth",
	"c_brynith",
	"c_valyria",
	"c_taelion",
	"c_gaenor",
	"c_faelrion",
	"c_haerith",
	"c_vaeryth",
	"c_xaenor",
	"c_jaelion",
	"c_naenith",
	"c_raelion",
	"c_aelrion",
	"c_qaenith",
	"c_gaelion",
	"c_saenor",
	"c_aenythor",
	"c_velrion",
	"c_daelryn",
	"c_rhaelyth",
	"c_naelthor",
	"c_valenor",
	"c_oelyrion",
	"c_qaelrion",
	"c_gaelyr",
	"c_haelthor",
	"c_maeryn",
	"c_xaelynor",
	"c_vaenyth",
	"c_yrithor",
	"c_zhaenyth",
	"c_laelthor",
	"c_saelrion",
	"c_paelys",
	"c_elynor",
	"c_qaenithor",
	"c_aerionor",
	"c_raelthorion",
	"c_daelynor",
	"c_vaelrion",
	"c_maelryth",
	"c_jaeryn",
	"c_zhaelor",
	"c_faelith",
	"c_oelrynor",
	"c_qaelthor",
	"c_brynysor",
	"c_xaelionor",
	"c_ilynor",
	"c_haelryth",
	"c_aelrith",
	"c_zaelryth",
	"c_vaelorion",
	"c_jaenorion",
	"c_laelythor",
	"c_elythorion",
	"c_naelythar",
	"c_paelzor",
	"c_vaelysor",
	"c_zhaelthor",
	"c_xaelythion",
	"c_ulythar",
	"c_saelynor",
	"c_ilyrion",
	"c_maenythor",
	"c_brythorion",
	"c_qaenorion",
	"c_taelythar",
	"c_gaelzor",
	"c_faelynor",
	"c_haenorion",
	"c_vaelzorion",
	"c_xaelrynor",
	"c_jaelrithor",
	"c_naerythion",
	"c_raelythor",
	"c_aelyrion",
	"c_qaelythorion"
]

script_dir = os.path.dirname(os.path.abspath(__file__))
count_document = os.path.join(r'C:\Users\Ive\Documents\Paradox Interactive\Crusader Kings III\mod\valyrian freehold priv\history\characters\vf_counts_with_python.txt')
history_document = os.path.join(script_dir, 'vf_countyhistory_with_python.txt')

with open(count_document, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Join the lines into a single string
file_content = ''.join(lines)

# Find all occurrences of mrcount_*number*
holder_list = re.findall(r'mrcount_\d+', file_content)

# Debugging information
print(f"Number of counties: {len(county_list)}")
print(f"Number of holders: {len(holder_list)}")
print("Holders found:")
for holder in holder_list:
    print(holder)

with open(history_document, 'w', encoding='utf-8') as file:
    history_lines = []
    i = 0
    for county in county_list:
        if i < 127:
            history_lines.append(str(county) + ' = {')
            history_lines.append('\t' + str(random.randint(7873, 7887)) + '.' + str(random.randint(1, 12)) + '.' + str(random.randint(1, 29)) + ' = {')
            if i < len(holder_list):
                history_lines.append('\t\t holder = ' + str(holder_list[i]))
            else:
                print(f"Warning: No holder available for county {county} at index {i}")
                history_lines.append('\t\t holder = unknown')
            history_lines.append('\t}')
            history_lines.append('}')
            i += 1

    file.write('\n'.join(history_lines))

    file.write