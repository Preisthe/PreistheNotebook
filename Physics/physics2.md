# General Physics II

## lecture 01: Coulomb’s Law and the Electric Field

### 电荷

电荷是量子化的，元电荷 $e=1.602\times 10^{-19}C$.
$C$: 库仑，电荷单位
电子质量：$9.109\times 10^{-31}kg$

电荷守恒定律：电荷不能凭空产生或消失
电荷在洛伦兹变换下保持不变，即没有相对论效应
密立根油滴实验测量了元电荷

### 库仑定律

描述了两个点电荷之间的相互作用力，与距离的平方成反比，与电荷的乘积成正比
标量形式：$F=k\frac{q_1q_2}{r^2}$
向量形式：$\vec{F}=k\frac{q_1q_2}{r^2}\hat{r}$
其中 $k=\frac{1}{4\pi\epsilon_0}$，$\epsilon_0=8.85\times 10^{-12}F/m$ 是真空介电常数

### 电场

电场是**向量场**， $\vec{E}(x, y, z)$
定义某点的电场强度为**试探电荷**在该点受到的力与电荷的比值
$$\vec{E}=\vec{F}/q_0$$
则根据库仑定律，点电荷产生的电场为
$$\vec{E}=\frac{kq}{r^2}\hat{r}$$

#### 电场线

是一种假想的，用来表示电场分布的线，电场线从正电荷出发，指向负电荷，密集处电场强，稀疏处电场弱

### 电偶极子

两个等量异号的点电荷组成的系统
用**电偶极矩**描述电偶极子的特性：
$$\vec{p}=q\vec{d}$$
其中 $\vec{d}$ 代表两个电荷之间的距离向量，从负电荷指向正电荷

#### 电偶极子产生的电场

电荷连线轴上（标量形式）：
$$E=\frac{q}{4\pi\epsilon_0(z-\frac{1}{2}d)^2} - \frac{q}{4\pi\epsilon_0(z+\frac{1}{2}d)^2}$$
对于 $z\gg d$，可以近似为
$$E=\frac{1}{2\pi\epsilon_0}\frac{p}{z^3}$$

#### 电偶极子受到的力矩

由于电荷等量异号，电偶极子受到的合力为 0，但力矩不为 0
@import "img/lec1/electricDipole.png"
$$\vec{\tau}=\vec{p}\times\vec{E}$$
倾向于将电偶极子转到与电场方向一致

## lecture 02: Continuous Charge and Gauss’ Law

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

## lecture 03: The Electrostatic Potential

基本概念高中都学过了，主要就是 $U=dE$，但是大学里常用 $V$ 表示**电势**，用 $U$ 表示**势能**

### 电势能 $U$

选定 0 势能点（一般为无穷远处），则某点的电势能定义为：将电荷从该点移动到 0 势能点的过程中，电场力所做的功

### 电势 $V$

定义为单位电荷所带的电势能：$$V=\frac{U}{q}$$
两点之间的电势差（**注意负号**）：
$$V=-\int_i^f \vec{E}\cdot d\vec{s}$$

- 电场指向电势差**减小最快**的方向
- 电势是标量，叠加时遵循标量相加

### 等势面

- 在等势面上移动电荷不做功
- 电场线垂直于等势面

### 常见电势的计算

#### 点电荷周围的电势

$$V = -\int_{\infty}^{\vec{r}}\vec{E}\cdot d\vec{s}
    = \frac{1}{4\pi\epsilon_0}\frac{q}{r}$$
可以看出电势的正负与电性有关

#### 电偶极子周围的电势

@import "img/lec3/dipole.png"

$$V=V_{(+)}+V_{(-)}=\frac{q}{4\pi\epsilon_0}\frac{r_{(-)}-r_{(+)}}{r_{(-)}r_{(+)}}$$
当 $r\gg d$ 时，
$$
\begin{align}
r_{(-)}-r_{(+)}&\approx d\cos\theta\\
r_{(-)}r_{(+)}&\approx r^2
\end{align}
$$ 所以
$$V=\frac{1}{4\pi\epsilon_0}\frac{p\cos\theta}{r^2}=\frac{1}{4\pi\epsilon_0}\frac{\vec{p}\cdot\vec{r}}{r^3}$$
其中 $\vec{p}=q\vec{d}$ 为电偶极矩

#### 均匀带电细棒周围的电势

这里仅考虑两端的点，设细棒带正电
@import "img/lec3/rod.png"
这个积分有点麻烦，最好背一下
@import "img/lec3/integral.png"

于是我们得到了在 $x=0$ 时，P 点的电势关于 $d$ （P 与棒的距离）的表达式，现在我们将他与之前利用高斯定理得到的无限长带电直线产生的电场 $E=\frac{\lambda}{2\pi\epsilon_0r}$ 联系起来：
- 先把距离 $d$ 的符号改为 $r$
$$V_P=\frac{\lambda}{4\pi\epsilon_0}\ln\left(\frac{L+\sqrt{L^2+r^2}}{r}\right)$$
- 对 P 点电势求 $L\to\infty$ 的极限
  - ~~不对啊怎么是正无穷~~
- 先对 P 点电势求负导数，经过一通计算
$$E_P=-\frac{dV_P}{dr}=\frac{\lambda}{4\pi\epsilon_0}\left(\frac{1}{r}-\frac{r}{\sqrt{L^2+r^2}\left(L+\sqrt{L^2+r^2}\right)}\right)$$
- 即 P 点电场强度的垂直分量，然后取 $L\to\infty$ 的极限
$$\lim_{L\to\infty}E_P=\frac{\lambda}{4\pi\epsilon_0r}$$
这个结果是合理的，因为现在讨论的是含端点的无限长**射线**的情况，如果考虑无限长**直线**，则应该将次结果**乘以 2**，那么就得到了与之前一致的结果。

#### 均匀带电圆盘产生的电势

设圆盘半径为 $R$ ，电荷面密度为 $\sigma$，考虑中心轴线上距圆盘 $z$ 处
将圆盘分割成无数个圆环进行积分，设圆环半径为 $R'$ ，厚度为 $dR'$ ，则
$$dq=\sigma (2\pi R')dR',\ r=\sqrt{R'^2+z^2}$$
从 0 到 R 积分，这个也是幂函数
$$\begin{align}
V&=\int_0^R\frac{1}{4\pi\epsilon_0}\frac{dq}{r}\\
&=\frac{\sigma}{2\epsilon_0}\int_0^R\frac{R'dR'}{\sqrt{R'^2+z^2}}\\
&=\frac{\sigma}{2\epsilon_0}\left(\sqrt{R^2+z^2}-z\right)
\end{align}$$
此结果可与[均匀带电圆盘产生的电场](#均匀带电圆盘产生的电场)联系起来
@import "img/lec3/Ez.png"{width=90%}

### 电势与电场的关系

不难发现，电势关于距离的导数就是某个方向上的电场强度
在三维空间中，将三个方向总结起来，就得到了
$$\vec{E}=-\nabla V$$
其中 $\nabla$ 为梯度算子，$\nabla V$ 即电势的梯度
