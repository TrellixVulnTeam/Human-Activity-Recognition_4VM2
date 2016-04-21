import numpy as np

print "SHUFFLING"
length_of_shuffling = [48, 104, 212, 56, 32, 108, 28, 80, 48, 32, 52, 44, 32, 40, 36, 16, 68, 60, 152, 140, 224, 84, 40, 132, 180, 108, 84, 36, 100, 136, 144, 84, 96, 76, 80, 204, 260, 160, 68, 48, 200, 188, 132, 84, 120, 176, 124, 128, 64, 296, 144, 112, 180, 84, 180, 120, 68, 172, 152, 144, 120, 76, 192, 124, 188, 64, 72, 88, 84, 84, 80, 72, 60, 40, 80, 60, 28, 160, 168, 168, 60, 48, 208, 48, 9376, 12304, 560, 160, 96, 16, 152, 44, 236, 644, 352, 420, 76, 220, 44, 68, 220, 24, 208, 468, 276, 300, 264, 116, 304, 156, 52, 28, 120, 48, 52, 380, 76, 52, 208, 144, 176, 156, 28, 48, 308, 140, 224, 32, 148, 4, 8, 40, 68, 64, 52, 140, 144, 40, 72, 180, 8, 68, 116, 164, 84, 112, 144, 20, 12, 156, 12, 152, 16, 8, 52, 76, 64, 40, 12, 12, 16, 108, 96, 92, 108, 204, 444, 32, 144, 96, 104, 116, 24, 168, 12, 12, 4, 388, 336, 104, 64, 200, 136, 156, 20, 32, 16, 36, 8, 112, 128, 124, 168, 92, 212, 24, 132, 128, 140, 24, 64, 192, 160, 196, 288, 40, 100, 92, 36, 32, 176, 588, 56, 56, 44, 44, 116, 264, 180, 156, 28, 44, 140, 48, 28, 484, 20, 356, 52, 32, 24, 120, 44, 104, 244, 124, 200, 48, 188, 24, 24, 48, 44, 60, 32, 28, 360, 248, 632, 152, 92, 72, 84, 68, 24, 16, 36, 188, 196, 56, 28, 432, 36, 32, 16, 40, 140, 44, 60, 84, 104, 248, 24, 44, 68, 112, 104, 68, 60, 156, 24, 60, 164, 436, 24, 40, 36, 48, 32, 44, 24, 8, 56, 128, 136, 112, 48, 128, 140, 116, 56, 16, 32, 72, 72, 804, 56, 380, 96, 116, 60, 196, 44, 48, 60, 80, 104, 32, 48, 136, 36, 108, 152, 220, 128, 128, 48, 60, 52, 52, 40, 96, 56, 204, 332, 156, 236, 40, 100, 40, 208, 48, 124, 104, 68, 48, 308, 20, 28, 312, 160, 60, 20, 192, 168, 48, 140, 100, 24, 148, 264, 144, 124, 148, 44, 92, 52, 60, 104, 60, 92, 76, 108, 152, 112, 48, 144, 28, 24, 92, 164, 244, 44, 56, 8, 12, 56, 236, 108, 16, 52, 80, 40, 80, 56, 20, 96, 160, 36, 224, 16, 56, 240, 92, 244, 228, 56, 88, 100, 56, 196, 132, 52, 144, 120, 12, 100, 184, 136, 140, 60, 56, 108, 56, 12, 60, 140, 264, 84, 12, 56, 20, 20, 80, 88, 656, 244, 112, 60, 156, 348, 28, 108, 68, 144, 220, 56, 64, 184, 72, 48, 64, 64, 76, 116, 76, 100, 72, 232, 444, 404, 188, 372, 164, 24, 316, 544, 184, 256, 296, 48, 64, 28, 264, 60, 152, 56, 220, 228, 152, 216, 136, 128, 76, 156, 36, 296, 52, 152, 168, 212, 28, 92, 300, 96, 208, 16, 136, 68, 92, 16, 48, 100, 124, 64, 192, 104, 80, 84, 56, 28, 96, 84, 40, 104, 412, 44, 44, 172, 92, 28, 20, 128, 40, 24, 48, 160, 28, 164, 136, 212, 208, 172, 156, 20, 84, 24, 40, 100, 116, 316, 216, 84, 172, 252, 84, 256, 248, 132, 232, 152, 56, 16, 16, 80, 32, 56, 236, 52, 108, 152, 84, 120, 36, 52, 320, 136, 44, 40, 40, 40, 56, 448, 364, 84, 16, 44, 48, 24, 36, 128, 112, 244, 432, 108, 32, 48, 60, 136, 60, 84, 208, 292, 176, 92, 400, 124, 144, 3068, 76, 120, 40, 296, 188, 88, 12, 40, 68, 104, 112, 140, 12, 48, 28, 40, 52, 12, 4, 12, 140, 16, 28, 36, 40, 340, 24, 20, 32, 32, 24, 16, 68, 72, 44, 240, 36, 144, 8, 120, 144, 64, 4, 16, 208, 40, 40, 20, 188, 36, 128, 92, 168, 152, 168, 124, 188, 128, 84, 48, 40, 204, 80, 100, 96, 56, 28, 68, 12, 132, 44, 220, 296, 256, 248, 148, 92, 76, 192, 52, 140, 176, 76, 96, 72, 76, 80, 72, 88, 76, 84, 156, 2356, 68, 64, 40, 28, 16, 24, 144, 72, 284, 68, 76, 660, 48, 236, 528, 456, 28, 84, 112, 740, 48, 84, 168, 56, 128, 212, 48, 88, 60, 36, 20, 28, 72, 152, 40, 124, 40, 112, 32, 164, 52, 24, 132, 24, 28, 56, 144, 144, 192, 48, 144, 44, 112, 44, 344, 36, 48, 80, 156, 112, 108, 80, 56, 260, 104, 24, 104, 100, 56, 24, 172, 208, 100, 168, 172, 96, 228, 112, 124, 108, 76, 164, 204, 60, 208, 204, 16, 64, 36, 100, 44, 100, 36, 248, 176, 36, 144, 140, 44, 144, 104, 72, 188, 276, 340, 28, 24, 36, 92, 56, 52, 32, 32, 12, 28, 104, 32, 72, 44, 48, 92, 80, 40, 20, 108, 96, 52, 40, 84, 104, 64, 68, 68, 36, 20, 152, 24, 28, 68, 12, 48, 40, 52, 28, 68, 56, 32, 44, 32, 104, 20, 60, 24, 84, 32, 88, 48, 60, 692, 32, 492, 44, 76, 80, 84, 72, 72, 80, 80, 72, 92, 40, 28, 180, 24, 48, 88, 60, 72, 36, 48, 52, 152, 440, 24, 112, 32, 164, 176, 144, 308, 52, 24, 248, 116, 56, 28, 32, 16, 72, 104, 8, 52, 48, 120, 40, 88, 324, 56, 28, 132, 128, 28, 52, 196, 264, 136, 128, 228, 28, 232, 308, 284, 144, 164, 24, 192, 148, 184, 192, 172, 60, 248, 148, 72, 224, 164, 232, 196, 192, 244, 80, 120, 124, 108, 112, 312, 120, 176, 148, 16, 200, 32, 592, 64, 304, 132, 108, 228, 260, 64, 64, 80, 112, 84, 136, 152, 52, 56, 124, 144, 328, 128, 92, 84, 40, 160, 36, 20, 172, 24, 156, 64, 40, 68, 112, 84, 40, 44, 132, 32, 124, 48, 32, 152, 28, 248, 180, 84, 68, 116, 144, 140, 88, 40, 52, 28, 160, 64, 32, 76, 40, 52, 180, 148, 48, 40, 120, 116, 376, 168, 168, 56, 48, 152, 48, 68, 72, 352, 88, 56, 296, 96, 40, 60, 44, 136, 728, 16, 48, 52, 20, 40, 156, 264, 92, 248, 36, 180, 60, 444, 100, 116, 52, 28, 216, 64, 60, 160, 44, 100, 176, 216, 136, 292, 44, 12, 116, 60, 120, 148, 100, 48, 24, 112, 128, 112, 108, 148, 124, 136, 156, 140, 72, 128, 84, 164, 152, 136, 68, 152, 152, 140, 132, 68, 112, 96, 100, 192, 420, 80]

