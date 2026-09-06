import numpy as np
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
def update_position(pos, vel, dt):
    return pos + vel * dt
def update_velocity(vel, acc, dt):
    return vel + acc * dt
#constants
G, ms, me, mj, dt ,ti = 6.67430e-11, 1.98847e30, 5.9722e24, 1.898e27, 300, 12 * 365 * 24 * 3600               
#velocity of the sun
vxs = 0
vys = 0
#Velocity of the earth
vxe = 0
vye = 30290
#velocity of jupiter
vxj=0
vyj=13070
#Position of the sun
xs = 0
ys = 0
#Position of the earth
xe = 1.4710e11
ye = 0
#postion of jupiter
xj=7.405e11
yj=0
xs = -(me * xe + mj * xj) / ms
vys = -(me * vye + mj * vyj) / ms
#distance vectors
#EARTH-SUN
dx_es, dy_es = xe - xs, ye - ys
r_es = (dx_es**2 + dy_es**2)**0.5
dx_js, dy_js = xj - xs, yj - ys
r_js = (dx_js**2 + dy_js**2)**0.5
dx_ej, dy_ej = xe - xj, ye - yj
r_ej = (dx_ej**2 + dy_ej**2)**0.5
#acceleraion for earth due to to the sun and jupiter
acc_ex= -G*ms*dx_es/r_es**3 - G*mj*dx_ej/r_ej**3
acc_ey  = -G*ms*dy_es/r_es**3 - G*mj*dy_ej/r_ej**3
acc_e = (acc_ex**2 + acc_ey**2)**0.5
#acceleratioon of jupiter due to the sun and earth
acc_jx= -G*ms*dx_js/r_js**3 - G*me*dx_ej/r_ej**3
acc_jy= -G*ms*dy_js/r_js**3 - G*me*dy_ej/r_ej**3
acc_j = (acc_jx**2 + acc_jy**2)**0.5
#acceleration of the sun due to the earth and jupiter
acc_sx= G*me*dx_es/r_es**3 + G*mj*dx_js/r_js**3
acc_sy = G*me*dy_es/r_es**3 + G*mj*dy_js/r_js**3
acc_s = (acc_sx**2 + acc_sy**2)**0.5
#postion
pexlist, peylist, psxlist, psylist, pjxlist, pjylist = [], [], [], [], [], []
hexlist, heylist, hsxlist, hsylist, hjxlist, hjylist = [], [], [], [], [], []
for time in range(0, ti, dt): 
    hex = update_velocity(vxe, acc_ex, dt)
    hey = update_velocity(vye, acc_ey, dt)
    hsx = update_velocity(vxs, acc_sx, dt)
    hsy = update_velocity(vys, acc_sy, dt)
    hjx = update_velocity(vxj, acc_jx, dt)
    hjy = update_velocity(vyj, acc_jy, dt)
    vxe, vye = hex, hey
    vxs, vys = hsx, hsy
    vxj, vyj = hjx, hjy
    pex = update_position(xe, vxe, dt)
    pey = update_position(ye, vye, dt)
    psx = update_position(xs, vxs, dt)
    psy = update_position(ys, vys, dt)
    pjx = update_position(xj, vxj, dt)
    pjy = update_position(yj, vyj, dt)
    xe, ye = pex, pey
    xs, ys = psx, psy
    xj, yj = pjx, pjy
    dx_es, dy_es = pex - psx, pey - psy
    r_es = (dx_es**2 + dy_es**2)**0.5
    dx_js, dy_js = pjx - psx, pjy - psy
    r_js = (dx_js**2 + dy_js**2)**0.5
    dx_ej, dy_ej = pex - pjx, pey - pjy
    r_ej = (dx_ej**2 + dy_ej**2)**0.5
    acc_ex = -G * ms * dx_es / r_es**3 - G * mj * dx_ej / r_ej**3
    acc_ey = -G * ms * dy_es / r_es**3 - G * mj * dy_ej / r_ej**3
    acc_jx = -G * ms * dx_js / r_js**3 - G * me * dx_ej / r_ej**3
    acc_jy = -G * ms * dy_js / r_js**3 - G * me * dy_ej / r_ej**3
    acc_sx = G * me * dx_es / r_es**3 + G *mj * dx_js / r_js**3
    acc_sy = G * me * dy_es / r_es**3 + G * mj * dy_js / r_js**3
    pexlist.append(pex)
    peylist.append(pey)
    psxlist.append(psx)
    psylist.append(psy)
    pjxlist.append(pjx)
    pjylist.append(pjy)
    hexlist.append(hex)
    heylist.append(hey)
    hsxlist.append(hsx)
    hsylist.append(hsy)
    hjxlist.append(hjx)
    hjylist.append(hjy)
fig, ax = plt.subplots(figsize=(9, 9))
max_range = 9.0e11  
ax.set_xlim(-max_range, max_range)
ax.set_ylim(-max_range, max_range)
ax.set_aspect('equal')
ax.grid(True, linestyle=':', alpha=0.6)
ax.plot(psxlist, psylist, color='orange', linewidth=1.5, linestyle='--', alpha=0.6, label='Sun Path')
ax.plot(pexlist, peylist, color='blue', linewidth=1.5, linestyle='--', alpha=0.6, label='Earth Orbit')
ax.plot(pjxlist, pjylist, color='red', linewidth=1.5, linestyle='--', alpha=0.6, label='Jupiter Orbit')
sun_dot, = ax.plot([], [], 'o', color='orange', markersize=16, label='Sun')
earth_dot, = ax.plot([], [], 'o', color='blue', markersize=8, label='Earth')
jupiter_dot, = ax.plot([], [], 'o', color='red', markersize=12, label='Jupiter')
ax.set_xlabel("X Position", fontsize=8)
ax.set_ylabel("Y Position", fontsize=8)
ax.set_title("Three-Body Orbital Simulation: Sun, Earth, and Jupiter", fontsize=13, weight='bold')
ax.legend(loc='upper right', fontsize=8)
step_skip = 60  
total_frames = len(pexlist) // step_skip
def init():
    sun_dot.set_data([], [])
    earth_dot.set_data([], [])
    jupiter_dot.set_data([], [])
    return sun_dot, earth_dot, jupiter_dot
def animate(lol):
    idx = lol * step_skip
    sun_dot.set_data([psxlist[idx]], [psylist[idx]])
    earth_dot.set_data([pexlist[idx]], [peylist[idx]])
    jupiter_dot.set_data([pjxlist[idx]], [pjylist[idx]])
    return sun_dot, earth_dot, jupiter_dot
anim = FuncAnimation(fig, animate, init_func=init, frames=total_frames, interval=15, blit=True)
plt.show()