#-------------------------------------------------------------------------------
# fibonacci.py - code for cSplash 2011 class "Fibonacci numbers in nature"
#
# Kenneth L. Ho (ho@courant.nyu.edu)
#-------------------------------------------------------------------------------

from __future__ import division

import numpy as np
from matplotlib import pyplot as plt
import os
import subprocess

phi = (1 + np.sqrt(5)) / 2

#-------------------------------------------------------------------------------
# floret growth
#-------------------------------------------------------------------------------

def grow_florets(n, turn=np.mod(phi,1)):
  i = np.arange(n)
  theta = np.mod(2*np.pi*turn*i, 2*np.pi)
  r = (n - i) / n
  return theta, r

def show_florets(theta, r, **kwargs):
  plt.figure(figsize=(6,6))
  plt.polar(theta, r, '.', **kwargs)
  plt.gca().set_rticks([])
  plt.show()

def show_floret_growth(theta, r, prefix='frame', grow=True, ms=10):
  n = len(r)
  savefmt = prefix + '%0' + str(len(str(n-1))) + 'i.png'
  plt.figure(figsize=(6,6))
  for i in range(n):
    plt.clf()
    if grow: s = float(n - i - 1) / n
    else:    s = 0.
    plt.polar(theta[:i+1], r[:i+1]-s, '.', mec='k', mfc='b', ms=ms)
    plt.polar(theta[i], r[i]-s, '.', mec='k', mfc='r', ms=ms)
    plt.gca().set_rlim([0, 1])
    plt.gca().set_rticks([])
    plt.savefig(savefmt %i)

def fibonacci_lim(lim):
  F = []
  if lim >= 0: F.append(0)
  if lim >= 1: F.append(1)
  f = 1
  while f <= lim:
    F.append(f)
    f = F[-1] + F[-2]
  return F

def floret_revolutions(n, **kwargs):
  r = np.arange(n)
  F = fibonacci_lim(r[-1])
  plt.figure(figsize=(6,6))
  plt.polar(np.mod(r/phi,1)*2*np.pi, r, '.', **kwargs)
  plt.polar(np.mod(F/phi,1)*2*np.pi, F, 'r.', **kwargs)
  plt.gca().set_rticks([])
  plt.show()

def floret_spirals(n=250, i=7, **kwargs):
  theta, r = grow_florets(n)
  F = fibonacci_lim(n)
  plt.figure(figsize=(6,6))
  plt.polar(theta[:F[i]], r[:F[i]], 'b.', **kwargs)
  plt.polar(theta[F[i]:F[i+1]], r[F[i]:F[i+1]], 'r.', **kwargs)
  plt.polar(theta[F[i+1]:], r[F[i+1]:], '.', c='0.75', **kwargs)
  plt.gca().set_rticks([])
  plt.show()

#-------------------------------------------------------------------------------
# convergents
#-------------------------------------------------------------------------------

pi_cfrac    = [3, 7, 15, 1, 292, 1, 1, 1, 2, 1]
e_cfrac     = [2, 1,  2, 1,  1,  4, 1, 1, 6, 1]
sqrt2_cfrac = [1, 2,  2, 2,  2,  2, 2, 2, 2, 2]
phi_cfrac   = [1, 1,  1, 1,  1,  1, 1, 1, 1, 1]

def convergents(cfrac):
  n = len(cfrac)
  numer = np.empty(n, dtype=int)
  denom = np.empty(n, dtype=int)
  if n >= 1:
    numer[0] = cfrac[0]
    denom[0] = 1
  if n >= 2:
    numer[1] = cfrac[1]*cfrac[0] + 1
    denom[1] = cfrac[1]
  for i in range(2,n):
    numer[i] = cfrac[i]*numer[i-1] + numer[i-2]
    denom[i] = cfrac[i]*denom[i-1] + denom[i-2]
  return numer, denom

#-------------------------------------------------------------------------------
# videos
#-------------------------------------------------------------------------------

def png2avi(src_dir, dest, fps=20):
  command = ['mencoder', 'mf://%s/*.png' % src_dir, '-mf',
             'type=png:fps=%i' % fps, '-ovc', 'lavc', '-lavcopts',
             'vcodec=mpeg4', '-oac', 'copy', '-o', dest]
  subprocess.check_call(command)

def generate_grow_4_data(data_dir='../data'):
  path = '%s/grow-4' % data_dir
  if not os.path.exists(path): os.makedirs(path)
  theta, r = grow_florets(50, 1./4)
  show_floret_growth(theta, r, prefix='%s/frame' % path, ms=15)
  png2avi(path, '%s/grow-4.avi' % data_dir, fps=5)

def generate_grow_5_data(data_dir='../data'):
  path = '%s/grow-5' % data_dir
  if not os.path.exists(path): os.makedirs(path)
  theta, r = grow_florets(50, 1./5)
  show_floret_growth(theta, r, prefix='%s/frame' % path, ms=15)
  png2avi(path, '%s/grow-5.avi' % data_dir, fps=5)

def generate_grow_phi_data(data_dir='../data'):
  path = '%s/grow-phi' % data_dir
  if not os.path.exists(path): os.makedirs(path)
  theta, r = grow_florets(500)
  show_floret_growth(theta, r, prefix='%s/frame' % path)
  png2avi(path, '%s/grow-phi.avi' % data_dir, fps=20)

def generate_grow_phi_fixed_data(data_dir='../data'):
  path = '%s/grow-phi-fixed' % data_dir
  if not os.path.exists(path): os.makedirs(path)
  theta, r = grow_florets(500)
  show_floret_growth(theta, r, prefix='%s/frame' % path, grow=False)
  png2avi(path, '%s/grow-phi-fixed.avi' % data_dir, fps=20)