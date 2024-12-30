## lecture 21: The Quantum Nature of Light

### Photoelectric Effect

懒得写了
$$\begin{align}
    E = hf = \hbar\omega\\
    hf=K+W
\end{align}$$
其中 $\hbar = \frac{h}{2\pi}$，称为约化普朗克常数  
$K$ 为逸出电子的动能  
$W$ 为逸出功（work function）

### Photons Have Momentum

光子的速度为 $c$，质量为 0，可以通过相对论计算光子的动量
$$\begin{align}
    E^2-c^2p^2 &= m^2c^4=0\\
    p = \frac{hf}{c} &= \frac{h}{\lambda} = \hbar k
\end{align}$$

### Compton Scattering

既然光子有能量，有动量，那么它与实物粒子作用时就有能量和动量的传递，就像碰撞一样。

将一束 X 光照到电子上，就会有大量光子与电子发生碰撞，光子会被撞向各个不同的方向，就发生了散射。

@import "img/lec21/angle.png"

我们也可以在相对论视角下进行计算：

@import "img/lec21/cal.png"

最终得到，散射光的波长与入射光波长之间差 $\Delta\lambda\equiv\lambda'-\lambda$ 为
$$\Delta\lambda = \frac{h}{mc}\left(1-\cos\phi\right)$$
其中 $\phi$ 为**光子**的散射角，$\theta$ 为**电子**的散射角。

$\theta$ 与 $\phi$ 之间的关系为
$$\tan\theta=\frac{\sin\phi}{\frac{\lambda'}{\lambda}-\cos\phi}$$
其中，$\frac{h}{mc}$ 称为康普顿波长（Compton Wavelength），相当于具有与电子的静止能量相当的光子的波长。

### Angular Momentum

在量子力学中，光子还有一个固有的自旋角动量，它要么是 $+\hbar$，要么是 $-\hbar$，其中符号分别代表**左旋**或**右旋**  
（左右旋的判断使用右手螺旋定则，光矢量在某一固定点旋转的角速度方向，若与传播方向一致，则自旋为正，即左旋）

每当带电粒子发射或吸收电磁辐射时，随着其能量和线动量的变化，它的角动量也会发生变化。

线性偏振光就可以看作是等量的左旋和右旋光子的叠加。
