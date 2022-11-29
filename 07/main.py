from numpy import zeros, linspace
from scipy.integrate import solve_ivp

from core import dA_dt
from plotter import spectral_plot


if __name__ == '__main__':

    n_dim = 10
    t_array = linspace(0.0, 4e-10, 1000)

    solution = solve_ivp(
        fun=dA_dt,
        t_eval=t_array,
        t_span=[t_array[0], t_array[-1]],
        y0=zeros(n_dim, dtype=complex)
    )

    spectral_plot(t=solution.t, A=solution.y)

    print("Done!")