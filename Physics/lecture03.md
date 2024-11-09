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
$$
\nabla=\frac{\partial}{\partial x} \hat{x} + \frac{\partial}{\partial y} \hat{x} + \frac{\partial}{\partial z} \hat{z}
$$
