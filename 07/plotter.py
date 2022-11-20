from numpy import ndarray, absolute
from numpy.fft import fft, fftshift
from matplotlib.pyplot import subplots

def spectral_plot(t: ndarray, A: ndarray):
    fig, axs = subplots(nrows=1, ncols=1, figsize=(8,4), facecolor="white")
    FA = fftshift(fft(A[0,:]))
    omega = fftshift(fft(t))
    axs.plot(omega, absolute(FA), label="Specturm of A")
    axs.set_xlabel(r"$\omega / 2 \pi \ [s^{-1}]$")
    axs.set_ylabel(r"|A(\omega)|^2|")

    fig.savefig("Power_vs_Freq.png")