## lecture 20: Polarization

我们用电场强度向量来表示电磁波的朝向，可以先固定 z，将电场方向分解为 x，y 两个方向来表示：
$$\begin{align}
\vec{E}_x(z, t) = \hat{i}E_{0x}\cos(kz - \omega t)\\
\vec{E}_y(z, t) = \hat{j}E_{0x}\cos(kz - \omega t + \epsilon)
\end{align}$$

### Linear polarization

当 $\epsilon=0$，即两个向量相位相同时，相当于线性叠加。
$$\vec{E} = \vec{E}_x + \vec{E}_y$$

### Circular polarization

当 $\epsilon=-\pi/2$ 时，可以写作
$$\vec{E}=E_0\left(\hat{i}\cos(kz-\omega t)+\hat{j}\sin(kz-\omega t)\right)$$
将 x 和 y 坐标的值分别看作在单位圆上旋转的点的投影，发现 $\vec{E}$ 的方向以 角速度 $\omega$ 旋转，时间上每个周期、空间上每个波长旋转 $2\pi$。  
对于观察者来说，看到的电场的旋转方向应当看作是**空间中一个定点**上，电场**随时间变化**的方向，所以对该例来说，观察者看到的是**顺时针**旋转，为**右旋光**。

同理，当 $\epsilon=\pi/2$ 时，$\sin$ 前多了个负号，观察者看到的是**逆时针**旋转，为**左旋光**。

**对着**光传播的方向观察，合成电矢量是顺时针方向旋转时，偏振是右旋的，反之是左旋的。

将相位、振幅相同的左右旋光叠加，就是线性光。

### Jones Vector

将电矢量写成列向量：
$$\vec{E} = \begin{bmatrix}E_x(t)\\E_y(t)\end{bmatrix} = \begin{bmatrix}E_{0x}\,e^{i(kz-\omega t+\phi_x)}\\E_{0y}\,e^{i(kz-\omega t+\phi_y)}\end{bmatrix}$$
我们可以把相位随时间和空间的变化分离出来简化计算，即
$$\vec{E} = \begin{bmatrix}E_{0x}\,e^{i\phi_x}\\E_{0y}\,e^{i\phi_y}\end{bmatrix}e^{i(kz-\omega t)}$$
我们重点关注这个列向量。之前我们都在实空间 $\mathbb{R}^2$ 上讨论，现在我们将使用在复数域 $\mathbb{C}$ 上扩张成的向量空间。  

对于这个二维向量，取他的两个基：
$$|H\rangle=\begin{pmatrix} 1\\0 \end{pmatrix},\quad |V\rangle=\begin{pmatrix} 0\\1 \end{pmatrix}$$
它们分别对应**水平**线性偏振光和**垂直**线性偏振光。

那么在复数域上，就可以由这两个基扩张成一个二维的复向量空间，但是其中一个分量是复数是什么意思呢？

设
$$|X\rangle=\begin{pmatrix} i\\0 \end{pmatrix}$$
这时候，使用复数的指数形式，我们发现
$$|X\rangle = \begin{pmatrix} i\\0 \end{pmatrix} = \begin{pmatrix} e^{i(\pi/2)}\\0 \end{pmatrix}$$
刚好相当于把 $E_x$ 的相位延迟了 $\pi/2$ ！  
因此，Jones vector 可以表示任意振幅、任意相位叠加形成的偏振光。比如：

@import "img/lec20/diag.png"

@import "img/lec20/circular.png"

另外，这还是一个内积空间，这里我们采用欧几里得内积（死去的线代还在追我），即
$$\langle A|B\rangle = \sum_{i=1}^n A_i\overline{B_i}$$
其中 $\overline{B_i}$ 是 $B_i$ 的共轭。那么很容易发现，
$$\langle H|V\rangle=\langle D|A\rangle=\langle R|L\rangle=0$$
即他们都是正交的。