#!/usr/bin/env python3

#=======================================================
# 
# A simple way to construct the spin-glass model
# namely, Edwards-Anderson model
#
# By default it is built on the simple-cubic lattice
# with random nearest hopping
# You can change it to other lattice in need
#
# Copyright @ Shunhong Zhang 2024-2025
# zhangshunhong.pku@gmail.com
#
#=========================================================

import os
import numpy as np
from asd.core.hamiltonian import *
from asd.core.geometry import *
from asd.core.shell_exchange import exchange_shell


# Gaussian distribution, with mean of 0, and standard deviation J_std
# bimodal: J = 1 or -1 with probablity of p and q (default: p = q = 0.5)
def generate_random_exchanges(Nbonds, J_mean=0., J_std=1., random_type='Gaussian', p_positive=0.5):
    if random_type=='Gaussian':    J_random = np.random.normal(loc=J_mean, scale=J_std, size=int(Nbonds) )
    elif random_type=='bimodal':   J_random = np.sign(np.random.random(Nbonds)-(1-p_positive))
    else:  raise ValueError ("Wrong random_type of {}".format(random_type))
    return J_random



def hist_exchange_couplings(J_random, J_mean=None, J_std=None, save=False, show=False):
    import matplotlib.pyplot as plt
    n_tot = len(J_random)
    fig, ax = plt.subplots(1,1)
    if J_mean is not None and J_std is not None:
        xx = np.linspace(J_mean-5*J_std, J_mean+5*J_std, 201)
        yy = 1/np.sqrt(2*np.pi*J_std**2) * np.exp(-(xx - J_mean)**2/2/J_std**2)
        yy *= np.sqrt(n_tot)
        #yy *= np.sqrt(2*np.pi*J_std**2)
        int_g = np.trapz(yy, x=xx)
        #print (int_g)
        ax.plot(xx, yy, alpha=0.5)
    hist, bins = np.histogram(J_random)
    ax.hist(J_random, fc='none', ec='C1', bins=20)
    ax.set_xlabel(r"$J_{ex}$ (meV)",fontsize=12)
    ax.set_ylabel(r"Count",fontsize=12)
    title = 'Total {}'.format(n_tot)
    ax.set_title(title,fontsize=12)
    fig.tight_layout()
    if save: fig.savefig('exchanges_histogram',dpi=200)
    if show: plt.show()
    return fig, hist, bins


def build_EA_model_ham(all_neigh_idx_sc, J_mean=0., J_d=1., random_type='Gaussian', p_positive=0.5, ham_kws={}):

    neigh_idx = all_neigh_idx_sc[0]
    bonds_indices = index_shell_bonds(neigh_idx)
    Nsites = len(neigh_idx)
    Nbonds = np.sum([len(neigh_iat) for neigh_iat in neigh_idx if neigh_iat is not None])
    #print ("Generate {} bonds for {} sites".format(Nbonds, Nsites))

    # unified ferromagnetic exchange
    J_iso_1 = np.ones(Nsites)

    if random_type=='Gaussian':  J_std = np.sqrt( J_d**2/ Nsites)
    else: J_std = None
    J_random = generate_random_exchanges(Nbonds, J_mean, J_std, random_type, p_positive)
    #fig, hist, bins = hist_exchange_couplings(J_random, J_mean, J_std, show=True)

    J_iso_2 = []
    for iat, bonds_iat in enumerate(bonds_indices):
        J_iso_2.append([])
        if bonds_iat is None: continue
        for ibond, bond_index in enumerate(bonds_iat):
            J_iso_2[iat].append(J_random[bond_index])

    exch_1 = exchange_shell(all_neigh_idx_sc[0], J_iso = J_iso_1, shell_name='1NN_uniform')
    exch_2 = exchange_shell(all_neigh_idx_sc[0], J_iso = J_iso_2, shell_name='1NN_random')
    ham_kws.update( BL_exch = [exch_2] )
    ham = spin_hamiltonian(**ham_kws)
    return ham




"""
Here we use the simple-cubic lattice as an example to demonstrate the usage
You can build the Edwards-Anderson model on other lattices similarly
"""

nx=3
ny=3
nz=3
lat_type='simple cubic'
latt, sites, all_neigh_idx, rotvecs = build_latt(lat_type,nx,ny,nz)
nat=sites.shape[-2]
Bfield=np.array([0,0,0])

""" Indices for neighboring atoms of each atom within the nx*ny*nz supercell. """
all_neigh_idx_sc = gen_neigh_idx_for_supercell(all_neigh_idx, nx, ny, nz)

""" Convert the atom position into the fractional coordinate of the supercell. """
sites_cart = np.dot(sites, latt)
latt = np.dot(np.diag([nx,ny,nz]), latt)
sites = np.dot(sites_cart, np.linalg.inv(latt))
sites = sites.reshape(1,1,1,-1,sites.shape[-1])


nat = sites.shape[-2]
S_values = np.tile( [1], (nx*ny*nz,1)).flatten()
SIA = np.tile( [0.5], (nx*ny*nz,1) ).flatten()


J_mean = 0.
J_d = 1.

ham_kws = dict(
Bfield=Bfield,
S_values=S_values,
BL_SIA=[SIA],
iso_only=True,
boundary_condition=[1,1,1])


if __name__ == '__main__':
    # Example of building a bimodal EA model with unbalanced positive (FM) and negative (AFM) exchanges
    ham = build_EA_model_ham(all_neigh_idx_sc, J_mean, J_d, random_type='bimodal', p_positive=0.8, ham_kws=ham_kws)

    # Example of building a Gaussian-random EA model with zero mean and unity variance
    # Note that J_d = 1 is not the standard deviation, (J_d^2/N) is. (N is the number of sites)
    ham = build_EA_model_ham(all_neigh_idx_sc, J_mean, J_d, random_type='Gaussian', ham_kws=ham_kws)

    #ham.verbose_all_interactions()
