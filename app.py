from flask import Flask
import math
app = Flask(__name__)


'''
DIAMETER = Średnica
VOLUME = Objętość
TEMP = Temperatura
POWER = Moc
DURATION = Czas trwania
AMBIENT TEMP = Temperatura otoczenia

c = ciepło właściwe substancji (dla wody wynosi około 4190 [J/kg*K])
Q = energia (ciepło) dostarczane do ciała
m = masa substancji [kg]
deltaT = różnica temperatur wody przed i po zagotowaniu [st C]
ciepło właściwe substancji można wyznaczyć z zależności:
c = Q / m * deltaT
Moc można zdefiniować jako zdolność układu do wykonania określonej pracy w danym czasie. lm szybciej wykonana
zostanie dana praca, tym większa będzie moc i odwrotnie.

W = praca
t = czas od włączenia do wyłączenia sie czajnika [s]
P = W / t   moc
U = napięcie prądu [V]
I = natężenie prądu [A]

wzór na wyznaczenie sprawności czajnika elektrycznego = (m * c * deltaT) / (U * I * t) 
'''

class Kettle(object):
    # Args:
    SPECIFIC_HEAT_CAP_WATER = 4.182  # c = 4.182 kJ / kg * K
    THERMAL_CONDUCTIVITY_STEEL = 15  # lambda = 15 W / m * K
    VOLTAGE = 230 # Volts

    def __init__(self):
        self.diameter = 5
        self.volume = 5
        self.temp = 5
        self.power = 5
        self.duration = 5
        self.ambient_temp = 5
        self.amper = 5

    def mass_surface(self, density=1):
        self._mass = self.volume * density
        self._temp = self.temp
        radius = self.diameter / 2

        # height in cm
        height = (self.volume * 1000) / (math.pi * math.pow(radius, 2))
        # surface in m^2
        self._surface = (2 * math.pi * math.pow(radius, 2) + 2 * math.pi * radius * height) / 10000

    def temperature(self):
        return self.temp

    def heat(self, power, duration, efficiency=0.98):
        self._temp += self.deltaT(power * efficiency, duration)
        return  self._temp

    def cool(self, duration, ambient_temp, heat_loss_factor=1):
        # Q = k_w * A * (T_kettle - T_ambient)
        # P = Q / t
        power = ((Kettle.THERMAL_CONDUCTIVITY_STEEL * self._surface * (self._temp - ambient_temp)) / duration)

        # W to kW
        power /= 1000
        self._temp -= self.deltaT(power, duration) * heat_loss_factor
        return self._temp

    def deltaT(self, power, duration):
        # P = Q / t
        # Q = c * m * delta T
        # => delta(T) = (P * t) / (c * m)
        return ((power * duration) / (Kettle.SPECIFIC_HEAT_CAP_WATER * self._mass))

    def efficiency(self):
        #(m * c * deltaT) / (U * I * t)
        efficiency = (power * Kettle.SPECIFIC_HEAT_CAP_WATER * self.deltaT(power, duration)) / (Kettle.VOLTAGE * amper * duration)
        return efficiency


diameter = 5
volume = 5
temp = 5
power = 5
duration = 5
ambient_temp = 5
amper = 5




@app.route("/")
def home():
    kettle = Kettle()
    return kettle.temperature()

@app.route("/test/")
def home():
    return "test jest git"

