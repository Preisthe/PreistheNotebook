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