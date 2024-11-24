## lecture 10: Magnetic Properties of Materials

### 磁偶极子

磁偶极可以有多种形式，例如：

- 磁铁
- 带电流的线圈
- 旋转的带电体
- 亚原子粒子

我们暂时将磁偶极的产生建模为**电流环**，从而方便解释磁现象。

#### 磁偶极矩

定义带电流的线圈的磁偶极矩为：
$$\vec{\mu}=Ni\vec{A}$$
其中 $N$ 是线圈匝数，$i$ 是电流，$\vec{A}$ 是线圈的面积向量。

磁偶极子在磁场中会受到力矩，$\vec{\tau}=\vec{\mu}\times\vec{B}$. 设 $\theta$ 是磁偶极矩与磁场之间的夹角，则
$$\vec{\tau}=-\mu B\sin\theta=-\frac{\partial}{\partial\theta}(-\mu B\cos\theta)$$
因此，磁偶极矩在磁场中的能量为
$$U_B=-\vec{\mu}\cdot\vec{B}=-\mu B\cos\theta$$

#### 磁偶极子产生的磁场

考虑一段弧形导线在其圆心处产生的磁场：
$$\begin{align}
    d\vec{B}&=\frac{\mu_0}{4\pi}\frac{id\vec{s}\times\hat{r}}{R^2}\\
    &=\frac{\mu_0i\hat{B}}{4\pi R}d\phi\\
\end{align}$$
于是 $$B = \frac{\mu_0i\phi}{4\pi R}$$

对于一个圆环，其磁偶极矩为 $\mu = i\pi R^2$，因此其圆心处的磁场
$$B=\frac{\mu_0i}{2R}=\frac{\mu_0}{2\pi}\frac{\mu}{R^3}$$
可以猜想，与**电偶极子**类似，磁偶极子周围的磁场也按**三次方**衰减。我们计算中心轴线上的磁场来说明。

回忆一下，当距离足够远时，电偶极子在中心轴线上产生的电场可以**近似**为
$$\vec{E}=\frac{1}{2\pi\epsilon_0}\frac{\vec{p}}{z^3}$$
可以证明，磁偶极子中心轴线上的磁场为
$$B(z)=\frac{\mu_0}{2\pi}\frac{\mu}{(R^2+z^2)^{3/2}}$$
因而当 $z\gg R$ 时，近似为 $\frac{\mu_0}{2\pi}\frac{\mu}{z^3}$

### 磁性材料

磁性材料可以看作无数个磁偶极子组成的集合，他们相互作用，并对外界磁场产生响应，从而表现出不同的性质。

根据原子的磁偶极矩和原子间的相互作用，材料的磁性可以分为**顺磁性**、**抗磁性**和**铁磁性**等。

#### Paramagnetism

顺磁性材料在外磁场作用下，磁矩会与磁场对齐，从而增加材料的磁场。

我们定义磁化强度 $\vec{M}$ 为单位体积内的磁矩

#### Diamagnetism

顺磁材料总是被磁铁吸引，而抗磁材料在强磁场下会被磁铁排斥。

#### Ferromagnetism

铁磁性材料的特点是相邻原子间有很强的相互作用。
$$U=-J\,\Sigma\vec{\mu_i}\cdot\vec{\mu_j}-\Sigma\vec{\mu_i}\cdot\vec{B}$$
当 $J>0$ 时，原子间的相互作用使得当外磁场消失时，磁矩仍保持对齐，从而产生铁磁性。