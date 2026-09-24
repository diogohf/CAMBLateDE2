import os
import numpy as np
from matplotlib import pyplot as plt
from camb import model

import camb

def get_pk_for_version(version):
    pars = camb.set_params(
        H0=67.5, ombh2=0.022, omch2=0.122, mnu=0.06, omk=0, tau=0.06, As=2e-9, ns=0.965, w0=-0.85, w1=-0.6, dark_energy_model="LateDE", DEmodel=2,
        halofit_version=version, lmax=3000, WantTransfer=True
    )
    pars = camb.set_params(
        H0=67.5, ombh2=0.022, omch2=0.122, mnu=0.06, omk=0, tau=0.06, As=2e-9, ns=0.965,
        dark_energy_model="LateDE", DEmodel=3, z_knot=[0.3, 0.6, 0.9, 1.2, 1.5], w_knot=[-1, -0.9, -0.8, -1.1, -1.2],
        halofit_version=version, lmax=3000, WantTransfer=True
    )
    pars.NonLinear = model.NonLinear_both
    results = camb.get_results(pars)
    kh, z, pk = results.get_matter_power_spectrum(minkh=1e-4, maxkh=5, npoints=200)
    return kh, pk[0]
kh, pk_hmcode_original = get_pk_for_version("mead2020")
kh, pk_hmcode_modified = get_pk_for_version("mead2020_de")
plt.semilogx(kh, (pk_hmcode_modified - pk_hmcode_original)/pk_hmcode_original)
plt.show()