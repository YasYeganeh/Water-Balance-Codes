import glob
import netCDF4 as nc
# from netCDF4 import Dataset
import pandas as pd
import numpy as np
import xarray as xr
import shapefile
from shapely.geometry import Point, Polygon, shape
import re
import matplotlib.pyplot as plt


# basin = shapefile.Reader(r'F:/Masters/classes/Term2/HW/Hydrology/4/Arcmap/Basins/MazandaranSeaBasin.shp')
# shapes = basin.shapes()
# polygon = shape(shapes[0])
# df = pd.read_csv('GLDAS_NOAH025_M.A201110.021.nc4.SUB.nc4')
# Index=[]
# for index, row in df.iterrows():
#     # print(index)
#     lat = row["lat"]
#     lon = row["lon"]
#     point = Point(lon, lat)
#     if polygon.contains(point):
#         Index.append(index)
# print(Index)
# print(df)

# LISTE 'Index' khorooji in code az khate 13 ta 25 ast ke  tebghe shape file hoze, index pixelhayi az ncdf ke dakhele shapfile hoze mioftand ra estekhraj karde
Index=[17, 32, 33, 34, 35, 36, 51, 52, 53, 54, 55, 56, 70, 71, 72, 73, 74, 89, 90, 91, 92, 109, 110, 111, 127, 128, 129, 146, 147, 148, 166, 185, 186, 200, 204, 205, 211, 212, 213, 217, 218, 219, 222, 223, 224, 225, 231, 232, 235, 236, 237, 238, 241, 242, 243, 244, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 260, 261, 262, 263, 264, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 279, 280, 281, 282, 283, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 320, 321, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 344, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 363, 367, 368, 369, 370, 371, 372, 373, 386, 387, 388, 389, 404, 405, 406, 407, 408, 423, 424, 425, 426, 427, 443, 444, 445, 446, 462, 463, 464, 465, 480, 481, 482, 499, 500, 501, 517, 518, 519, 537, 538, 556, 557, 574, 575, 592, 593, 594, 611, 612, 613, 630, 631, 632, 633, 650, 651, 652, 669, 670, 671, 687, 688, 689, 690, 706, 707, 708, 709, 726, 727, 728, 746, 747, 766, 767, 768, 785, 786, 787, 804, 805, 806, 807, 824, 825, 826, 827, 843, 844, 845, 846, 847, 862, 863, 864, 865, 866, 882, 883, 884, 885, 901, 902, 903, 904, 921, 922, 923, 940, 941, 942, 943, 960, 961, 962, 979, 980, 981, 997, 998, 999, 1000, 1016, 1017, 1018, 1035, 1036, 1037, 1053, 1054, 1055, 1072, 1073, 1074, 1091, 1092, 1110, 1129, 1157, 1172, 1173, 1174, 1175, 1176, 1191, 1192, 1193, 1194, 1195, 1196, 1210, 1211, 1212, 1213, 1214, 1229, 1230, 1231, 1232, 1249, 1250, 1251, 1267, 1268, 1269, 1286, 1287, 1288, 1306, 1325, 1326, 1340, 1344, 1345, 1351, 1352, 1353, 1357, 1358, 1359, 1362, 1363, 1364, 1365, 1371, 1372, 1375, 1376, 1377, 1378, 1381, 1382, 1383, 1384, 1387, 1388, 1389, 1390, 1391, 1392, 1393, 1394, 1395, 1396, 1397, 1400, 1401, 1402, 1403, 1404, 1406, 1407, 1408, 1409, 1410, 1411, 1412, 1413, 1414, 1415, 1416, 1419, 1420, 1421, 1422, 1423, 1425, 1426, 1427, 1428, 1429, 1430, 1431, 1432, 1433, 1434, 1435, 1437, 1438, 1439, 1440, 1441, 1442, 1443, 1444, 1445, 1446, 1447, 1448, 1449, 1450, 1451, 1452, 1453, 1454, 1455, 1456, 1457, 1458, 1460, 1461, 1465, 1466, 1467, 1468, 1469, 1470, 1471, 1472, 1473, 1474, 1475, 1476, 1484, 1486, 1487, 1488, 1489, 1490, 1491, 1492, 1493, 1494, 1495, 1503, 1507, 1508, 1509, 1510, 1511, 1512, 1513, 1526, 1527, 1528, 1529, 1544, 1545, 1546, 1547, 1548, 1563, 1564, 1565, 1566, 1567, 1583, 1584, 1585, 1586, 1602, 1603, 1604, 1605, 1620, 1621, 1622, 1639, 1640, 1641, 1657, 1658, 1659, 1677, 1678, 1696, 1697, 1714, 1715, 1732, 1733, 1734, 1751, 1752, 1753, 1770, 1771, 1772, 1773, 1790, 1791, 1792, 1809, 1810, 1811, 1827, 1828, 1829, 1830, 1846, 1847, 1848, 1849, 1866, 1867, 1868, 1886, 1887, 1906, 1907, 1908, 1925, 1926, 1927, 1944, 1945, 1946, 1947, 1964, 1965, 1966, 1967, 1983, 1984, 1985, 1986, 1987, 2002, 2003, 2004, 2005, 2006, 2022, 2023, 2024, 2025, 2041, 2042, 2043, 2044, 2061, 2062, 2063, 2080, 2081, 2082, 2083, 2100, 2101, 2102, 2119, 2120, 2121, 2137, 2138, 2139, 2140, 2156, 2157, 2158, 2175, 2176, 2177, 2193, 2194, 2195, 2212, 2213, 2214, 2231, 2232, 2250, 2269]

###############################
# SERI ZAMANI MAHANE

for parameter in ['Rainf_f_tavg','Evap_tavg','Tair_f_inst']:
    Monthly_avg = []
    dates=[]
    for filename in glob.glob('*.nc4'):
        time = re.findall(".*_M.A(\d*)", filename)[0]
        year = time[:4]
        month = time[4:]
        # print(year, month)
        date = year + ' ' + month
        # print(date)
        dates.append(date)
        csv_name = filename[:-4] + ".csv"
        # ds = xr.open_dataset(filename).to_dataframe().to_csv(csv_name)  # tabdile ncdf be dataframe va csv
        df = pd.read_csv(csv_name)
        df = df[df.index.isin(Index)]
        Monthly_avg.append(df[parameter].mean())
        if parameter=='Rainf_f_tavg':
            monthly_avg=[element * (30*24*3600*0.001*1000) for element in Monthly_avg]
            yearly=sum(monthly_avg)
            plt.xlabel("Month")
            plt.ylabel("Average Precipitation (mm)")
        if parameter=='Evap_tavg':
            monthly_avg = [element * (30 * 24 * 3600 * 0.001 * 1000) for element in Monthly_avg]
            yearly = sum(monthly_avg)
            plt.xlabel("Month")
            plt.ylabel("Average Evapotranspiration (mm)")
        if parameter=='Tair_f_inst':
            monthly_avg = [element - 273 for element in Monthly_avg]
            yearly = np.mean(monthly_avg)
            plt.xlabel("Month")
            plt.ylabel("Average Temperature (mm)")
    print(f'{parameter} monthly avg is:', monthly_avg)
    print(f'{parameter} yearly avg is:', yearly)
    plt.plot(dates, monthly_avg)
    plt.xticks(rotation='vertical')
    plt.title(f'{parameter} in year 91')
    plt.show()
