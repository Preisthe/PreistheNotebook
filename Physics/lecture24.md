## lecture 24: Quantum Wells

本章的要点是通过与**驻波**进行类比，探究在某些限制条件存在的情况下薛定谔方程的解。

### 无限深势阱

@import "img/lec24/inf.png"
类似于驻波在两端振幅为 0 的限制条件，在无限深势阱中，我们可以解出电子位于某处的概率为：
$$p_n(x)=\left|\psi(x)\right|^2=|A|^2\sin^2\left(\frac{n\pi}{L}x\right)$$
其中常数 $A$ 可以通过归一化条件确定：
$$\int_{-\infty}^{\infty}|\psi_n(x)|^2dx=\int_0^L|\psi_n(x)|^2dx=1$$
通过简单的积分可以得到
$$A=\sqrt{\frac{2}{L}}$$

### 能级

不考虑相对论效应，我们也可以算出不同 n 对应的电子的能量。

由于势能为 0，所以电子的能量就等于动能：
$$\begin{align}
    E_n&=K=\frac{p^2}{2m}\\
    &=\left(\frac{h^2}{8mL^2}\right)n^2
\end{align}$$
$n=1$ 时能量最低，称为基态。也就是说，任何受约束的量子体系，其最低能量总是存在的，称为零点能量。

电子吸收或发射光子，就会发生能级跃迁，这个变化是离散的。

但是单一的解并不满足 $\psi_n(0)=\psi_n(L)=0$ 的限制条件：
$$\psi_n(x)=e^{i\frac{n\pi}{L}x}\ or\ \psi_n(x)=e^{-i\frac{n\pi}{L}x}$$
我们仍然需要将各种情况线性组合来得到最终的解。而且当 $n$ 充分大时，概率几乎均匀分布，即**当量子数足够大时，量子力学的解就与经典力学非常相似**。

### 有限深势阱

对于有限深势阱，波函数可能穿透势壁，驻波的形式不再适用。

***仅作定性分析***

@import "img/lec24/finite.png"

因此有限深势阱的解的波长要大一些，因此能量就要低一些。

而那些本身能量就比势壁高的电子来说，它们并不受势阱约束，因而可以具有连续的能量。

@import "img/lec24/energy.png"

### 高维薛定谔方程

把薛定谔方程推广到二维：
$$E\Psi(x, y)=-\frac{\hbar^2}{2m}\left(\frac{\partial^2}{\partial x^2}+\frac{\partial^2}{\partial y^2}\right)\Psi(x, y)$$
对于满足 $\Psi(x,y)=X(x)Y(y)$ 的波函数，薛定谔方程等价于
$$E=-\frac{\hbar^2}{2m}\frac{1}{X(x)}\frac{\partial^2X(x)}{\partial x^2}-\frac{\hbar^2}{2m}\frac{1}{Y(y)}\frac{\partial^2Y(y)}{\partial y^2}$$
它有着 $E=F(x)+G(y)$ 的形式，而且二者必须都为常数。这样就可以分解为两个常微分方程。

一般来说，当
$$U(x,y)=U_x(x)+U_y(y)$$
或者极坐标系中
$$U(r,\theta,\phi)=V(r)$$
时可以这样搞。

#### 高维无限深势阱

##### 二维

$$\begin{align}
    \psi_n(x,y)&=\frac{2}{\sqrt{L_xL_y}}\sin\left(\frac{n_x\pi}{L_x}x\right)\sin\left(\frac{n_y\pi}{L_y}y\right)\\
    E_n&=\frac{h^2}{8m}\left(\frac{n_x^2}{L_x^2}+\frac{n_y^2}{L_y^2}\right)
\end{align}$$

##### 三维

$$\begin{align}
    \psi_n(x,y,z)&=\sqrt{\frac{8}{V}}\sin\left(\frac{n_x\pi}{L_x}x\right)\sin\left(\frac{n_y\pi}{L_y}y\right)\sin\left(\frac{n_z\pi}{L_z}z\right)\\
    E_n&=\frac{h^2}{8m}\left(\frac{n_x^2}{L_x^2}+\frac{n_y^2}{L_y^2}+\frac{n_z^2}{L_z^2}\right)
\end{align}$$