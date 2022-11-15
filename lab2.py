from __future__ import division, print_function
from vpython import *
scene.width = scene.height = 600
scale = 1.63
sff=2e5
sf=0.5
K = 8.987e9 
mProton = 1.672e-27 
cProton = 1.602e-19
melectron = 9.11e-31
celectron = -1.602e-19
deltat = 0.00007

proton1 = sphere(pos=vector(0,0,0), radius=0.2, color=color.cyan)
electron = sphere(pos=vector(-0.529, 0,0), radius=0.05,
               color=color.yellow, make_trail=True)
proton2 = sphere(pos=vector(1.052,0,0), radius=0.2, color=color.white)

# v = sqrt(kqq/mr) for an electron with a circular orbit around proton1
# = 

vi = scale*sqrt(K*cProton*celectron/(-0.529*melectron))

#
#   For Part 1
#     * vi = sqrt(K*cProton*celectron/(-0.529*melectron)) = 21.88
#     * deltat = 0.000001
#
print('vi=', vi)


#
#   For Part 2
#     * vi =1.29*sqrt(K*cProton*celectron/(-0.529*melectron)) = 28.221011023688423 
#     * vi = 31.798918930127652 is also stable at deltat = 0.00007
#     * deltat for vi=28.22 is 0.00001
#

#
#   For Part 3
#     * Figure 8: vi = 19.962536867531536
#     * Escape 1: vi = 30.94356384
#         * v = sqrt(2kqq/(m_e*r)
#     * Escape 2: vi = 35.74749579
#         * v = sqrt( 2kqq/(m_e*r)  + 2kqq/(m_e * (r+1.052)) )
#     * Calculations:
#          delta K = 1/2 m_e * v_final^2 - 1/2 m_e * v_original^2  
#         1. delta K = 2.1807 * 10^-28 J = 1.36 * 10^-9 eV
#         2. delta K = 5.6759 * 10^-28 J = 3.54 * 10^-9 eV
#

velectron = vector(0,vi,0)
pelectron = melectron*velectron
print('p=', pelectron)
t = 0
#Fgrav = 1
#parr = arrow(pos=electron.pos, axis=sf*pelectron, color=color.green, shaftwidth = electron.radius*2)#
#farr = arrow(pos=electron.pos, axis=sff*Fgrav, color=color.blue, shaftwidth = electron.radius/2)
#farr=arrow(pos=electron.pos, color=color.red, shaftwidth=electron.radius*2)
#farrm=arrow(pos=electron.pos, color=color.red, shaftwidth=electron.radius/2)

scene.autoscale = True ##turn off automatic camera zoom

scene.center = (proton1.pos + proton2.pos)/2

while t < 100*24*60*60:
    rate(5e3)     
    rvec=electron.pos-proton1.pos
    rvecm=electron.pos-proton2.pos
    rhat=norm(rvec)
    rhatm=norm(rvecm)
    fmag=-K*cProton*celectron/mag(rvec)**2
    fmagm=-K*cProton*celectron/mag(rvecm)**2
    Fgrav=fmag*rhat+fmagm*rhatm
    pelectron=pelectron-Fgrav*deltat
    electron.pos = electron.pos + (pelectron/melectron)*deltat
    #parr.pos = electron.pos
    #parr.axis=sf*pelectron*10
    #farr.pos = electron.pos
    #farr.axis = -sff*Fgrav    
    t = t+deltat


