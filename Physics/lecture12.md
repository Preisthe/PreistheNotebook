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

### 磁场的能量

对于 LR 电路，写出电动势的表达式
$$\varepsilon=L\frac{di}{dt}+Ri$$
两边乘上 $i$，得到
$$\varepsilon i=Li\frac{di}{dt}+i^2R$$
这个关系式可以看成能量守恒方程，即电动势做功的速率，等于磁场能增加的速率，加上电阻发热的速率。于是我们找到了包含磁场能量的方程：
$$\frac{dU_B}{dt}=Li\frac{di}{dt}=\frac{d}{dt}\left(\frac{1}{2}Li^2\right)$$
$$U_B=\frac{1}{2}Li^2$$

### 磁场的能量密度

根据对称性，螺线管内的磁场能一定均匀分布在 $Ah$ 体积内。
@import "img/lec12/solenoid.png"
则单位体积内的磁场能的表达式为
$$u_B=\frac{U_B}{Ah}=\frac{Li^2}{2Ah}$$
而 $\frac{L}{h}$ 就是单位长度的自感，即 $\mu_0n^2A$，于是
$$u_B=\frac{1}{2}\mu_0n^2i^2=\frac{B^2}{2\mu_0}$$

### 互感

@import "img/lec12/mutual.png"
设两个线圈，线圈 1 产生磁场 $B_1$，设线圈 2 上由于 $B_1$ 产生的磁通量为 $\Phi_{21}$，则
$$M_{21}=\frac{N_2\Phi_{21}}{i_1}$$
