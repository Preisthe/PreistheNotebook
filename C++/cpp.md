# C++

## 命名空间

相当于导入某个模块
例如：

```cpp
#include <iostream>
using namespace std;
```

就可以直接使用 `cout` 而不需要 `std::cout`
std 是标准模板库（STL）的命名空间
也可以指定某个函数或变量，如：

```cpp
using std::cout;
```

后续就可直接使用 cout.

## 变量

c++ 是静态类型语言

### 基本类型

增加了字符串类型

```cpp
std::string name = "Preisthe";
```

### 结构体

与 C语言中的类似

#### pair

c++ 中的特殊结构体，位于 std 命名空间中
pair 是一个模板，在声明时要指定两个成员的类型
使用时用 first 和 second 访问两个域

```cpp
std::pair<int, std::string> p1(1, "hello");
cout << p1.first << " " << p1.second;
// prints "1 hello"
```

- 使用 std::make_pair 快速创建 pair 对象
  - 可用于打包返回值
  - 无需声明类型

### auto

auto 关键字，用于编译时自动推导类型，可以省去写复杂类型声明的麻烦
常用于

- 函数返回值类型
- 接受 make_pair 返回的 pair 对象
- 循环变量

有点像 python 了
但不要过度使用，仅在类型名过长的时候使用

### 结构化绑定

使用方括号 `[]`
例：

```cpp
auto p = std::make_pair(“s”, 5);
auto [a, b] = p;
// a is string, b is int
// auto [a, b] = std::make_pair(...);
```

就是解包，也适用于结构体，很像 python，但*不能嵌套*

用于循环：

```cpp
void shift(vector<std::pair<int, int>>& nums) {
    for (auto& [num1, num2]: nums) {
        num1++;
        num2++;
    }
}
```

直接迭代序列中的元素，很像 python 的 `for item in seq`
且上例中的变量都是**引用**（ python 貌似做不到 ）

### 变量初始化

- 统一初始化：使用花括号 `{}`
  - 结构体：`Student s = {"Sarah", "CA", 21};`
  - 向量：`std::vector<int> v{1, 2, 3};`
  - 基本类型：`int x{5};`
  - *注意区分初始化的花括号和 make_pair 的圆括号*
- std::initializer_list
  - `std::vector<int> vec(3, 5); // 3 个 5`

### 引用

使用 `&` 符号，相当于对变量取别名，常用于函数传参，相当于直接自动指针了。例：

```cpp
void changeX(int& x){ // changes to x will persist
    x = 0;
}
```

`&` 参与构建了一种新的变量类型，将当前变量与被引用变量绑定，可以对任何类型使用
*注意*："=" 仅产生值传递，只有加上 `&` 才是引用

#### 常见错误

```cpp
void shift(vector<std::pair<int, int>>& nums) { // 函数声明中是引用
    for (size_t i = 0; i < nums.size(); ++i) {
        auto [num1, num2] = nums[i]; // 但解包出来的变量不是引用
        num1++;
        num2++;
    }
}
```

使用 auto& 避免

### std::vector

动态数组

#### 基本操作

- `v.size()` 返回大小
- `v.push_back(x)` 在末尾添加元素
- `v[i] = k` 访问元素
- `v.empty()` 判断是否为空
- `v.clear()` 清空

## 函数

### 函数重载

函数名相同，参数不同（参数类型不同或参数个数不同），增加了函数名使用的方便性
例：

```cpp
int half(int x, int divisor = 2) { // (1)
return x / divisor;
}
double half(double x) { // (2)
return x / 2;
}
half(4)// uses version (1), returns 2
half(3, 3)// uses version (1), returns 1
half(3.0) // uses version (2), returns 1.5
```

同时，*c++ 引入了函数默认参数*
