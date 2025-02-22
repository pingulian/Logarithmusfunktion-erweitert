%matplotlib inline 
# ↑ zur Verhinderung von evtl Problemen bei mehrfachem Ausführen
import numpy as np
import matplotlib.pyplot as plt
import sys
plt.style.use('_mpl-gallery') #fürs Diagramm
fig, ax = plt.subplots() #fürs Diagramm

# Werte aus Boyles Experiment
#x = np.array([1.0, 1.5, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0, 24.0, 28.0, 32.0])
#y = np.array([29.750, 19.125, 14.375, 9.5, 7.125, 5.625, 4.875, 4.250, 3.750, 3.375, 3.0, 2.625, 2.250, 2.0, 1.875, 1.750, 1.5, 1.375, 1.250])
#z = 0

# Werte aus Keplers Experiment
#x = np.array([1.0, 4.0, 9.0]) #Distance (D)
#y = np.array([1.0, 8.0, 27.0]) #Period(P)
#z = 0

# andere synthetische Werte (für x / y ↑ 3 = c)
#x = np.array([1, 8, 64])
#y = np.array([1, 2, 4])
#z = 0

#Werte Temperatur abkühlen (v5)
#x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150])
#y = np.array([23.75,23.75,23.77,23.73,22.95,22.42,21.89,21.45,21.1,20.76,20.25,19.77,19.34,18.96,18.55,18.24,17.97,17.66,17.36,17.1,16.87,16.78,16.48,16.26,16.1,15.97,15.76,15.53,15.37,15.33,15.3,15.18,14.95,14.58,14.26,14.05,13.98,13.78,13.57,13.39,13.29,13.08,12.82,12.62,12.46,12.33,12.32,12.26,12.2,12.02,11.92,11.9,11.82,11.71,11.63,11.57,11.41,11.28,11.15,11.02,10.84,10.71,10.54,10.42,10.35,10.24,10.11,10.02,9.94,9.79,9.69,9.6,9.52,9.41,9.31,9.18,9.03,8.92,8.84,8.71,8.5,8.48,8.37,8.27,8.18,8.05,7.93,7.82,7.72,7.61,7.51,7.4,7.29,7.17,7.09,7,6.89,6.82,6.7,6.51,6.47,6.46,6.36,6.26,6.16,6.05,5.97,5.87,5.81,5.71,5.61,5.5,5.42,5.34,5.24,5.1,4.97,4.86,4.71,4.62,4.59,4.52,4.47,4.39,4.35,4.28,4.21,4.18,4.09,4.04,3.97,3.91,3.83,3.76,3.75,3.61,3.56,3.48,3.4,3.35,3.26,3.26,3.22,3.15,3.06,2.97,2.93,2.9,2.86,2.79])
#z = 1

#Werte Temperatur abkühlen - y=ln(T)+3,17
#x = np.array([13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150])
#y = np.array([0.16, 0.18, 0.21, 0.23, 0.25, 0.26, 0.28, 0.3, 0.31, 0.33, 0.34, 0.35, 0.37, 0.38, 0.39, 0.4, 0.41, 0.43, 0.44, 0.44, 0.44, 0.45, 0.46, 0.49, 0.51, 0.53, 0.53, 0.54, 0.56, 0.57, 0.58, 0.6, 0.62, 0.63, 0.65, 0.66, 0.66, 0.66, 0.67, 0.68, 0.69, 0.69, 0.7, 0.71, 0.71, 0.72, 0.73, 0.74, 0.76, 0.77, 0.78, 0.8, 0.81, 0.82, 0.83, 0.84, 0.85, 0.86, 0.87, 0.89, 0.9, 0.91, 0.91, 0.93, 0.94, 0.95, 0.97, 0.98, 0.99, 1, 1.03, 1.03, 1.04, 1.06, 1.07, 1.08, 1.1, 1.11, 1.12, 1.14, 1.15, 1.17, 1.18, 1.2, 1.21, 1.22, 1.24, 1.25, 1.27, 1.29, 1.3, 1.3, 1.32, 1.33, 1.35, 1.37, 1.38, 1.4, 1.41, 1.43, 1.44, 1.46, 1.48, 1.49, 1.51, 1.54, 1.56, 1.59, 1.62, 1.64, 1.64, 1.66, 1.67, 1.69, 1.7, 1.71, 1.73, 1.74, 1.76, 1.77, 1.79, 1.8, 1.83, 1.84, 1.85, 1.88, 1.9, 1.92, 1.94, 1.96, 1.99, 1.99, 2, 2.02, 2.05, 2.08, 2.09, 2.1])
#z = 0

