import os
import numpy as np
from matplotlib import pyplot as plt
from camb import model

import camb

z = np.linspace(0, 3)
a = 1/(1+z)
def get_pk_for_version(version):
    pars = camb.set_params(
        H0=67.5, ombh2=0.022, omch2=0.122, mnu=0.06, omk=0, tau=0.06, As=2e-9, ns=0.965,
        dark_energy_model="LateDE", DEmodel=11, pade_eps0=1.0, pade_eta0=10,
        halofit_version=version, lmax=3000, WantTransfer=True
    )
    pars.NonLinear = model.NonLinear_both
    results = camb.get_results(pars)
    rho_de, w_de = results.get_dark_energy_rho_w(a)
    kh, z, pk = results.get_matter_power_spectrum(minkh=1e-4, maxkh=5, npoints=200)
    return kh, pk[0], rho_de, w_de


kh, pk_hmcode_original, rho_de, w_de = get_pk_for_version("mead2020")
kh, pk_hmcode_modified, rho_de, w_de = get_pk_for_version("mead2020_de")
plt.plot(z, w_de)
plt.show()