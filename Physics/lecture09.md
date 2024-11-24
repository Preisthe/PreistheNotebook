## lecture 09: Magnetic Field of a Current

静止的电荷产生恒定电场，属于**静电学**。  
与之相应的，恒定的电流产生恒定的磁场，称作**静磁学**。

### Biot-Savart Law

与库仑定律类似：
$$d\vec{B}=\frac{\mu_0}{4\pi}\frac{id\vec{s}\times\vec{r}}{r^3}$$
其中，$\vec{r}$ 是从电流元到观察点的距离，$id\vec{s}$ 是电流元，$\mu_0=4\pi\times10^{-7}\ T\cdot m/A$ 称作真空磁导率。

### 无限长直导线周围的磁场

@import "img/lec9/long.png"

$$\begin{align}
    d\vec{B}&=\frac{\mu_0}{4\pi}\frac{i\,d\vec{s}\times\vec{r}}{r^3}\\
    &=\frac{\mu_0}{4\pi}\frac{ids\cdot R}{r^3}\hat{n}\\
\end{align}$$
省略一些计算
$$B = \frac{\mu_0 i}{2\pi R}$$

### 安培环路定律

$$\oint\vec{B}\cdot d\vec{s}=\mu_0 i_{enc}$$

### 螺线管中的磁场

我们假设螺线管的半径远小于螺线管的长度，且线圈缠绕紧密，那么**螺线管中的磁场恒定，且螺线管外磁场为 0**.
@import "img/lec9/solenoid.png"
根据安培环路定律：
$$\begin{align}
    Bh &= \mu_0inh\\
    B &= \mu_0in
\end{align}$$
其中，$n$ 是螺线管单位长度上的匝数

### 磁场的旋度

应用 Stokes 定理（见 lec4），可以得到
$$\int_S(\nabla\times\vec{B})\cdot\vec{A}=\oint\vec{B}\cdot d\vec{s}=\mu_0i_{enc}=\mu_0\int_S\vec{J}\cdot d\vec{A}$$
$$\nabla\times\vec{B}=\mu_0\vec{J}$$
这是安培环路定律的微分形式