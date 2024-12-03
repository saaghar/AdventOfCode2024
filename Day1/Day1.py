
'''
Sort both lists: Arrange the numbers in each list from smallest to largest.
Pair up the numbers: Match the smallest number from the first list with the smallest number from the second list, the second smallest with the second smallest, and so on.
Calculate the distances: For each pair of numbers, subtract the smaller number from the larger one to find how far apart they are.
Add up the distances: Add all the differences together to find the total distance between the two lists.
'''

'''Here's how to do it:
1. Sort both lists: Arrange the numbers in each list from smallest to largest. Done 
2. Pair up the numbers: Match the smallest number from the first list with the smallest number from the second list, 
the second smallest with the second smallest, and so on.
3. Calculate the distances: For each pair of numbers, subtract the smaller 
number from the larger one to find how far apart they are.
4. Add up the distances: Add all the differences together to find the total 
distance between the two lists.'''


def sort_list (_list):
    for i in range(0, len(_list)):
        for j in range (i+1, len(_list)):
            if _list[i] >= _list[j]:
                #temp variable
                temp = _list[i]
                _list[i] = _list[j]
                _list[j] = temp
    return _list


def pair_up_numbers (_list1, _list2):

    sort_list(_list1)
    sort_list(_list2)

    total_dif = 0
    for i in range(len(_list1)):
        dif = abs(_list1[i] - _list2[i])
        total_dif += dif
    return total_dif

left_c = [   88276, 66898, 58877, 69396, 53434, 69841, 51135, 75350, 87528, 33533, 88767, 70018, 25424, 46726, 41136,
             81001, 48800, 68425, 32161, 18867, 58177, 67114, 48598, 49215, 50571, 57798, 87680, 81941, 25776, 61540,
             30036, 72011, 74083, 87228, 49402, 20185, 79992, 83744, 51270, 65194, 83619, 61729, 22798, 17489, 72632,
             20376, 14663, 75764, 42214, 73812, 77490, 58694, 84894, 89172, 26728, 38031, 42918, 71012, 54495, 46702,
             43028, 35521, 67868, 34274, 20784, 35595, 34154, 44840, 36669, 41986, 46387, 44020, 84238, 36022, 71031,
             64368, 10793, 20169, 18550, 88728, 66508, 18159, 39451, 42664, 23446, 97584, 78504, 26535, 15557, 28271,
             36597, 46447, 95598, 93731, 32397, 52807, 26220, 95837, 67607, 37466, 43058, 26473, 68777, 22436, 88573,
             61259, 38254, 93975, 57986, 77318, 84495, 81381, 57739, 60598, 33182, 93710, 37609, 78984, 22162, 55715,
             63919, 90630, 25719, 94542, 46758, 81729, 38275, 98915, 56501, 26391, 20345, 90235, 76165, 34771, 11831,
             17735, 82093, 74646, 18879, 62123, 76704, 35340, 17626, 73828, 60131, 93584, 62201, 19005, 35018, 47795,
             41800, 80773, 80820, 22857, 37449, 82183, 45864, 36815, 54020, 81545, 62572, 44708, 66801, 59501, 67098,
             21266, 58508, 84719, 45950, 70627, 94298, 11607, 99117, 17953, 31425, 85902, 88524, 63952, 19191, 79802,
             57866, 62302, 78098, 20698, 84629, 41677, 27485, 75935, 31977, 10336, 38958, 84834, 96511, 12736, 89758,
             53646, 15153, 32060, 27908, 16393, 25261, 60760, 25775, 16904, 62346, 47080, 93255, 89013, 43284, 65144,
             48707, 57437, 11138, 24856, 29683, 98693, 77263, 30391, 33113, 65000, 31396, 46020, 99476, 11386, 13977,
             86041, 62608, 80461, 42619, 18929, 91858, 19069, 61625, 13273, 58290]
right_c = [  66757, 13714, 87487, 12997, 62485, 67231, 99904, 18379, 59461, 35866, 25688, 18379, 37382, 68550, 44070,
             57100, 20883, 87909, 69003, 53216, 19563, 46700, 90768, 39678, 65700, 56585, 69003, 15557, 32379, 58056,
             13872, 69003, 56426, 81833, 73309, 37731, 61292, 53216, 88596, 46832, 84894, 48656, 27189, 88767, 85830,
             74164, 10793, 18838, 79141, 70018, 16156, 13273, 57554, 61675, 10793, 20716, 72362, 67914, 54567, 63623,
             14772, 30594, 67268, 24937, 48924, 84894, 24579, 59881, 56576, 66757, 17065, 21738, 17801, 30633, 18379,
             17801, 84894, 34934, 70811, 62854, 64049, 54705, 58284, 38958, 75653, 43691, 58006, 53216, 21045, 47020,
             50514, 13273, 22815, 81772, 42899, 58056, 59055, 54705, 97159, 45429, 45549, 38665, 98333, 91327, 18379,
             13273, 22391, 44919, 86639, 62161, 36775, 69003, 16156, 40116, 57284, 40019, 19836, 38227, 87784, 79073,
             45370, 87468, 18379, 80660, 65583, 67887, 92261, 65294, 83143, 18379, 88767, 72889, 65757, 17801, 85257,
             15601, 80861, 34915, 15331, 90282, 10793, 46892, 57504, 23294, 44363, 10793, 44764, 87646, 42747, 36954,
             78433, 85010, 34934, 81640, 10995, 24232, 46505, 48985, 13273, 88831, 18336, 64739, 97842, 12794, 75382,
             53216, 43409, 20883, 65647, 47730, 87646, 88003, 20883, 13714, 86162, 88767, 97877, 35026, 38958, 15331,
             56895, 46538, 95481, 43965, 80543, 21616, 27525, 45791, 16820, 78794, 13714, 61769, 44057, 28591, 59184,
             54868, 91337, 34232, 45791, 78168, 52734, 38227, 20883, 29227, 53147, 42526, 70760, 13714, 69177, 93383,
             87646, 58056, 75483, 38227, 60040, 55209, 69834, 66757, 47463, 34934, 62769, 54868, 85419, 68175, 58056,
             38227, 84894, 68879, 35285, 71805, 28002, 58965, 39986, 26273, 17801]


difference = pair_up_numbers(right_c, left_c)
print(difference)
