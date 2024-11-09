## lecture 02: Continuous Charge and Gauss' Law

### 均匀带电圆环产生的电场

设圆环半径为 $R$，电荷密度为 $\lambda$，则圆环中心轴线上距离圆环距离为 $z$ 处的电场为
$$E_z=\frac{qz}{4\pi\epsilon_0(z^2+R^2)^{3/2}}$$
其中 $q=\lambda\cdot 2\pi R$  
当 $z\gg R$ 时，还可以近似为 $$E=\frac{1}{4\pi\epsilon_0}\frac{q}{z^2}$$
这意味着当距离足够远时，圆环也可以近似看成点电荷

### 均匀带电圆盘产生的电场

设圆盘半径为 $R$，电荷密度为 $\sigma$，则圆盘中心轴线上距离圆盘距离为 $z$ 处的电场为：  
把圆盘看成一系列半径从小到大圆环的积分
$$\begin{align}
dE_z&=\frac{\sigma(2\pi rdr)z}{4\pi\epsilon_0(z^2+r^2)^{3/2}}\\
E_z=\int_0^R dE_z&=\frac{\sigma}{2\epsilon_0}\left[1-\frac{z}{(z^2+R^2)^{1/2}}\right]
\end{align}$$
这个还挺好积的，就是幂函数积分

### Gauss 定理

#### 电通量

电通量描述了穿过一个曲面的电场线的数量，定义为**电场**与**面积元**点积的积分：
$$\Phi=\int\vec{E}\cdot d\vec{A}$$

#### 高斯定理（真空中）

高斯定理描述了穿过高斯面的净电通量与曲面所包含的电荷的关系  
取闭合曲面作为高斯曲面，曲面上面积元的方向为**向外**，则高斯定理为：
$$\epsilon_0\oint\vec{E}\cdot d\vec{A}=q_{enc}$$ 即
$$\epsilon_0 \Phi = q_{enc}$$

#### 与库仑定律的关系

库仑定律是高斯定理的特例，即当高斯面是一个半径为 $r$ 的球面，所包含电荷为位于球心的点电荷时，由于对称性，高斯面上电场强度大小处处相等，且方向都垂直于高斯面
$$\begin{align}
q &= \epsilon_0 \oint \vec{E} \cdot d\vec{A} = \epsilon_0 E \oint dA\\
E &= \frac{q}{\epsilon_0} \frac{1}{4\pi r^2} = \frac{1}{4\pi\epsilon_0}\frac{q}{r^2}
\end{align}$$
所以库仑定律中的 $4\pi$ 仅仅是一个几何系数，与 $\epsilon_0$ 无关

#### 高斯定理的应用

##### 均匀带电球体内部的电场

在带电球体内部距球心距离为 $r$ 处，取一个半径为 $r$ 的球面作为高斯面

- 由于电荷均匀分布，所以 $q'=q\left(r/R\right)^3$
- 且高斯面外电荷产生的电场为 0

所以
$$\vec{E}=\left(\frac{q}{4\pi\epsilon_0R^3}\right)\vec{r}$$
与 $r$ 成正比

##### 无限大均匀带电平面

在两侧都会产生匀强电场
$$E = \frac{\sigma}{2\epsilon_0}$$
即 [均匀带电圆盘产生的电场](#均匀带电圆盘产生的电场) 在 $R\to\infty$ 时的极限  
常用于**近似**有限带电**绝缘**薄板产生的电场

##### 无限长带电直线

设电荷线密度为 $\lambda$ ，取半径为 $r$ 的圆柱面作为高斯面
$$E = \frac{\lambda}{2\pi\epsilon_0r}$$
方向与电性有关  
常用于**近似**有限带电直线产生的电场
