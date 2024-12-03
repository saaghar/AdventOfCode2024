# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

'''
In the example list above, the pairs and distances would be as follows:

The smallest number in the left list is 1, and the smallest number in the right list is 3. The distance between them is 2.
The second-smallest number in the left list is 2, and the second-smallest number in the right list is another 3. The distance between them is 1.
The third-smallest number in both lists is 3, so the distance between them is 0.
The next numbers to pair up are 3 and 4, a distance of 1.
The fifth-smallest numbers in each list are 3 and 5, a distance of 2.
Finally, the largest number in the left list is 4, while the largest number in the right list is 9;
these are a distance 5 apart.
'''


# Original list with pairs of numbers (two columns)
original_list = [
    (88276, 66757), (66898, 13714), (58877, 87487), (69396, 12997), (53434, 62485),
    (69841, 67231), (51135, 99904), (75350, 18379), (87528, 59461), (33533, 35866),
    (88767, 25688), (70018, 18379), (25424, 37382), (46726, 68550), (41136, 44070),
    (81001, 57100), (48800, 20883), (68425, 87909), (32161, 69003), (18867, 53216),
    (58177, 19563), (67114, 46700), (48598, 90768), (49215, 39678), (50571, 65700),
    (57798, 56585), (87680, 69003), (81941, 15557), (25776, 32379), (61540, 58056),
    (30036, 13872), (72011, 69003), (74083, 56426), (87228, 81833), (49402, 73309),
    (20185, 37731), (79992, 61292), (83744, 53216), (51270, 88596), (65194, 46832),
    (83619, 84894), (61729, 48656), (22798, 27189), (17489, 88767), (72632, 85830),
    (20376, 74164), (14663, 10793), (75764, 18838), (42214, 79141), (73812, 70018),
    (77490, 16156), (58694, 13273), (84894, 57554), (89172, 61675), (26728, 10793),
    (38031, 20716), (42918, 72362), (71012, 67914), (54495, 54567), (46702, 63623),
    (43028, 14772), (35521, 30594), (67868, 67268), (34274, 24937), (20784, 48924),
    (35595, 84894), (34154, 24579), (44840, 59881), (36669, 56576), (41986, 66757),
    (46387, 17065), (44020, 21738), (84238, 17801), (36022, 30633), (71031, 18379),
    (64368, 17801), (10793, 84894), (20169, 34934), (18550, 70811), (88728, 62854),
    (66508, 64049), (18159, 54705), (39451, 58284), (42664, 38958), (23446, 75653),
    (97584, 43691), (78504, 58006), (26535, 53216), (15557, 21045), (28271, 47020),
    (36597, 50514), (46447, 13273), (95598, 22815), (93731, 81772), (32397, 42899),
    (52807, 58056), (26220, 59055), (95837, 54705), (67607, 97159), (37466, 45429),
    (43058, 45549), (26473, 38665), (68777, 98333), (22436, 91327), (88573, 18379),
    (61259, 13273), (38254, 22391), (93975, 44919), (57986, 86639), (77318, 62161),
    (84495, 36775), (81381, 69003), (57739, 16156), (60598, 40116), (33182, 57284),
    (93710, 40019), (37609, 19836), (78984, 38227), (22162, 87784), (55715, 79073),
    (63919, 45370), (90630, 87468), (25719, 18379), (94542, 80660), (46758, 65583),
    (81729, 67887), (38275, 92261), (98915, 65294), (56501, 83143), (26391, 18379),
    (20345, 88767), (90235, 72889), (76165, 65757), (34771, 17801), (11831, 85257),
    (17735, 15601), (82093, 80861), (74646, 34915), (18879, 15331), (62123, 90282),
    (76704, 10793), (35340, 46892), (17626, 57504), (73828, 23294), (60131, 44363),
    (93584, 10793), (62201, 44764), (19005, 87646), (35018, 42747), (47795, 36954),
    (41800, 78433), (80773, 85010), (80820, 34934), (22857, 81640), (37449, 10995),
    (82183, 24232), (45864, 46505), (36815, 48985), (54020, 13273), (81545, 88831),
    (62572, 18336), (44708, 64739), (66801, 97842), (59501, 12794), (67098, 75382),
    (21266, 53216), (58508, 43409), (84719, 20883), (45950, 65647), (70627, 47730),
    (94298, 87646), (11607, 88003), (99117, 20883), (17953, 13714), (31425, 86162),
    (85902, 88767), (88524, 97877), (63952, 35026), (19191, 38958), (79802, 15331),
    (57866, 56895), (62302, 46538), (78098, 95481), (20698, 43965), (84629, 80543),
    (41677, 21616), (27485, 27525), (75935, 45791), (31977, 16820), (10336, 78794),
    (38958, 13714), (84834, 61769), (96511, 44057), (12736, 28591), (89758, 59184),
    (53646, 54868), (15153, 91337), (32060, 34232), (27908, 45791), (16393, 78168),
    (25261, 52734), (60760, 38227), (25775, 20883), (16904, 29227), (62346, 53147),
    (47080, 42526), (93255, 70760), (89013, 13714), (43284, 69177), (65144, 93383),
    (48707, 87646), (57437, 58056), (11138, 75483), (24856, 38227), (29683, 60040),
    (98693, 55209), (77263, 69834), (30391, 66757), (33113, 47463), (65000, 34934),
    (31396, 62769), (46020, 54868), (99476, 85419), (11386, 68175), (13977, 58056),
    (86041, 38227), (62608, 84894), (80461, 68879), (42619, 35285), (18929, 71805),
    (91858, 28002), (19069, 58965), (61625, 39986), (13273, 26273), (58290, 17801)
]

# Flatten the list into a single list
flattened_list = [item for sublist in original_list for item in sublist]

# Print the flattened list
print(flattened_list)


# Separera vänster och höger kolumn
left_column = [pair[0] for pair in original_list]
right_column = [pair[1] for pair in original_list]

# Visa listorna
print("Vänster kolumn:", left_column)
print("Höger kolumn:", right_column)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/