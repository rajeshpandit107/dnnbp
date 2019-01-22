def sigmf(x):
	import math

	return 1 / (1 + math.exp(-x))

def cell(w, x, prev_h, prev_c):
	import numpy as np

	# X = prev_h + x + [1]
	X = np.append(prev_h, x)
	X = np.append(X, np.array([1])) # 1 ini buat dikali sama bias

	a = np.tanh(np.dot(w[0], X))
	i = sigmf(np.dot(w[1], X))
	f = sigmf(np.dot(w[2], X))
	o = sigmf(np.dot(w[3], X))

	# print(a,i,f, prev_c)

	c = a * i + f * prev_c
	h = np.tanh(c) * o

	return h, c

# def run(x):
# 	# U, W, B
# 	wa1 = [0, 0.15, 0.25, 0.45, 0.20]
# 	wi1 = [0, 0.80, 0.80, 0.95, 0.65]
# 	wf1 = [0, 0.10, 0.45, 0.70, 0.15]
# 	wo1 = [0, 0.25, 0.40, 0.60, 0.10]

# 	W10 = [wa1, wi1, wf1, wo1]

# 	wa1 = [0.15, 0.25, 0.45, 0.20, 0]
# 	wi1 = [0.80, 0.80, 0.95, 0.65, 0]
# 	wf1 = [0.10, 0.45, 0.70, 0.15, 0]
# 	wo1 = [0.25, 0.40, 0.60, 0.10, 0]

# 	W11 = [wa1, wi1, wf1, wo1]

# 	wa2 = [0.15, 0.25, 0.45, 0.20]
# 	wi2 = [0.80, 0.80, 0.95, 0.65]
# 	wf2 = [0.10, 0.45, 0.70, 0.15]
# 	wo2 = [0.25, 0.40, 0.60, 0.10]

# 	W2 = [wa2, wi2, wf2, wo2]

# 	H1 = [[0, 0]]
# 	H2 = [[0]]

# 	C1 = [[0, 0]]
# 	C2 = [[0]]

# 	for i, item in enumerate(x):
# 		h_temp = []
# 		c_temp = []

# 		# calculate cell 1 of layer 1
# 		h, c = cell(W10, item, H1[i], C1[i][0])
# 		h_temp.append(h); c_temp.append(c)

# 		# calculate cell2 of layer 1
# 		h, c = cell(W11, item, H1[i], C1[i][1])
# 		h_temp.append(h); c_temp.append(c)

# 		# adding outputs to H1 & C1 memory
# 		H1.append(h_temp); C1.append(c_temp)

# 		h_temp = []
# 		c_temp = []

# 		# calculate cell 1 of layer 2
# 		# print("print", H1[i+1],H2[i], C2[i][0])
# 		h, c = cell(W2, H1[i+1], H2[i], C2[i][0])
# 		h_temp.append(h); c_temp.append(c)

# 		# adding outputs to H2 & C2 memory
# 		H2.append(h_temp); C2.append(c_temp)

# 	print("H1:\n", H1)
# 	print("C1:\n", C1)
# 	print("H2:\n", H2)
# 	print("C2:\n", C2)

# def tb():
# 	x = [[2,1], [2,1], [2,1], [2,1], [2,1], [2,1], [2,1]]
# 	run(x);

