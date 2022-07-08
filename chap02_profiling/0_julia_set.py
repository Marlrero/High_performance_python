# %%
z = -1.8 -1.8j
print(abs(z))

# %%
c = -0.62772 -0.42193j
z = 0 + 0j
for n in range(9):
    z = z*z + c  # f(z) = z^2 + c
    print(f'{n}: z={z: .5f}, abs(z)={abs(z): 0.3f}, c={c: .5f}')
    
    # abs(z) < 2를 만족하므로 계속 z 값을 갱신함

# %%
c = -0.62772 -0.42193j
z = 0j
z_list_1 = []
for n in range(50):
    z = z*z + c  # f(z) = z^2 + c
    print(f'{n}: z={z: .5f}, abs(z)={abs(z): 0.3f}, c={c: .5f}')
    z_list_1.append(z)

# %%
c = -0.62772 -0.42193j
z = -0.82 + 0j
z_list_2 = []
for n in range(50):
    z = z*z + c  # f(z) = z^2 + c
    print(f'{n}: z={z: .5f}, abs(z)={abs(z): 0.3f}, c={c: .5f}')
    z_list_2.append(z)
# %%
import matplotlib.pyplot as plt
import numpy as np
# %%
x = range(50)
y1 = np.array(z_list_1)
y2 = np.array(z_list_2)

plt.plot(x, y1, 'b', x, y2, 'r--')
plt.legend(['z=0j', 'z=(-0.82+0j)'])
plt.ylim(-1, 2.5)
plt.yticks(np.arange(-1, 2.5, 0.25))
plt.show()