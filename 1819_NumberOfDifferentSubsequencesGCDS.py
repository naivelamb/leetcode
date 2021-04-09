import math
class Solution:
    def countDifferentSubsequenceGCDs(self, nums) -> int:
        res = 0
        all_nums = set(nums)
        for i in range(1, 200001):
            current_gcd = None
            for k in range(i, 200001, i):
                if k in all_nums:
                    if current_gcd is None:
                        current_gcd = k
                    else:
                        current_gcd = math.gcd(current_gcd, k)
                    if current_gcd == i:
                        res += 1
                        break
        return res

s = Solution()
#tmp = [5852,6671,170275,141929,2414,99931,179958,56781,110656,190278,7613,138315,58116,114790,129975,144929,61102,90624,60521,177432,57353,199478,120483,75965,5634,109100,145872,168374,26215,48735,164982,189698,77697,31691,194812,87215,189133,186435,131282,110653,133096,175717,49768,79527,74491,154031,130905,132458,103116,154404,9051,125889,63633,194965,105982,108610,174259,45353,96240,143865,184298,176813,193519,98227,22667,115072,174001,133281,28294,42913,136561,103090,97131,128371,192091,7753,123030,11400,80880,184388,161169,155500,151566,103180,169649,44657,44196,131659,59491,3225,52303,141458,143744,60864,106026,134683,90132,151466,92609,120359,70590,172810,143654,159632,191208,1497,100582,194119,134349,33882,135969,147157,53867,111698,14713,126118,95614,149422,145333,52387,132310,108371,127121,93531,108639,90723,416,141159,141587,163445,160551,86806,120101,157249,7334,60190,166559,46455,144378,153213,47392,24013,144449,66924,8509,176453,18469,21820,4376,118751,3817,197695,198073,73715,65421,70423,28702,163789,48395,90289,76097,18224,43902,41845,66904,138250,44079,172139,71543,169923,186540,77200,119198,184190,84411,130153,124197,29935,6196,81791,101334,90006,110342,49294,67744,28512,66443,191406,133724,54812,158768,113156,5458,59081,4684,104154,38395,9261,188439,42003,116830,184709,132726,177780,111848,142791,57829,165354,182204,135424,118187,58510,137337,170003,8048,103521,176922,150955,84213,172969,165400,111752,15411,193319,78278,32948,55610,12437,80318,18541,20040,81360,78088,194994,41474,109098,148096,66155,34182,2224,146989,9940,154819,57041,149496,120810,44963,184556,163306,133399,9811,99083,52536,90946,25959,53940,150309,176726,113496,155035,50888,129067,27375,174577,102253,77614,132149,131020,4509,85288,160466,105468,73755,4743,41148,52653,85916,147677,35427,88892,112523,55845,69871,176805,25273,99414,143558,90139,180122,140072,127009,139598,61510,17124,190177,10591,22199,34870,44485,43661,141089,55829,70258,198998,87094,157342,132616,66924,96498,88828,89204,29862,76341,61654,158331,187462,128135,35481,152033,144487,27336,84077,10260,106588,19188,99676,38622,32773,89365,30066,161268,153986,99101,20094,149627,144252,58646,148365,21429,69921,95655,77478,147967,140063,29968,120002,72662,28241,11994,77526,3246,160872,175745,3814,24035,108406,30174,10492,49263,62819,153825,110367,42473,30293,118203,43879,178492,63287,41667,195037,26958,114060,99164,142325,77077,144235,66430,186545,125046,82434,26249,54425,170932,83209,10387,7147,2755,77477,190444,156388,83952,117925,102569,82125,104479,16506,16828,83192,157666,119501,29193,65553,56412,161955,142322,180405,122925,173496,93278,67918,48031,141978,54484,80563,52224,64588,94494,21331,73607,23440,197470,117415,23722,170921,150565,168681,88837,59619,102362,80422,10762,85785,48972,83031,151784,79380,64448,87644,26463,142666,160273,151778,156229,24129,64251,57713,5341,63901,105323,18961,70272,144496,18591,191148,19695,5640,166562,2600,76238,196800,94160,129306,122903,40418,26460,131447,86008,20214,133503,174391,45415,47073,39208,37104,83830,80118,28018,185946,134836,157783,76937,33109,54196,37141,142998,189433,8326,82856,163455,176213,144953,195608,180774,53854,46703,78362,113414,140901,41392,12730,187387,175055,64828,66215,16886,178803,117099,112767,143988,65594,141919,115186,141050,118833,2849]
tmp = [187378,36750,83797,174965,195523,94032,118488,196037,49939,104929,121535,22527,103371,95912,2572,74742,55463,153208,93338,98162,163921,1961,24871,116738,198965,106251,80398,183552,45427,78429,192641,170850,57476,195131,86500,87141,55530,10732,13359,4874,185402,47698,157574,121218,85005,187044,9630,69714,155621,137737,71178,17254,188198,167897,65512,3110,34087,197063,108346,91074,70772,130670,10234,101122,29052,80019,181489,109895,196962,65064,60140,135776,152952,114289,148642,69202,2725,1528,39727,124507,185757,39098,91772,20337,156752,64877,145993,168847,144241,40461,34800,105124,36399,160222,182125,191868,86555,50939,33945,35875,159380,180463,30533,33345,8764,156223,72939,71570,92392,1945,38105,183644,2273,16715,119589,187828,113461,187193,104232,81112,179468,35043,102683,111696,198076,94375,117421,91703,76645,124568,48665,70502,2092,81660,60277,182246,13924,130935,15648,1976,20750,155685,121428,658,167125,64344,34728,186570,102776,192544,161676,101826,58325,155596,161920,72561,48060,189460,57198,42342,23746,86607,90942,22584,31981,145811,60495,53656,86130,146842,140616,117435,185036,21711,113077,149849,93421,43269,47473,162001,26642,92869,48427,180203,129311,160080,20778,119560,113088,57322,16623,17745,174578,166174,65981,86057,102775,96566,152457,85556,112812,135431,162693,156929,170735,18533,49863,107911,91131,138083,193268,130343,90856,181741,31294,117285,86321,2280,59054,79727,107708,175156,177872,36685,50204,72909,184892,133425,161491,12128,42548,152060,81279,14929,173176,29165,69661,167268,154503,29266,47107,185161,167849,146330,118539,149390,64963,122821,112975,14307,36934,129198,94336,131872,76483,195074,98415,23336,148355,114586,34037,179571,182603,133406,61123,112195,127608,16426,154853,189592,94819,139484,136492,48526,16256,185146,53484,49686,4866,90984,62292,62608,186003,138125,138003,170306,107680,146364,108785,43310,61533,207,57579,133806,139643,14879,171871,40733,143848,23660,6478,37299,142765,69843,60188,94577,87184,191622,36121,24581,67067,108167,93219,155666,11127,143787,16290,176497,120136,9915,191633,166903,82436,81629,78702,176955,194319,102157,80428,100912,126477,77240,176240,31432,153366,180154,170619,2972,187297,27721,111145,19296,54675,32261,165360,2470,64391,123008,18580,55753,89350,56320,77614,74899,121923,121921,182559,146354,150246,187141,133546,55161,182343,121330,98692,21896,192387,8087,19344,78871,189288,163022,117800,53700,188815,77403,108620,48482,168439,159043,174514,103471,98307,190832,121382,58022,64663,129413,3695,76708,70351,124292,129365,92288,197803,28690,155503,189402,181699,175641,196660,31433,56116,180648,117050,101728,56363,110389,16172,191054,46131,199537,184054,179111,101325,111440,97925,137788,37151,17819,134152,186649,41878,11785,152609,55609,199131,131793,142487,189326,121984,171717,81280,78895,124654,35327,5512,185419,118275,113694,175283,176709,151705,90455,114224,186588,95235,57112,70845,53299,175254,120884,151303,124207,71151,180101,163428,108897,74592,72598,116350,17256,29142,85259,117369,178779,177523,75300,136023,59483,133442,83944,65079,40656,41160,66672,185623,65051,107944,7920,176655,112537,104357,59076,35652,18851,22237,43317,122874,157867,190637,99481,57644,76582,158287,102563,70345,2078,74402,39272,31501,194520,112980,73841,193649,175787,78882,180486,109759,145272,16039,173579,195341,178755,38980,25524,43399,135888,127782,113523,29077,15078]

print(s.countDifferentSubsequenceGCDs(tmp))