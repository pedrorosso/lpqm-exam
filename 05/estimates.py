from scipy.constants import pi, G, hbar, m_e

mass_earth = 5.9722e24
omega_CS = 9192631770 * 2 * pi


def delta_T(r1, r2): return 2 * pi * G * mass_earth * m_e / \
    (omega_CS ** 2 * hbar) * abs(r1 ** -1 - r2 ** -1)


r_0 = 6370e3
r_1 = 6470e3

print(f"Delta T: {delta_T(r_0, r_1)}")
