## lecture 12: Inductors and Inductance

### 自感

定义螺线管的自感为：
$$L=N\Phi_B/i$$
于是，自感就是对单位电流产生的**磁链**（$N\Phi_B$）的量度。单位为 $\textrm{H}$（亨利）。则
$$L=\frac{(nl)(\mu_0inA)}{i}=\mu_0n^2lA$$
那么单位长度上的自感就等于
$$\frac{L}{l}=\mu_0n^2A$$
所以自感只取决于线圈的几何结构，而与电流无关。设螺线管的长度 $l$ 远远大于半径，这个螺线管的自感就可以近似为（忽略了边缘效应）
$$L=\mu_0n^2lA=N^2(\mu_0A/l)$$

当电流变化时，线圈会产生**自感电动势**
$$\varepsilon_L=-L\frac{di}{dt}$$

### 互感

@import "img/lec12/mutual.png"
设两个线圈，线圈 1 产生磁场 $B_1$，设线圈 2 上由于 $B_1$ 产生的磁通量为 $\Phi_{21}$，则
$$M_{21}=\frac{N_2\Phi_{21}}{i_1}$$
