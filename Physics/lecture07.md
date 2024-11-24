## lecture 07: DC Circuits

### 电容器存储的能量

$$dU=V'dq'=(q'/C)dq'$$
$$U=\int_0^q dU=\int_0^q (q'/C)dq'=\frac{q^2}{2C}=\frac{1}{2}CV^2$$

### RC 电路

根据能量守恒，电容器增加的能量来自于电动势的做功减去电阻的发热
$$\frac{dU}{dt}=\frac{q}{C}\frac{dq}{dt}=i\epsilon-i^2R$$
$i=dq/dt$，所以
$$R\frac{dq}{dt}+\frac{q}{C}=\epsilon$$
该式也可根据欧姆定律得到

然后解一下小学二年级就学过的微分方程，通过变量分离，可以解出
$$q=C\epsilon(1-e^{-\frac{t}{RC}})$$
其中，$\tau=RC$ 被称作充电时间常数
$$i=\frac{dq}{dt}=\left(\frac{\epsilon}{R}\right)e^{-t/\tau}$$

### 电场的能量密度

考虑平行板电容器，其中 $C=\epsilon_0 A/d$， $V=Ed$，则电容储存的能量为
$$U=\frac{1}{2}CV^2=\frac{1}{2}\epsilon_0 E^2(Ad)$$
定义能量密度 $u$，即极板间单位体积所包含的电势能，那么在这里 $u$ 就是定值
$$u=\frac{1}{2}\epsilon_0E^2$$
**这个结论对任意电场成立**。也就是说，平行板电容器存储的电势能可以看作是板间电场所蕴含的能量。

### 电介质

电介质可以是任何绝缘材料，可以用于填充平行板电容器中的空隙，从而增大电容。

对于静电荷，电介质虽然不导电，但也会感应出感应电荷，从而削减电场强度，进而降低极板间的电势差。

#### 相对介电常数

将电介质插入平行板导致电容增大的系数 $\kappa$，就被称为该材料的相对介电常数。任意材料 $\kappa\ge1$.

对于任意静电学方程，如果空间被某种材料所填充而不是真空，那么真空介电常数 $\epsilon_0$ 就要修正为 $\epsilon=\kappa\epsilon_0$，称为材料的介电常数

例如，高斯定理修正为
$$\epsilon_0\oint \kappa\vec{E}\cdot d\vec{A}=q$$