if __name__ == "__main__":
	import numpy as np

	# cell 4
	# W_i = [
	# 	 -0.00651917, -0.15639755, -0.14184645, -0.1212172,   0.04775171,  0.07724813,
	# 	 -0.05459924, -0.1473062 , -0.04456262, -0.12122583,  0.02838087,  0.12484984,
	# 	 -0.09658161, -0.0544478 ,  0.12316187, -0.06415586,  0.06690548, -0.02223762,
	# 	 -0.01942247,  0.10455464,  0.09432151,  0.04022662, -0.10823,     0.11307148,
	# 	 -0.02866874,  0.06664595, -0.07292868, -0.09498388, -0.06814551,  0.10701226,
	# 	  0.07863889, -0.03617415, -0.02169011, -0.06229361,  0.07385953,  0.1215181,
	# 	  0.05198291,  0.09322705,  0.13521336, -0.14459117,  0.06281399, -0.03890364,
	# 	 -0.0006937 ,  0.01385748, -0.07040884, -0.12574317, -0.12829338,  0.11642888,
	# 	 -0.06898572,  0.00021582, -0.04377563, -0.09790096, -0.06424016
	# 	]
	# W_f = [
	# 	 -0.02453584, -0.10196738,  0.08706138,  0.140378,   -0.14147523,  0.11478967,
	# 	 -0.08246098,  0.07222234, -0.0543694,  -0.09139033, -0.1427913,   0.08906263,
	# 	  0.03573965,  0.10340317, -0.09805319, -0.08604964,  0.09104414,  0.01703342,
	# 	 -0.11277716, -0.1238602,   0.00648234, -0.0416004,  -0.02404536, -0.023228,
	# 	 -0.08615823, -0.0353624,   0.03912978, -0.11898746,  0.10231845,  0.13058804,
	# 	  0.12943256, -0.1102967,  -0.14007008, -0.05517979, -0.00691686, -0.11043198,
	# 	 -0.04352543, -0.04794159, -0.07174501,  0.07835992, -0.07984751, -0.05602729,
	# 	  0.01126647, -0.04268992, -0.00917423,  0.06331417,  0.09447785,  0.14358553,
	# 	 -0.11134878, -0.14719787, -0.09936729, -0.06209351,  0.04299457
	# 	]
	# W_a = [
	# 	 -0.19452587,  0.02068138,  0.18085736,  0.14226761, -0.0316235 ,  0.15386885,
	# 	 -0.07112437,  0.03086472, -0.16951743, -0.15292245,  0.04267162,  0.02472915,
	# 	 -0.18109281, -0.03524796,  0.76182544,  0.05267655,  0.65821135,  0.25317886,
	# 	  0.19925663, -0.5536641,  -0.84355736, -0.4533724,  -0.06754421, -0.76409686,
	# 	  0.54789335,  0.09356738,  0.16743895, -0.23186508, -0.22452523,  0.10295425,
	# 	 -0.14949556,  0.14419022, -0.15950894,  0.01691391, -0.16008304,  0.10616001,
	# 	 -0.04313218,  0.09863346, -0.02060572, -0.12749603, -0.2912513 ,  0.14109921,
	# 	  0.41023636, -0.17050795,  0.4088831,   0.1685237,   0.21752839,  0.13101783,
	# 	  0.7916676 ,  0.3092015,   0.20174792,  0.65444237, -0.32971415
	# 	]
	# W_o = [
	# 	  8.3404198e-02, -1.2754035e-01, -2.4177763e-01,  3.8428426e-01,
	# 	  8.1700611e-01,  4.0029794e-01, -1.9565052e-01, -6.8552971e-01,
	# 	  1.0533657e-01, -1.7581466e-01, -3.5612047e-01,  2.7427170e-02,
	# 	 -9.6097589e-01, -3.9907330e-01,  7.1056497e-01, -5.7348013e-01,
	# 	  4.8019081e-01,  8.5395539e-01, -4.1580009e-01, -7.6821351e-01,
	# 	  1.3025692e-01, -1.0922647e+00, -9.5981985e-01, -8.0812061e-01,
	# 	  7.0266539e-01, -8.3235823e-02,  4.7158763e-01, -5.4590219e-01,
	# 	 -3.3961323e-01,  3.9499290e-02, -2.8332293e-03, -2.1211502e-01,
	# 	 -4.5684519e-01,  3.4137819e-02,  3.4755953e-02, -2.1655875e-01,
	# 	 -5.2392870e-02, -8.8207245e-02,  5.3173876e-01, -1.5928257e-01,
	# 	  1.1840930e-01, -2.0541112e-01, -8.7140584e-01, -4.1719694e-02,
	# 	 -1.8674573e-01,  3.8948550e-04,  6.9030486e-02, -4.5726117e-02,
	# 	 -4.3736663e-01, -4.6797848e-01, -1.2074592e-01,  1.0034432e+00,
	# 	  6.0447294e-01
	# 	]
	# U_i = [
	# 	  0.00612837, -0.06935013, -0.0878988,  -0.04359174,  0.02487833, -0.19421126,
	# 	  0.04261507, -0.09764091, -0.00345173,  0.08588862, -0.12727292, -0.05583247,
	# 	  0.03921631,  0.10477229,  0.16228591, -0.02603376,  0.02931217,  0.06989836,
	# 	 -0.00646052, -0.042303,   -0.01439881,  0.16898845,  0.10458903, -0.00766414,
	# 	 -0.08396526, -0.0387619,   0.03919313,  0.00424006, -0.05676219, -0.00723992,
	# 	  0.06800182,  0.1116448,  -0.05724223,  0.01670931,  0.02495195,  0.03392423,
	# 	  0.02669317, -0.16750583,  0.06570495, -0.06535552, -0.01222422, -0.00697631,
	# 	 -0.00874833, -0.01940295,  0.01351569,  0.05088714, -0.00837928,  0.03933763,
	# 	 -0.05080327,  0.078325,   -0.09977635, -0.0184499 ,  0.09341519
	# 	]
	# U_f = [
	# 	 -0.06652573,  0.02222504, -0.09878703, -0.13093396,  0.07408568,  0.10827209,
	# 	 -0.12557343, -0.11533146,  0.06227909,  0.07678092,  0.03791051, -0.01473946,
	# 	  0.06424088, -0.03324877, -0.00272741,  0.13595124, -0.00815166, -0.01418081,
	# 	  0.10180148,  0.02745712, -0.04313579,  0.07023194,  0.07751412, -0.04125224,
	# 	 -0.04358647, -0.04377162, -0.01994726,  0.03162838, -0.01847541, -0.02019647,
	# 	 -0.01328689,  0.02600278, -0.06669875, -0.002402,    0.03299932,  0.02539235,
	# 	 -0.04620105, -0.01264985, -0.04296141, -0.21376249, -0.00205263,  0.00639245,
	# 	 -0.00272425, -0.06243756, -0.02721209,  0.04106709,  0.0114681,   0.04771544,
	# 	 -0.15204887, -0.03831339, -0.01922275,  0.03173603, -0.03196539
	# 	]
	# U_a = [
	# 	  0.1484712,  -0.02544265, -0.2796158 , -0.12998487, -0.28855258, -0.35916904,
	# 	  0.01629824,  0.12893869,  0.02764273,  0.40544397, -0.01477846, -0.0867673,
	# 	 -0.02035528, -0.15837644, -0.01207534,  0.12488455,  0.3339465 , -0.0517404,
	# 	  0.03828485, -0.15318862,  0.09420725,  0.16289948,  0.36654225, -0.08718687,
	# 	  0.09414774, -0.03180505, -0.01704958, -0.41202593,  0.24092418,  0.23186664,
	# 	 -0.2536683,   0.14906622, -0.2033019 , -0.43956655, -0.22768654, -0.01514669,
	# 	  0.08802595,  0.05998521,  0.09086794,  0.3142056,   0.27961445,  0.07009967,
	# 	  0.11627257,  0.14767633,  0.13528752, -0.02057074,  0.3823129 ,  0.09804386,
	# 	  0.04189064, -0.02600301, -0.07167131, -0.07320925,  0.14483167
	# 	]
	# U_o = [
	# 	 -1.83168411e-01,  7.37959445e-02,  3.96745652e-03,  1.24403834e-01,
	# 	 -9.51168942e-04,  5.80449641e-01, -1.01919509e-01, -7.33455345e-02,
	# 	  2.22073472e-03, -2.09962294e-01, -1.72322482e-01,  4.03689861e-01,
	# 	 -3.27028818e-02, -1.19785242e-01,  9.10888910e-02, -3.62890065e-01,
	# 	 -5.91351032e-01, -4.70286235e-03,  2.05623299e-01,  3.73894960e-01,
	# 	 -2.21290335e-01,  3.13073337e-01, -2.71262258e-01, -1.47505835e-01,
	# 	 -6.93263113e-02,  5.96887320e-02,  3.91854554e-01, -2.89888054e-01,
	# 	 -2.22968906e-01,  2.83690542e-02,  2.11198196e-01,  2.73795545e-01,
	# 	 -5.50764203e-02, -2.26557896e-01, -1.46600530e-02, -4.14292403e-02,
	# 	 -3.82001579e-01, -4.31837849e-02, -1.26713693e-01, -5.53881824e-01,
	# 	  1.06966710e+00, -1.30313039e-02, -5.42143174e-02,  3.31140339e-01,
	# 	  6.74837083e-02,  2.35681966e-01,  1.22195102e-01,  1.82028010e-01,
	# 	  6.75570220e-02, -7.56925195e-02, -1.71729196e-02,  4.56986576e-01,
	# 	  3.92247513e-02
	# 	]
	# B_i = [0.002653873]
	# B_f = [1.0035063]
	# B_a = [0.04432528]
	# B_o = [-0.003412661]

	# cell 48
	# W_i = [
	#   3.06299031e-01,  8.06680880e-04, -1.42520592e-01, -2.22960070e-01,
	#  -1.37087750e+00, -4.26641852e-02,  1.92917269e-02, -9.14699018e-01,
	#   7.12792218e-01,  3.50553811e-01, -1.75186232e-01, -9.27801907e-01,
	#  -7.01319873e-01, -1.06744015e+00,  5.45748413e-01,  1.25230670e-01,
	#   2.03930587e-01,  2.46292967e-02,  3.65605623e-01, -4.04319495e-01,
	#  -1.17422596e-01, -1.58343807e-01, -7.78792262e-01, -1.44536495e-01,
	#  -3.83916050e-01,  2.48676598e-01,  1.29967883e-01,  1.88454717e-01,
	#   3.20211440e-01,  2.13640153e-01,  3.30361128e-01,  3.34967881e-01,
	#  -3.07165533e-02,  2.49579877e-01,  9.68283340e-02, -5.60692213e-02,
	#  -1.64800301e-01,  2.43915111e-01,  6.30728900e-02, -3.49326223e-01,
	#  -2.47344762e-01,  2.22460166e-01, -1.31024793e-01, -1.67000026e-01,
	#  -7.50366807e-01,  2.58115113e-01,  3.96797538e-01, -7.14382231e-02,
	#  -2.63259858e-01,  6.30277991e-01, -3.83352414e-02, -5.71157217e-01,
	#   5.27955055e-01
	# ]
	# W_f = [
	#   0.865695,    0.01799434, -0.2660277,   0.13889416,  0.5399493,   0.22476572,
	#   0.9229715,   0.8289297,   0.21388543,  0.19471139, -0.11136107,  0.24622679,
	#  -0.3215845,  -0.4305918,   0.1800795,   0.20185727, -0.14581795, -0.15010132,
	#   0.16612025, -0.16523594,  0.2647341,  -0.53103,    -0.25842488,  0.22281986,
	#  -0.14687209, -0.33166727,  0.41821417,  0.8265414,   0.03378696, -0.6494265,
	#  -0.08278668,  0.04916333,  0.03239656,  0.4219137,  -0.0110266,  -0.48982283,
	#   0.17565396, -0.20883471,  0.23534249, -0.3184359,   0.13223033,  0.12197959,
	#   0.6977227,   0.10129695, -0.4890279,   0.41308317,  0.2197327,   1.7523687,
	#   0.45193398, -0.35946745, -0.13801254, -0.74095905,  0.12129659
	# ]
	# W_a = [
	#  -0.59529287,  0.09713385,  0.353829,   -0.43389136, -0.02179679, -0.11239529,
	#  -0.14644825, -0.6627281,  -0.37997198,  0.31286645,  0.01345805,  0.00528577,
	#   0.4055027,  -0.3279488,  -0.18841507,  0.1367811,  -0.10276942,  0.07660933,
	#   0.07821221, -0.06502566, -0.46762234,  1.360238,    0.4127453,   0.09157871,
	#   0.7564619,   0.04279173, -0.43493,    -0.42395407,  0.23998404,  0.17299333,
	#   0.40130633, -0.10843722, -0.04903012,  0.12893067,  0.05179751,  0.5621182,
	#   0.15550777,  0.47796673,  0.11033501,  0.3360256,   0.00509169, -0.03714962,
	#  -0.58245707,  0.07960191,  0.65078735, -0.30561957,  0.43093705, -0.05165024,
	#  -0.01777003,  0.29764172,  0.20348603, -0.23585999,  0.2666465, 
	# ]
	# W_o = [
	#   0.04624243, -0.13449536, -0.14168182,  0.02511223,  0.06983857,  0.06527125,
	#  -0.00550922, -0.08579773, -0.13119793, -0.12427814, -0.08523023,  0.01058258,
	#  -0.07454379,  0.07317269, -0.07735509,  0.07474446,  0.05896213,  0.06676739,
	#  -0.0282021,   0.08423667,  0.09256138, -0.00571475, -0.03588016,  0.01894058,
	#   0.06453127, -0.10466355, -0.08175871, -0.01653559, -0.00034938,  0.01702518,
	#   0.11690358,  0.03960941,  0.07956978,  0.10096411, -0.08415184, -0.00348798,
	#   0.08281434,  0.14904246, -0.02267797, -0.10100313,  0.14278732,  0.11215312,
	#   0.04304006, -0.03174358, -0.02064823, -0.02832556, -0.09070048,  0.01625178,
	#   0.01271882, -0.05932813,  0.14733922,  0.11663525, -0.08469249
	# ]
	# U_i = [
	#  -0.29322132, -0.27346724,  0.22480385, -0.16412966, -0.4266484,  -0.08114491,
	#   0.11022406, -0.09302744,  0.01405009, -0.02707016, -0.28997144,  0.25192776,
	#  -0.02190578,  0.10683684, -0.09851,    -0.19592188, -1.0166941,   0.01871707,
	#  -0.0286086,   0.40567937, -0.99011886, -0.25739357, -0.53739774, -0.29476923,
	#   0.05613506,  0.07794223, -0.28578028,  0.39100143,  0.18825729,  0.21862864,
	#  -0.1928728,   0.11814664,  0.12818216, -0.03703472,  0.19602613, -0.11307251,
	#  -0.02425589,  0.27209947,  0.06488937,  0.0532201,   0.13496512, -0.08282304,
	#   0.07306835,  1.1803429,  -0.10700694,  0.15894485,  0.26278427, -0.59413004,
	#   0.01168957,  0.07377174,  0.04612763,  0.11372356,  0.24628143
	# ]
	# U_f = [
	#  -0.08351108,  0.19985506, -0.03667584,  0.00921194,  0.3208458,   0.24690406,
	#  -0.00267078,  0.8992802,  -0.0049813,  -0.23393276,  0.2964371,   0.33209524,
	#  -0.05584794, -0.0646481,   0.16538882, -0.1438168,  -0.5192386,  -0.06270757,
	#  -0.10725005, -0.027234,    0.33836862,  0.9902131,  -0.01834827, -0.00358191,
	#  -0.11975479, -0.01452423,  0.25770214,  0.1010732,   0.12686533, -0.47193053,
	#   0.32089773,  0.21607174,  0.24295244,  0.12629035, -0.17385854, -0.01793665,
	#  -0.09071663,  0.00333755,  0.31918755, -0.1570841,  -0.1108537,   0.00202239,
	#  -0.01719213,  0.01817184,  0.13309963, -0.08354507,  0.05802325,  0.165935,
	#  -0.0576022,   0.1697013,   0.03568245,  1.0099717,   0.12823416
	# ]
	# U_a = [
	#  -0.08294283,  0.07200451,  0.21075077, -0.0506181,   0.39873847,  0.22337095,
	#  -0.04733144,  0.16696885, -0.01582314,  0.01494245,  0.12618563, -0.0876353,
	#   0.01457065, -0.14786734,  0.06146546, -0.00772806, -0.20998152, -0.02612959,
	#   0.12034193,  0.30034918, -0.9007211,  -0.02128418, -0.21226224,  0.12775011,
	#  -0.01866305, -0.03626611,  0.09529518, -0.52499044, -0.17840356,  0.21625537,
	#  -0.34604716, -0.7403963,   0.14471823,  0.26400235, -0.04612842,  0.0565178,
	#   0.1848221,  -0.02392852, -0.32648653,  0.1520373,   0.6075076,  -0.07544951,
	#   0.02095437, -0.17365932, -0.051643,    0.03506663, -0.03954742,  0.29544377,
	#  -0.16314703,  0.02123047, -0.13000396, -0.37733293,  0.10237701
	# ]
	# U_o = [
	#  -0.02839377, -0.05701372, -0.01167165, -0.00658506, -0.08029788, -0.13884696,
	#   0.08715691, -0.02137773, -0.04393606,  0.03799721,  0.07452677, -0.01459021,
	#   0.05264317, -0.1668033,  -0.01024438,  0.01357399,  0.12114964,  0.00955314,
	#  -0.12844029, -0.04741636, -0.01994465,  0.01459712,  0.03213436,  0.11839335,
	#  -0.05676229, -0.04129412, -0.02540429,  0.01738912, -0.02966114,  0.14473216,
	#  -0.04898999, -0.09140359, -0.11129966,  0.03314012,  0.04021974,  0.05111075,
	#  -0.05069948,  0.03504401, -0.01834799,  0.05023393, -0.01002263, -0.05016592,
	#   0.04491122, -0.06794544, -0.01684049,  0.06440851, -0.11289305, -0.01327477,
	#   0.07581633,  0.02617683, -0.04304627,  0.05252657,  0.02826778
	# ]
	# B_i = [-0.034355663]
	# B_f = [1.0516121]
	# B_a = [0.024488833]
	# B_o = [0.008139851]


	# cell 49
	# W_i = [
	#  -0.10657662,  0.13034658,  0.0831341,   0.13266097,  0.14024575, -0.14500995,
	#  -0.09374981,  0.14963244, -0.00379027, -0.09476121,  0.06084201,  0.13659765,
	#   0.03845352, -0.00250508, -0.03121401, -0.07786706, -0.12612681,  0.07966562,
	#   0.13652356,  0.10291673,  0.05326225,  0.10181426, -0.06372991,  0.04997253,
	#   0.04818746, -0.03529824, -0.01024316, -0.00748961,  0.00392258, -0.02735646,
	#  -0.11660557, -0.1219445,   0.06223105, -0.0785042,   0.03026865,  0.14850463,
	#   0.10094963, -0.11868708,  0.10182552, -0.06692473, -0.02329662,  0.00471936,
	#   0.07856275,  0.14829652, -0.14186227,  0.04211375, -0.13405047,  0.02476628,
	#   0.11135249, -0.059907,   -0.14475986,  0.13559763, -0.04127309
	# ]
	# W_f = [
	#  -7.25635067e-02, -1.05727822e-01, -5.77921942e-02, -1.38677314e-01,
	#   1.02127790e-02, -6.86688349e-02,  1.43135622e-01, -2.40794271e-02,
	#  -4.28401083e-02, -8.57772231e-02, -6.21434823e-02, -3.31501812e-02,
	#   6.67710751e-02,  9.22735184e-02,  3.62656116e-02, -8.39165971e-02,
	#  -1.43731102e-01, -1.00590363e-01, -1.28564522e-01,  1.77164376e-02,
	#   1.08536407e-01, -1.19273603e-01, -4.32840660e-02,  2.68732607e-02,
	#   4.62496430e-02,  1.24589637e-01, -4.42408547e-02, -9.82452482e-02,
	#  -1.70667768e-02,  4.44718897e-02,  2.93945968e-02,  1.24847442e-02,
	#  -1.35075599e-01, -1.00018479e-01, -1.30611882e-01,  1.10122219e-01,
	#   9.66862589e-02,  6.21921569e-02, -2.06569433e-02, -7.28084147e-03,
	#   7.80545026e-02,  9.96799320e-02,  1.35527596e-01,  8.77419263e-02,
	#  -6.71020225e-02,  6.23464584e-05,  1.37750074e-01, -1.13745928e-01,
	#   8.90487432e-02, -2.90490538e-02,  8.60238373e-02,  1.09871134e-01,
	#  -6.71998933e-02
	# ]
	# W_a = [
	#  -0.12529318, -0.14675531, -0.00845999, -0.12896435,  0.01337634, -0.05064972,
	#   0.07741769,  0.13318963, -0.0328173,   0.07204153, -0.07664505,  0.13964985,
	#   0.13053893, -0.06146257, -0.11854706, -0.05487196, -0.10163422, -0.12067646,
	#   0.01401061,  0.03151126, -0.05649624, -0.00384843,  0.0884914,   0.01598224,
	#  -0.11596226,  0.13986547,  0.11940561, -0.02502985,  0.00780405, -0.0676958,
	#   0.02970733,  0.12194286,  0.14118771, -0.02551399, -0.05559015, -0.02075969,
	#   0.12277837,  0.04569753, -0.04012695, -0.07210886, -0.05949784,  0.05875117,
	#   0.1473359,  -0.08857426,  0.1008736,   0.0893534,   0.12152122,  0.01855779,
	#  -0.12255721,  0.05777898,  0.10420682,  0.06125511,  0.09628783
	# ]
	# W_o = [
	#   0.04239863,  0.14337541, -0.11784936, -0.02403644, -0.04761361, -0.00474893,
	#   0.01625395, -0.13872069,  0.05590452,  0.12201725, -0.0449919,   0.09063442,
	#  -0.12403006,  0.10035513,  0.11577724,  0.06316933, -0.11144143,  0.07904868,
	#  -0.07277925,  0.0258923,   0.03798003,  0.07387161,  0.08962074,  0.04124095,
	#  -0.06257581, -0.0871728,   0.04679228, -0.1401784,   0.04975499,  0.08279644,
	#   0.13055451,  0.12505512, -0.07568399,  0.10046361, -0.02641779, -0.09390651,
	#   0.0249237,   0.06336069, -0.00378934,  0.07507935, -0.06557888, -0.13465989,
	#  -0.02643247, -0.02165832, -0.04284054, -0.13964006, -0.09817554, -0.09699354,
	#  -0.00211157,  0.13579626,  0.02562287, -0.1236533,  -0.04288567
	# ]
	# U_i = [
	#  -5.30613586e-02,  5.89341149e-02, -4.72738147e-02,  9.72500653e-04,
	#   1.08606286e-01,  7.57279620e-02, -4.63443436e-03, -4.34514433e-02,
	#   6.88894652e-03, -1.54631920e-02,  5.86157478e-02,  5.83289331e-03,
	#   3.82120302e-03, -3.04105226e-02, -1.12382978e-01,  2.70635001e-02,
	#   5.96317016e-02, -2.16948595e-02,  6.07485510e-02, -5.33274338e-02,
	#   6.98758140e-02, -8.23138058e-02, -1.30094111e-01, -1.68794319e-01,
	#   3.76298688e-02,  4.43440229e-02,  5.00800163e-02, -1.49024883e-03,
	#   1.14157550e-01,  9.28554963e-03,  6.51923567e-02,  3.29157896e-02,
	#  -3.44489738e-02,  1.02498025e-01, -4.16811556e-02, -6.15122654e-02,
	#   1.37869483e-02,  2.07011867e-02,  4.22913209e-02,  1.23240046e-01,
	#   4.09333482e-02,  5.95940728e-05,  1.02928229e-01, -1.14703916e-01,
	#   3.86547297e-02, -3.61498259e-02,  3.20555978e-02, -3.00995004e-03,
	#   2.57952102e-02,  5.50988540e-02, -9.82719660e-02, -1.24626863e-03,
	#   1.51130622e-02
	# ]
	# U_f = [
	#  -0.13049114, -0.07566038, -0.00977006, -0.07145136,  0.0692742,   0.06005816,
	#  -0.05294349,  0.04261602,  0.02365798,  0.01424062, -0.00399506,  0.10225983,
	#  -0.1263423,  -0.06690164, -0.13876005,  0.03617627, -0.06369183,  0.00358375,
	#  -0.00157037,  0.07492475, -0.01412926,  0.05155888,  0.03285778, -0.09761824,
	#  -0.01434497, -0.10983482,  0.06686269,  0.1284155,   0.01507814,  0.16958733,
	#   0.00820803,  0.04756442,  0.03795464, -0.02271678,  0.06718799,  0.07263979,
	#  -0.17351998,  0.01684649, -0.08463546, -0.06332654,  0.01687476, -0.0396934,
	#   0.08361503, -0.1121939,   0.07142319, -0.06918788,  0.04641758, -0.02158047,
	#  -0.06697768,  0.02577637, -0.02710943, -0.08466134,  0.12386038
	# ]
	# U_a = [
	#  -7.17028081e-02, -2.69823838e-02, -6.74794540e-02,  3.10760662e-02,
	#  -2.59471573e-02,  8.26353729e-02,  5.62734343e-02, -1.27815545e-01,
	#  -1.21271685e-01, -3.04389633e-02,  6.52749538e-02,  6.86531514e-02,
	#  -7.35788122e-02,  4.75833863e-02,  2.94705518e-02, -1.40323834e-02,
	#   1.15216911e-01,  7.45712370e-02, -2.29113065e-02,  1.16525836e-01,
	#  -3.00710909e-02, -4.06470671e-02,  3.07775121e-02, -3.49294469e-02,
	#  -3.46430987e-02, -7.28196392e-05, -6.16510399e-02,  4.37860563e-02,
	#  -7.49528263e-05, -5.73350452e-02, -8.32336023e-02,  1.11724347e-01,
	#  -1.06134608e-01,  5.18917339e-04, -7.04634041e-02,  2.42481418e-02,
	#  -1.01078220e-01,  1.14045158e-01, -2.27140449e-02,  1.99803580e-02,
	#   6.78257272e-02, -3.51439230e-02,  9.51571241e-02,  8.69042799e-03,
	#   5.26501872e-02, -5.75658828e-02, -3.31189744e-02, -2.78288834e-02,
	#   3.71800363e-02, -1.02472618e-01,  6.95290267e-02,  1.04992710e-01,
	#   2.84613948e-02
	# ]
	# U_o = [
	#  -0.03319762, -0.05648485,  0.01912127,  0.07511327, -0.0396357,   0.05645681,
	#   0.04962103, -0.00258964,  0.02338454,  0.07176874,  0.04393255,  0.04026592,
	#   0.00786126,  0.06996714,  0.04541215,  0.14857699,  0.12215824, -0.08778828,
	#  -0.06101407,  0.08689421, -0.00350063,  0.1020112,  -0.13282295,  0.06344593,
	#   0.00478396, -0.12916718,  0.12273891,  0.01378745,  0.0911266,   0.03346447,
	#  -0.05557664, -0.10093813,  0.12456027,  0.06870485,  0.1360795,  -0.12389162,
	#   0.01279434,  0.1140676,   0.06155659, -0.01209024,  0.04040131,  0.05265643,
	#  -0.00863248,  0.00328132,  0.04453625, -0.02176528,  0.00333556,  0.00246747,
	#  -0.00937696,  0.00722148, -0.04566098,  0.049538,    0.05833744
	# ]
	# B_i = [0.0] 
	# B_f = [1.0] 
	# B_a = [0.0] 
	# B_o = [0.0] 

	from numpy import genfromtxt
	
	W_a = genfromtxt('Forward_Simul2\\sigmoidTrained2\\wa', delimiter=',')
	W_i = genfromtxt('Forward_Simul2\\sigmoidTrained2\\wi', delimiter=',')
	W_f = genfromtxt('Forward_Simul2\\sigmoidTrained2\\wf', delimiter=',')
	W_o = genfromtxt('Forward_Simul2\\sigmoidTrained2\\wo', delimiter=',')
	U_a = genfromtxt('Forward_Simul2\\sigmoidTrained2\\ua', delimiter=',')
	U_i = genfromtxt('Forward_Simul2\\sigmoidTrained2\\ui', delimiter=',')
	U_f = genfromtxt('Forward_Simul2\\sigmoidTrained2\\uf', delimiter=',')
	U_o = genfromtxt('Forward_Simul2\\sigmoidTrained2\\uo', delimiter=',')
	B_a = genfromtxt('Forward_Simul2\\sigmoidTrained2\\ba', delimiter=',')
	B_i = genfromtxt('Forward_Simul2\\sigmoidTrained2\\bi', delimiter=',')
	B_f = genfromtxt('Forward_Simul2\\sigmoidTrained2\\bf', delimiter=',')
	B_o = genfromtxt('Forward_Simul2\\sigmoidTrained2\\bo', delimiter=',')

	WA = []
	WI = []
	WF = []
	WO = []

	for i in range(0,53):
		Temp_A = np.array([])
		Temp_A = np.append(U_a[:,i],W_a[:,i])
		Temp_A = np.append(Temp_A, B_a[i])
		WA.append(Temp_A)

		Temp_I = np.array([])
		Temp_I = np.append(U_i[:,i],W_i[:,i])
		Temp_I = np.append(Temp_I, B_i[i])
		WI.append(Temp_I)

		Temp_F = np.array([])
		Temp_F = np.append(U_f[:,i],W_f[:,i])
		Temp_F = np.append(Temp_F, B_f[i])
		WF.append(Temp_F)

		Temp_O = np.array([])
		Temp_O = np.append(U_o[:,i],W_o[:,i])
		Temp_O = np.append(Temp_O, B_o[i])
		WO.append(Temp_O)


	
	W = np.array([WA, WI, WF, WO])
	prev_h = np.zeros(53)
	prev_c = np.zeros(53)

	# X = [ 4.98186240e-03, -2.71241786e+01,  1.01456744e+00,  7.69437272e-01,
	# 	  -6.76223812e-01, -6.52513496e-01,  2.94067849e-01, -3.22239621e-01,
	# 	  -9.90899889e-02, -4.53458888e-01, -2.48639283e-01, -3.07830844e-01,
	# 	  -2.60279212e-01, -3.41419377e-02,  1.37322772e-02,  3.22253257e-03,
	# 	   1.75387744e-02,  2.26283855e-02,  1.37637502e-02,  1.29960036e-02,
	# 	   3.49572363e-02,  6.27400390e-03,  8.86102218e-03,  7.88909750e-03,
	# 	   6.90721661e-03,  4.07418263e-03,  1.74928409e-02,  6.29680864e-03,
	# 	   2.15863162e+00,  7.08103792e-01,  1.51156633e+00,  6.44029103e-01,
	# 	   4.49640168e-01,  3.04037669e-01,  4.79631543e-01,  4.08864068e-01,
	# 	   3.14478513e-01,  2.89509468e-01,  3.41910933e-01,  3.57950716e-01,
	# 	   2.43869852e-01,  2.06210000e+00, -2.51730000e-01,  6.07590000e-01,
	# 	   3.23890000e-01,  3.08450000e-01, -1.57200000e-02,  1.72820000e-02,
	# 	  -1.52810000e-01, -1.52120000e-01, -5.33240000e-02, -1.46180000e-01,
	# 	  -4.50820000e-03]

	X = np.array([
	 [ 4.98186240e-03, -2.71241786e+01,  1.01456744e+00,  7.69437272e-01,
	  -6.76223812e-01, -6.52513496e-01,  2.94067849e-01, -3.22239621e-01,
	  -9.90899889e-02, -4.53458888e-01, -2.48639283e-01, -3.07830844e-01,
	  -2.60279212e-01, -3.41419377e-02,  1.37322772e-02,  3.22253257e-03,
	   1.75387744e-02,  2.26283855e-02,  1.37637502e-02,  1.29960036e-02,
	   3.49572363e-02,  6.27400390e-03,  8.86102218e-03,  7.88909750e-03,
	   6.90721661e-03,  4.07418263e-03,  1.74928409e-02,  6.29680864e-03,
	   2.15863162e+00,  7.08103792e-01,  1.51156633e+00,  6.44029103e-01,
	   4.49640168e-01,  3.04037669e-01,  4.79631543e-01,  4.08864068e-01,
	   3.14478513e-01,  2.89509468e-01,  3.41910933e-01,  3.57950716e-01,
	   2.43869852e-01,  2.06210000e+00, -2.51730000e-01,  6.07590000e-01,
	   3.23890000e-01,  3.08450000e-01, -1.57200000e-02,  1.72820000e-02,
	  -1.52810000e-01, -1.52120000e-01, -5.33240000e-02, -1.46180000e-01,
	  -4.50820000e-03],
	 [ 8.38112874e-03, -2.67512872e+01,  8.08911274e-01, -5.06501509e-01,
	  -7.59941523e-02, -2.58356534e-01,  4.29430569e-02, -6.72176233e-02,
	  -4.31205329e-01, -3.94900253e-01, -2.28420927e-01, -9.29092247e-02,
	  -1.33578216e-01, -3.65539136e-02,  8.94715069e-03,  2.86350665e-03,
	   2.10568550e-02,  1.48515596e-02,  9.89731472e-03,  9.45964499e-03,
	   3.04508942e-02,  9.36669516e-03,  1.19050992e-02,  1.21867461e-02,
	   1.15646837e-02,  3.89221448e-03,  1.67891457e-02,  1.56777953e-02,
	   2.51801388e+00,  9.42145069e-01,  1.01820220e+00,  6.14704467e-01,
	   6.96422313e-01,  5.28430649e-01,  3.92255271e-01,  2.74482461e-01,
	   3.50855173e-01,  2.53025919e-01,  3.78733294e-01,  3.95568310e-01,
	   1.38176147e-01,  2.16580000e+00,  6.10030000e-02,  5.11460000e-01,
	   1.96250000e-02,  3.11630000e-01,  3.86420000e-02,  6.60140000e-02,
	  -1.31450000e-05,  9.89870000e-02,  1.24490000e-01, -9.68100000e-02,
	   1.38670000e-02],
	 [ 7.73659359e-03, -2.74957997e+01,  7.85817379e-01,  1.60018540e-01,
	  -9.24266423e-02, -1.03431637e-01, -1.82800903e-01, -3.12516141e-01,
	  -2.00439130e-01, -3.52201766e-01, -1.32873824e-01, -1.60978418e-01,
	  -8.54076611e-02, -1.44590807e-01,  2.64284101e-02,  3.02531293e-03,
	   2.56843104e-02,  1.08408835e-02,  1.14048602e-02,  8.25559952e-03,
	   4.71825743e-02,  4.74989463e-03,  6.57697693e-03,  6.58490687e-03,
	   1.40461347e-02,  7.84096312e-03,  2.41876787e-02,  1.58748013e-02,
	   2.48391767e+00,  9.24752447e-01,  1.23204814e+00,  6.50580761e-01,
	   6.27206350e-01,  5.22105683e-01,  3.94521382e-01,  3.36194917e-01,
	   3.73969092e-01,  3.03831488e-01,  3.58026377e-01,  4.49007814e-01,
	   3.19004686e-01,  2.14200000e+00,  5.25060000e-02,  6.97750000e-01,
	   1.11090000e-01,  3.39190000e-01,  2.68380000e-02, -5.25840000e-02,
	  -2.26450000e-01, -6.59900000e-02,  8.82370000e-02,  6.93970000e-03,
	   1.69080000e-01],
	 [ 3.71750291e-03, -2.70048041e+01,  8.78431561e-01,  2.97907934e-01,
	  -3.25292353e-01, -2.36258843e-01,  1.31140243e-01, -3.96237598e-01,
	  -1.09554138e-03, -2.37802942e-01, -4.86930217e-02, -3.14338964e-01,
	  -3.42869332e-01, -3.43615436e-01,  3.17297975e-02,  2.90838497e-03,
	   1.56625805e-02,  1.11182331e-02,  1.23710713e-02,  7.20359252e-03,
	   2.91236458e-02,  4.06552722e-03,  8.56926915e-03,  6.58523070e-03,
	   2.86131785e-02,  1.25450742e-02,  2.14529870e-02,  4.46557531e-03,
	   2.18388141e+00,  9.53159712e-01,  1.12010166e+00,  4.33326755e-01,
	   6.18965888e-01,  5.53646561e-01,  3.09893701e-01,  2.67102051e-01,
	   3.96091523e-01,  3.02226327e-01,  2.25135465e-01,  4.20075727e-01,
	   2.87014638e-01,  2.14380000e+00,  2.69120000e-01,  9.12760000e-01,
	   3.72680000e-01,  2.91760000e-01, -5.02060000e-02,  7.16650000e-03,
	  -9.33230000e-02, -2.58840000e-02, -5.42460000e-02, -9.60580000e-02,
	   9.38720000e-02],
	 [ 6.25000076e-03, -2.64300706e+01,  1.38867857e+00, -1.03262611e-01,
	  -5.48121299e-01, -1.77409839e-01,  3.69462884e-01, -9.99639221e-02,
	   4.20012633e-02, -7.34468851e-02, -9.96509098e-02, -2.99163706e-01,
	  -4.10253195e-01, -3.34401270e-01,  1.19982512e-02,  6.56502610e-03,
	   2.56180297e-02,  2.20746440e-02,  9.74981210e-03,  4.14367292e-03,
	   2.86160406e-02,  4.55559206e-03,  8.35397380e-03,  1.73553597e-02,
	   2.91241617e-02,  8.89969548e-03,  2.00736624e-02,  5.80713823e-03,
	   2.33963690e+00,  1.15362032e+00,  9.40019567e-01,  5.44445876e-01,
	   6.11528434e-01,  3.99005879e-01,  3.09518786e-01,  2.89964010e-01,
	   3.50097487e-01,  2.39043754e-01,  2.48697638e-01,  4.21468813e-01,
	   2.46985389e-01,  2.19370000e+00,  3.51150000e-01,  7.49190000e-01,
	   2.51240000e-01,  3.60000000e-01,  2.67590000e-02, -3.40370000e-03,
	  -1.98300000e-01, -5.44880000e-02, -8.90920000e-03, -9.56500000e-02,
	   5.27930000e-02],
	 [ 3.66468725e-03, -2.93246476e+01,  2.30230472e+00, -3.17868041e-01,
	  -4.43178578e-01,  4.64146786e-02,  3.20639479e-01,  1.57395905e-01,
	   6.54532918e-02, -2.34215655e-02, -3.36023030e-01, -2.20045188e-01,
	  -1.53343871e-01, -2.02344743e-01,  7.34110472e-03,  6.44647110e-03,
	   2.72752945e-02,  2.84160219e-02,  1.19431615e-02,  8.42367306e-03,
	   7.83219597e-02,  4.16419044e-03,  4.12196573e-03,  1.56486728e-02,
	   1.37555630e-02,  4.16109488e-03,  2.87179153e-02,  5.32766794e-03,
	   3.95593001e+00,  4.45388863e-01,  8.34949144e-01,  9.63104192e-01,
	   4.81175976e-01,  2.73343578e-01,  2.48800456e-01,  2.59937101e-01,
	   2.69858298e-01,  2.86717674e-01,  3.29304976e-01,  4.29338946e-01,
	   2.74149758e-01,  2.36030000e+00,  1.39840000e-01,  5.65970000e-01,
	   1.73970000e-01,  5.29450000e-01,  6.87940000e-02,  7.58100000e-02,
	  -2.29800000e-02,  6.10040000e-02,  8.28230000e-03,  2.65340000e-02,
	   3.95810000e-01],
	 [ 5.76009152e-04, -3.38723786e+01,  2.46190614e+00, -2.85399794e-01,
	   8.18886899e-02,  2.74668157e-01,  2.82101872e-01,  1.87713643e-01,
	   6.36988040e-02,  7.89053163e-03, -2.98005341e-01, -2.97763668e-02,
	   6.68140413e-02, -7.18728987e-02,  3.89313568e-03,  2.31686586e-03,
	   3.04517877e-02,  1.13558479e-02,  7.07298712e-03,  7.76099435e-03,
	   1.47563548e-01,  3.83460297e-03,  2.90653355e-03,  5.13292286e-03,
	   9.89114901e-03,  2.19094162e-03,  4.22487125e-02,  1.19266255e-03,
	   4.56326901e+00,  2.81649097e-01,  5.79873696e-01,  9.55312139e-01,
	   2.79099563e-01,  1.75953574e-01,  1.74344730e-01,  1.83475183e-01,
	   1.43108564e-01,  3.09057636e-01,  2.25541578e-01,  1.53666272e-01,
	   1.76146680e-01,  1.99410000e+00,  3.27760000e-01,  5.12870000e-01,
	   4.53330000e-01,  3.26360000e-01,  2.22200000e-01,  1.49450000e-01,
	  -1.48670000e-01, -7.71890000e-03,  1.07360000e-01,  2.18720000e-01,
	   1.60110000e-01]
	 ])

	# print(X.shape)

	for j,item in enumerate(X):
		H = []
		C = []
		for i in range(0,53):
			h, c = cell(W[:,i], item, prev_h, prev_c[i])
			H.append(h)
			C.append(c)
		prev_h = H
		prev_c = C

		print("input:",j)
		for i in range(0,46,5):
			print(H[i],H[i+1],H[i+2],H[i+3],H[i+4])
		print(H[50],H[51],H[52])