print 'Mean',np.mean(length_of_shuffling)
print 'Median', np.median(length_of_shuffling)
print 'STD', np.std(length_of_shuffling)

over_3 = 0
for i in length_of_shuffling:
	if i > 400:
		over_3 += 1.0

print over_3 / len(length_of_shuffling)
print len(length_of_shuffling)

print "WALKING"
length_of_walking = [252, 240, 264, 256, 256, 260, 376, 272, 292, 276, 160, 280, 924, 1508, 1532, 452, 284, 3204, 328, 1084, 404, 216, 128, 88, 128, 128, 112, 156, 112, 116, 396, 456, 424, 608, 30784, 3644, 5184, 460, 1092, 252, 156, 128, 124, 240, 952, 344, 280, 252, 300, 3328, 1488, 1368, 1664, 320, 748, 220, 1260, 268, 1108, 260, 464, 324, 492, 160, 1384, 228, 252, 284, 208, 1436, 1672, 440, 212, 188, 132, 176, 216, 172, 208, 200, 240, 288, 288, 244, 300, 192, 176, 984, 1444, 1448, 392, 256, 280, 3560, 1628, 388, 224, 100, 216, 128, 116, 88, 124, 108, 96, 248, 336, 308, 456, 244, 33272, 3708, 3992, 560, 340, 568, 128, 168, 172, 1036, 1148, 1768, 288, 560, 288, 236, 260, 464, 140, 652, 1452, 300, 1476, 280, 3216, 740, 324, 692, 336, 772, 512, 1712, 736, 676, 1724, 556, 316, 248, 116, 128, 120, 124, 128, 240, 948, 300, 844, 412, 104, 100, 188, 84, 100, 352, 160, 424, 1208, 628, 780, 1656, 516, 288, 164, 1040, 360, 1640, 1724, 420, 344, 464, 1196, 1984, 2308, 736, 656, 104, 316, 192, 592, 1752, 224, 208, 248, 172, 268, 280, 312, 164, 240, 236, 180, 368, 1100, 224, 1380, 1364, 428, 256, 192, 3576, 1272, 316, 164, 176, 148, 80, 120, 76, 112, 120, 344, 996, 472, 31204, 3508, 4140, 828, 352, 388, 200, 616, 292, 208, 368, 336, 180, 124, 132, 164, 796, 1100, 132, 1048, 928, 1112, 1244, 952, 224, 260, 164, 204, 292, 244, 364, 340, 236, 268, 100, 400, 1168, 360, 1588, 1632, 440, 460, 560, 5664, 764, 372, 248, 208, 168, 132, 200, 164, 152, 124, 164, 136, 132, 412, 400, 1152, 344, 372, 280, 41168, 3904, 2496, 304, 440, 1788, 248, 1192, 580, 2824, 2288, 23620, 112, 144, 1392, 176, 1700, 448, 360, 156, 68, 1112, 2652, 108, 3192, 3296, 120, 256, 1300, 1280, 180, 2236, 2128, 232, 224, 308, 152, 184, 240, 208, 208, 200, 208, 252, 236, 260, 564, 980, 1552, 1464, 480, 340, 3612, 220, 1484, 188, 164, 124, 148, 148, 120, 124, 108, 124, 120, 312, 428, 136, 484, 35596, 4492, 4948, 164, 532, 232, 308, 400, 136, 496, 200, 144, 124, 156, 248, 384, 128, 224, 196, 560, 260, 156, 144, 1364, 1680, 212, 444, 228, 676, 200, 208, 144, 164, 124, 164, 264, 292, 296, 280, 172, 1204, 1504, 1432, 516, 3992, 1284, 308, 448, 204, 124, 144, 128, 104, 124, 96, 112, 320, 1924, 36664, 3880, 3368, 212, 264, 528, 352, 260, 256, 120, 148, 140, 144, 176, 156, 224, 244, 396, 1116, 1872, 4160, 668, 304, 720, 252, 292, 692, 456, 224, 120, 152, 140, 152, 128, 116, 140, 172, 928, 304, 408, 204, 716, 204, 1296, 156, 212, 188, 244, 192, 204, 264, 148, 184, 140, 240, 164, 216, 232, 128, 236, 240, 1316, 1796, 1740, 444, 4156, 1600, 724, 120, 184, 144, 156, 108, 176, 120, 248, 564, 220, 768, 31864, 3816, 4556, 188, 352, 384, 280, 400, 276, 68, 128, 276, 1312, 440, 452, 388, 424, 224, 352, 608, 176, 200, 1248, 312, 264, 672, 320, 676, 592, 144, 176, 484, 268, 196, 804, 704, 252, 172, 556, 436, 2264, 124, 348, 992]

print 'Mean',np.mean(length_of_walking)
print 'Median', np.median(length_of_walking)
print 'STD', np.std(length_of_walking)

under_3 = 0
for i in length_of_walking:
	if i < 400:
		under_3 += 1.0

print 'Under',under_3 / len(length_of_walking)
print len(length_of_walking)


a = [True, True, False]

b = [False, True, True]

c = [False, True, False]
print a, b, c

print a and b and c