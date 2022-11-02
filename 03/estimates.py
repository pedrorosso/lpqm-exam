from scipy.constants import Planck, pi, c

def solve_quadratic_equation(a: float, b: float, c: float):
    delta: float = b ** 2 - 4 * a * c
    sol1: float = 0.5 * (-b + delta ** 0.5) / a
    sol2: float = 0.5 * (-b - delta ** 0.5) / a

    return sol1, sol2

# Paper parameters
beta = 0.19
lambda_laser = 739.7e-9
linewidth_wavelength = 0.3e-9
lambda_pump = 632e-9
threshold_power = 27e-9

# Calculating pumping rates
R_pump = lambda_pump * threshold_power / (Planck * c)
gamma_cavity = 2 * pi * c * linewidth_wavelength / (lambda_laser ** 2)

# Calculating the expected photons inside the cavity
b_test = (1 / beta - R_pump / gamma_cavity)
c_test = -1.0 * R_pump / gamma_cavity

# Solving the quadratic equation for photonic populations
p1, p2 = solve_quadratic_equation(a=1, b=b_test, c=c_test)

# Calculating required photonic pump / laser pump
R_required = 0.5 * gamma_cavity * (1 + beta ** -1)
required_threshold_power = Planck * c * R_required / lambda_pump

print(f"Pumping rate R_pump: {R_pump:.3e} photons")
print(f"Frequency linewidth: {1e-9 * gamma_cavity / (2 * pi):.3f} GHz")
print(f"Possible photonic populations:\np1: {p1:.5f}\np2: {p2:.5f}")
print(f"Required photonic pump rate for P = 1: {R_required:.3e} photons")
print(f"Realistic threshold power: {1e6 * required_threshold_power} mW")