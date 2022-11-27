from numpy import absolute, ndarray
from numpy.fft import fftfreq, fft, ifft
from scipy.constants import c, hbar, pi

# Simulation parameters from appendix
D2 = 2.2e6 * 2 * pi
D3 = 25e3 * 2 * pi
D4 = -300 * 2 * pi
P_in = 1.0
xi = 12
q_int = 1.5e6
q_ext = 8e5

# Taken from figure 2
omega_p = 192.2e12 * 2 * pi

n2_SiN = 1.4e-18 # NOT KNOWN
omega_0 = 1.0 # NOT KNOWN

# Taken from text
n_SiN = 2.0
a_eff = 800e-9 ** 2
l_eff = pi * 238e-6
g = hbar * omega_0 * omega_0 * c * n2_SiN / (n_SiN * n_SiN * a_eff * l_eff)

kappa = 1.0 # NOT KNOWN
eta = 1.0 # NOT KNOWN

def dA_dt(t: float,
          A: ndarray) -> ndarray:

    dA_dphi2 = ifft(fft(A) * -1.0 * (fftfreq(A.shape[-1])) ** 2)
    phi_term = 0.5j * D2 * dA_dphi2
    pump_term = (kappa * eta * P_in / (hbar * omega_0)) ** 0.5
    linear_term = (-0.5 * kappa - 1.0j * (omega_0 - omega_p)) * A
    kerr_term = 1.0j * g * absolute(A) ** 2 * A

    return phi_term + kerr_term + linear_term + pump_term

if __name__ == '__main__':
    print(f"g: {g:.5e}")