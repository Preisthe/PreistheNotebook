## lecture 14: Maxwell's Equations and EM Waves

### 过去的章节

在之前的讨论中，电磁学的四大天王是这样的：

@import "img/lec14/legacy.png"

他们分别描述了电场和磁场的散度、旋度

#### 然而，这里竟然藏着一个巨大的漏洞！

我们对**法拉第电磁感应定律**两边求散度
$$\nabla\cdot\left(\nabla\times\vec{E}\right)=\nabla\cdot\left(-\frac{\partial\vec{B}}{\partial t}\right)=-\frac{\partial}{\partial t}\left(\nabla\cdot\vec{B}\right)$$
由于磁场的散度恒为 0，所以上式也理应恒等于 0.
事实上**旋度的散度为 0** 也是一个数学恒等式。

然而，当我们对**安培环路定理**做同样的操作时
$$\nabla\cdot\left(\nabla\times\vec{B}\right)=\nabla\cdot\left(\mu_0\vec{J}\right)=\mu_0(\nabla\cdot\vec{J})$$
问题出现了，右边却并不恒等于 0！

进一步，应用连续性方程 $\nabla\cdot\vec{J}=-\frac{\partial\rho}{\partial t}$ 和高斯定理，得到
$$\nabla\cdot(\nabla\times\vec{B})=-\mu_0\frac{\partial\rho}{\partial t}=-\mu_0\frac{\partial(\epsilon_0\nabla\cdot\vec{E})}{\partial t}=-\nabla\cdot\left(\mu_0\epsilon_0\frac{\partial\vec{E}}{\partial t}\right)$$
于是，那个男人说，只要把安培环路定理小修一下：
$$\nabla\times\vec{B}=\mu_0\vec{J}+\mu_0\epsilon_0\frac{\partial\vec{E}}{\partial t}$$
称为**全电流定律**。其中，
$$\vec{J}_d=\epsilon_0\frac{\partial\vec{E}}{\partial t}$$
称为**位移电流**（displacement current）

#### 然后就把这个问题优美的解决了

麦克斯韦的修正还体现了一个非常巧妙的对称性，即正如变化的磁场产生电场，**变化的电场也能产生磁场**。

安培环路定理修正后的**全电流定律**的积分形式：
$$\oint_C\vec{B}\cdot d\vec{s}=\mu_0(i_{enc}+\int_S\vec{J}_d\cdot d\vec{A})$$
我们可以直观地来认识一下**位移电流**

@import "img/lec14/amp.png"

如图所示，导线接在电容器上，此时电容正在充电。给定**安培环路** C（导线周围那一圈），我们应当可以选择任意被 C 所包含的曲面计算电流，并得出相同的结论。

- 取环路 C 所在平面，则通过曲面的电流等于导线上的电流。
- 现在把曲面向左拉开，将其拉出导线与右侧极板，此时该曲面不与任何导线相交，所以通过曲面的电流为 0。但确有电场穿过该曲面，并发生了变化，所以位移电流不为 0，且等于导线上的电流。

位移电流相当于一种假想的电流，它穿过电容器，延续了导线上的电流。

### 现在让我们正式介绍一下麦克斯韦方程组

我们从两方面完整描述电磁学：

- 电荷产生场
- 场影响电荷

@import "img/lec14/maxwell.png"

现在你满意了吧？

#### 磁荷

// TODO:

### 电磁波

#### 波动方程

在一块没有电荷或电流的空间，麦克斯韦方程组化为

@import "img/lec14/equation.png"

它们形成了 E 和 B 的一组耦合一阶偏微分方程。我们通过计算旋度的旋度化简

@import "img/lec14/decouple.png" {width="80%"}

再对 nabla 算子应用一下向量三重积
$$\nabla\times(\nabla\times\vec{C})=\nabla(\nabla\cdot\vec{C})-\nabla^2\vec{C}$$
其中 $\nabla^2\vec{C}$ 是拉普拉斯算子，$\nabla^2=\nabla\cdot\nabla$

两个高斯定理告诉我们，真空中 $\nabla\cdot\vec{E}=0$，$\nabla\cdot\vec{B}=0$，所以
$$\nabla^2\vec{E}=\mu_0\epsilon_0\frac{\partial^2\vec{E}}{\partial t^2},\quad \nabla^2\vec{B}=\mu_0\epsilon_0\frac{\partial^2\vec{B}}{\partial t^2}$$
这意味着 $\vec{E}$ 和 $\vec{B}$ 在空间中的每个笛卡尔分量都满足波动方程
$$\frac{\partial^2 f}{\partial t^2}=c^2\nabla^2 f$$
于是我们发现，所有电磁波的速度都等于
$$c=\frac{1}{\sqrt{\mu_0\epsilon_0}}\approx 3.00\times 10^8 m/s$$

#### 电磁波的传播

变化的磁场激发了垂直的电场，变化的电场激发了垂直的磁场，如此往复，形成电磁波。

我们关注平面波方程
$$f(x,t)=Acos(kx-\omega t+\phi)$$
其中 $k$ 是波数，$\omega$ 是角频率，且
$$\lambda=\frac{2\pi}{k},\quad T=\frac{2\pi}{\omega}$$
现在我们利用小学二年级就学过的波动方程的解，写出电场和磁场的一组解
$$\vec{E}=\vec{E}_m cos(kx-\omega t+\phi),\quad \vec{B}=\vec{B}_m cos(kx-\omega t+\phi)$$
再根据 $\frac{\partial^2 f}{\partial t^2}=c^2\nabla^2 f$，所以一定有 $\omega^2=c^2k^2$，或 $\omega=ck$。

此外，麦克斯韦方程组对 $\vec{E}$ 和 $\vec{B}$ 还有额外的限制。我们可以推导出以下性质：

##### 1. 横波

计算电场的散度
$$\nabla\cdot\vec{E}(x,t)=-k\hat{x}\cdot\vec{E}_m\sin(kx-\omega t+\phi)$$
由高斯定理，$\nabla\cdot\vec{E}=0$, $\nabla\cdot\vec{B}=0$,
所以 $(\vec{E}_m)_x=(\vec{B}_m)_x=0$，这说明电磁波是**横波**。

##### 2. 电场和磁场的方向

计算电场的旋度和磁场关于时间的导数
$$\begin{align}
  \nabla\times\vec{E}(x,t)&=-k\hat{x}\times\vec{E}_m\sin(kx-\omega t+\phi)\\
  \frac{\partial}{\partial t}\vec{B}(x,t)&=\omega\vec{B}_m\sin(kx-\omega t+\phi)
\end{align}
$$
根据法拉第电磁感应定律 $\nabla\times\vec{E}=-\frac{\partial\vec{B}}{\partial t}$，得到
$$-k\hat{x}\times\vec{E}_m=-\omega\vec{B}_m$$
更普遍的，对于传播方向 $\hat{k}$，
$$\vec{B}=\frac{1}{c}(\hat{k}\times\vec{E})$$

@import "img/lec14/wave.png"

- 电场和磁场相互垂直
- 利用 $\vec{E}\times\vec{B}$ 可以得到电磁波的传播方向

#### 电磁波的产生：开放电容

@import "img/lec14/gen.png"

*antenna: 天线

#### 电磁波的能量

// TODO:
