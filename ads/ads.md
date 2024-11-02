# 高级数据结构与算法分析

## 1. AVL Trees, Splay Trees, and Amortized Analysis

### AVL 树

就是不停的转，要额外存一个树高或者**平衡因子**，所以**空间开销**总是比 Splay Tree 大。

- 平衡因子 = 左 - 右

#### 插入

- Trouble maker 总是找最近的 Trouble finder 解决

@import "img/1/avl_ins_1.png"

    注意到这种方法使(原) Mar 子树的高跟插入前保持一致

- 扭着不平衡的话，要下探两个孩子节点

@import "img/1/avl_ins_2.png"

    注意到这样使 B 子树的高跟插入前保持一致

插入时查找消耗 $O(\log N)$ 时间，旋转消耗 $O(1)$

#### 删除

AVL 删除最坏**旋转**次数是 $O(\log N)$ 的，因为某些情况下，不能保证解决问题的子树树高不变，导致可能递归到根

#### 最小节点数

与斐波那契数列有紧密关系
定义空树树高为 -1

@import "img/1/avl_min.png"

结论： $n_h = F_{h+2} - 1$

### Splay Trees

每次查询一个节点的时候，就把他转到根上

- **Case1**: 父节点是根
    直接转
- **Case2**: 两种
    @import "img/1/splay.png"

#### 均摊 $O(\log N)$ 原因

Splaying not only moves the accessed node to the root, but also roughly halves the depth of most nodes on the path.

### 均摊开销

定义势能函数为 均摊开销 - 实际开销

@import "img/1/potential.png"

在设计时，$\hat{c}_i$ 应当易于计算 n 次连续操作复杂度，从而控制 $\Sigma c_i$ 的上界

@import "img/1/amotized.png"

上图中的势能差不一定要大于 0，只要挪到左边后，仍然可被 $\Sigma_{i=1}^n \hat{c_i}$ 控制即可