#Werte ln(Temperatur) abkühlen - y=ln(T)
#x = np.array([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150])
#y = np.array([-3.17, -3.17, -3.17, -3.17, -3.17, -3.13, -3.11, -3.09, -3.07, -3.05, -3.03, -3.01, -2.98, -2.96, -2.94, -2.92, -2.9, -2.89, -2.87, -2.85, -2.84, -2.83, -2.82, -2.8, -2.79, -2.78, -2.77, -2.76, -2.74, -2.73, -2.73, -2.73, -2.72, -2.7, -2.68, -2.66, -2.64, -2.64, -2.62, -2.61, -2.59, -2.59, -2.57, -2.55, -2.54, -2.52, -2.51, -2.51, -2.51, -2.5, -2.49, -2.48, -2.48, -2.47, -2.46, -2.45, -2.45, -2.43, -2.42, -2.41, -2.4, -2.38, -2.37, -2.36, -2.34, -2.34, -2.33, -2.31, -2.3, -2.3, -2.28, -2.27, -2.26, -2.25, -2.24, -2.23, -2.22, -2.2, -2.19, -2.18, -2.16, -2.14, -2.14, -2.12, -2.11, -2.1, -2.09, -2.07, -2.06, -2.04, -2.03, -2.02, -2, -1.99, -1.97, -1.96, -1.95, -1.93, -1.92, -1.9, -1.87, -1.87, -1.87, -1.85, -1.83, -1.82, -1.8, -1.79, -1.77, -1.76, -1.74, -1.72, -1.7, -1.69, -1.68, -1.66, -1.63, -1.6, -1.58, -1.55, -1.53, -1.52, -1.51, -1.5, -1.48, -1.47, -1.45, -1.44, -1.43, -1.41, -1.4, -1.38, -1.36, -1.34, -1.32, -1.32, -1.28, -1.27, -1.25, -1.22, -1.21, -1.18, -1.18, -1.17, -1.15, -1.12, -1.09, -1.08, -1.06])
#z = 0

#Werte Temperatur abkühlen (v5 - korrigiert)
x = np.array([13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150])
y = np.array([19.34,18.96,18.55,18.24,17.97,17.66,17.36,17.1,16.87,16.78,16.48,16.26,16.1,15.97,15.76,15.53,15.37,15.33,15.3,15.18,14.95,14.58,14.26,14.05,13.98,13.78,13.57,13.39,13.29,13.08,12.82,12.62,12.46,12.33,12.32,12.26,12.2,12.02,11.92,11.9,11.82,11.71,11.63,11.57,11.41,11.28,11.15,11.02,10.84,10.71,10.54,10.42,10.35,10.24,10.11,10.02,9.94,9.79,9.69,9.6,9.52,9.41,9.31,9.18,9.03,8.92,8.84,8.71,8.5,8.48,8.37,8.27,8.18,8.05,7.93,7.82,7.72,7.61,7.51,7.4,7.29,7.17,7.09,7,6.89,6.82,6.7,6.51,6.47,6.46,6.36,6.26,6.16,6.05,5.97,5.87,5.81,5.71,5.61,5.5,5.42,5.34,5.24,5.1,4.97,4.86,4.71,4.62,4.59,4.52,4.47,4.39,4.35,4.28,4.21,4.18,4.09,4.04,3.97,3.91,3.83,3.76,3.75,3.61,3.56,3.48,3.4,3.35,3.26,3.26,3.22,3.15,3.06,2.97,2.93,2.9,2.86,2.79])
z = 1

# Synthetische Werte (mit Fehler bei x[3]: 9 statt 8) (für x / -y = konstant)
#x = np.array([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
#y = np.array([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10])
#z = 0

if (z == 1):
    y = - np.log(y)
    y = y + 3.17

averagex = np.mean(x)
averagey = np.mean(y)
maxerlabweichung = 50 # Maximal zugelassene Abweichung in %
a = 1 #Exponent für x für print
b = 1 #Exponent für y für print
c = 1 #counter
d = 1 #für while

#Funktion zur Berechnung von Durchschnitt, Min, Max und Abweichung
def min_max_abw():
    # Berechnung von Durchschnitt, Maximal- und Minimalwert
    average = np.mean(xy)
    maxxy = np.max(xy)
    minxy = np.min(xy)

    maxabweichungnumb = max(abs(maxxy - average), abs(minxy - average))

    #Abweichung in %
    abweichung = np.absolute((maxabweichungnumb / average) * 100)

    return average, maxxy, minxy, maxabweichungnumb, abweichung

# im Falle eines antiproportinalen Zusammenhangs
def antiproportional(average, maxxy, minxy, maxabweichungnumb, abweichung):
    if abweichung < maxerlabweichung:
        print(" - x entspricht t (Zeit); y entspricht log(T) (Temperatur) - ")
        print("Durchschnitt von (x ↑",a,"* y ↑",b,"):", average)
        print("Maximaler Wert:", maxxy)
        print("Minimaler Wert:", minxy)
        print("\nMaximale Abweichung vom Durchschnitt (Absolute Zahl):", maxabweichungnumb)
        print("Maximale Abweichung vom Durchschnitt (%):", abweichung, "%")
        print("Maximal zugelassene Abweichung:", maxerlabweichung, "%")
        print("\nErgebnis:")
        
        print("(x ↑",a,"* y ↑",b,") = konstant (antiproportional)")
        print("(Die Abweichung vom Durchschnitt überschreitet die maximal zugelassene Abweichung nicht)")
        sys.exit()
    else:
        print("(x ↑",a,"* y ↑",b,") ist nicht konstant (nicht antiproportional)")
        print("(Die Abweichung vom Durchschnitt überschreitet die maximal zugelassene Abweichung)")
        

