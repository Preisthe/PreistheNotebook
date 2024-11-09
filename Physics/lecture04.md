## lecture 04: The Triangle of Electrostatics

本节揭示了电场、电势和电荷分布三者之间的关系
@import "img/lec4/triangle.png"

### 静电场是电势的负梯度

梯度指向电势**增加最快**的方向，所以电场是**负**梯度
$$\vec{E}=-\nabla V$$

### 静电场的旋度为 0

#### 旋度

对于任意向量场 $\vec{v}$ ，其旋度定义为
$$\nabla\times\vec{v}
=\left|\begin{matrix}
\hat{x} & \hat{y} & \hat{z} \\
\frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\
v_x & v_y & v_z
\end{matrix}\right|$$ $$=\hat{x}\left(\frac{\partial v_z}{\partial y}-\frac{\partial v_y}{\partial z}\right)+\hat{y}\left(\frac{\partial v_x}{\partial z}-\frac{\partial v_z}{\partial x}\right)+\hat{z}\left(\frac{\partial v_y}{\partial x}-\frac{\partial v_x}{\partial y}\right)$$
旋度的几何意义顾名思义，就是一点周围旋转的趋势。

#### 静电场的旋度

对于静电场 $\vec{E}$，设 $\vec{v}=-\vec{E}$，则

$$\vec{v}=\nabla\phi=\frac{\partial\phi}{\partial x}\hat{x}+\frac{\partial\phi}{\partial y}\hat{y}+\frac{\partial\phi}{\partial z}\hat{z}$$

对于 x 分量，

$$\left(\nabla\times\vec{v}\right)_x=\frac{\partial v_z}{\partial y}-\frac{\partial v_y}{\partial z}=\frac{\partial}{\partial y}\frac{\partial\phi}{\partial z}-\frac{\partial}{\partial z}\frac{\partial\phi}{\partial y}=0$$

可以看到，任意梯度的旋度都是 0，即对于任意解析的函数 $\phi$ ，都有 $\nabla\times\left(\nabla\phi\right)=0$，所以

$$\nabla\times\vec{E}=0$$

#### 静电力是保守力

**只对“静电场”成立！**

实际上静电场旋度为 0 还暗示了静电力是保守力，这一点可以通过 Stokes 定理联系起来。Stokes 定理，又称旋度定理，揭示了曲面积分与曲线积分之间的关系，
$$\oint_C\vec{v}\cdot d\vec{l}=\int_S(\nabla\times\vec{v})\cdot d\vec{A}$$
那么对于静电场，左边是电场在某一环路上的积分 $\oint_C\vec{E}\cdot d\vec{l}$，对任意闭合曲线恒等于零，于是就得到了右边恒等于零。

**坑**

Stokes 定理的前提条件是所积区域是单连通分量，即没有“洞”，如果区域某点没有定义也不能使用
@import "img/lec4/hole.png"

### 高斯定理的微分形式

我们定义 $\rho(\vec{r})$ 为空间中一点 $\vec{r}$ 处的电荷密度，即取空间中一块极小的体积，
$$\rho(\vec{r})=\lim_{\Delta V\to 0}\frac{q_{enc}^{\Delta V}}{\Delta V}$$
对这块空间边界上的曲面应用高斯定理，则

@import "img/lec4/gauss.png"

现在来计算等式最右边的曲面积分，假设取到的小体积是长方体，且 $\Delta V=\Delta x\Delta y\Delta z$

@import "img/lec4/cube.png"

在 $x \pm \Delta x/2$ 范围内，直接计算前后两个面的曲面积分，就可以得到这个值是 $(\partial E_x/\partial x)\Delta V$
同理可得另外两个方向上的积分，所以
$$\frac{\rho(\vec{r})}{\epsilon_0}=\left(\frac{\partial E_x}{\partial x}+\frac{\partial E_y}{\partial y}+\frac{\partial E_z}{\partial z}\right)\equiv\nabla\cdot\vec{E}$$

这就是高斯定理的微分形式，右边的表达式称为**散度**（divergence），表示一个向量场在某一点向外发散的趋势。所以高斯定理就显得很直观了，因为电场线从正电荷出，向负电荷进，所以某点的电荷密度就表征了电场线向外发散的程度。

#### 拓展：高斯定理与高斯公式

高斯公式是高斯定理的**推广**，高斯定理是高斯公式在静电学中的**特例**。  
高斯公式揭示了面积分与体积分之间的关系，又称**散度定理**，直观来讲，一块闭合空间的边界上某个量有多少流入流出，就等于空间内部该量的增减。

让我们沿用之前的假设，
@import "img/lec4/gauss.png"
这一次我们从右边出发，那么就得到了小体积的散度等于小长方体六个面上的积分，然后将大量小体积累积起来，发现相邻小体积边界上的面积分相互**抵消**了，最后只剩下整个区域**边界**上的面积分，这就是高斯公式。
$$\oint_S\vec{v}\cdot d\vec{A}=\int_V(\nabla\cdot\vec{v})dV$$

#### Poisson's Equation

把高斯定理的微分形式与电场和电势的关系结合起来，就得到了
$$\nabla^2V\equiv\nabla\cdot\nabla V=-\frac{\rho}{\epsilon_0}$$