# im Falle eines proportionalen Zusammenhangs
def proportional(average, maxxy, minxy, maxabweichungnumb, abweichung):
    if abweichung < maxerlabweichung:
        print(" - x entspricht t (Zeit); y entspricht log(T) (Temperatur) - ")
        print("Durchschnitt von (x ↑",a,"/ y ↑",b,"):", average)
        print("Maximaler Wert:", maxxy)
        print("Minimaler Wert:", minxy)
        print("\nMaximale Abweichung vom Durchschnitt (Absolute Zahl):", maxabweichungnumb)
        print("Maximale Abweichung vom Durchschnitt (%):", abweichung, "%")
        print("Maximal zugelassene Abweichung:", maxerlabweichung, "%")
        print("\nErgebnis:")
        
        print("(x ↑",a,"/ y ↑",b,") = konstant (proportional)")
        print("(Die Abweichung vom Durchschnitt überschreitet die maximal zugelassene Abweichung nicht)")
        sys.exit()
    else:
        print("(x ↑",a,"/ y ↑",b,") ist nicht konstant (nicht proportional)")
        print("(Die Abweichung vom Durchschnitt überschreitet die maximal zugelassene Abweichung)")

def diagramm():
    ax.set_title('log(T)(t)-Diagramm')
    ax.set_xlabel('Zeit t (in s)')
    ax.set_ylabel('log der Temperatur T (in °C)')        
    ax.plot(x, y, linewidth=2.0)
    plt.show()
    
try:
    #Antiproportionaler Zusammenhang
    if (abs(x[1]) > abs(x[-1]) and abs(y[1]) < abs(y[-1])) or (abs(x[1]) < abs(x[-1]) and abs(y[1]) > abs(y[-1])):
        diagramm()
        print("Antiproportionaler Zusammenhang")
        xy = x * y
        average, maxxy, minxy, maxabweichungnumb, abweichung = min_max_abw()
        antiproportional(average, maxxy, minxy, maxabweichungnumb, abweichung)

        #Was soll passieren, wenn xy nicht konstantt ist (nicht antiproportional)?
        while d == 1: 
            if (xy[1] > xy[-1] and x[1] < x[-1]) or (xy[1] < xy[-1] and x[1] > x[-1]): #Antiproportional
                c = c + 1
                print("Zusammenhang", c )
                a = a + 1 #Exponent von x erhöhen
                xy = xy * x
                average, maxxy, minxy, maxabweichungnumb, abweichung = min_max_abw()
                antiproportional(average, maxxy, minxy, maxabweichungnumb, abweichung)
        
            else: #Proportional
                c = c + 1
                print("Zusammenhang", c )
                b = b + 1 #Exponent von y erhöhen
                xy = xy * y
                average, maxxy, minxy, maxabweichungnumb, abweichung = min_max_abw()
                antiproportional(average, maxxy, minxy, maxabweichungnumb, abweichung)

    #Proportionaler Zusammenhang
    else:
        diagramm()
        print("Proportionaler Zusammenhang")
        xy = x / y
        average, maxxy, minxy, maxabweichungnumb, abweichung = min_max_abw()
        proportional(average, maxxy, minxy, maxabweichungnumb, abweichung)

        #Was soll passieren, wenn x/y nicht konstantt ist (nicht proportional)?
        while d == 1:
            if (xy[1] > xy[-1] and x[1] > x[-1]) or (xy[1] < xy[-1] and x[1] < x[-1]): #Proportional
                c = c + 1
                print("Zusammenhang", c )
                b = b + 1 #Exponent von y erhöhen
                xy = xy / y
                average, maxxy, minxy, maxabweichungnumb, abweichung = min_max_abw()
                proportional(average, maxxy, minxy, maxabweichungnumb, abweichung)

            else: #Antiproportional
                c = c + 1
                print("Zusammenhang", c )
                a = a + 1 #Exponent von x erhöhen
                xy = xy * x
                average, maxxy, minxy, maxabweichungnumb, abweichung = min_max_abw()
                proportional(average, maxxy, minxy, maxabweichungnumb, abweichung)


except SystemExit: #Dient dem Verhindern einer Errormessage bei Verwendung von sys.exit() Fehlerbehandlung:
    pass # Keine Fehlermeldung anzeigen, wenn das Programm gestoppt wurde
