## Numpy—ndarry对象

### Numpy的导入
- 函数库的导入`import numpy as np`
- 二个基本对象：
    - ndarray：数组，存储单一数据类型的多维数组
    - ufunc：能够对数组处理的函数
### 创建数组
#### array函数
- 在IPython中输入函数名并添加一个‘？’显示就可以显示文档内容。例如：`np.array?`
- 通过array函数创建数组
    - `a = np.array(paras)`： 通过array函数创建，其中paras可以为list/tuple/多维list
    - `a.dtype`：获取数组内的元素的类型
    - `a.shape`：获取数组的大小
        - `a.shape = (3, 4)`可以通过修改shape属性保持元素个数不变的情况下，改变多维数组的形状
        - `a.shape = 2,-1`：当某个轴的元素为-1的时候，将根据数组元素的个数自动计算这个轴的长度
    - `a.reshape((6, 2))`：创建一个改变尺寸的新数组，原来的数组shape保持不变，**但是原数组和新创建的数组共享数字据，也就是他们里面的元素是相同的，在内存中是同一块。**
#### 其他函数
- `np.arange(start,stop,step,dtype)`:类似python中的range函数，可以指定开始值，步长和终止值来创建**一维数组**，注意：数组不包括终止值。
- `linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)`：endpoint指定是否包含终值，缺省值是包含
- `logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None)`：创建等比数列
- 创建具有初始化占位符内容数组：
    - `zeros()`：初始值为0
    - `ones()`：初始值为1
    - `empty()`：初始值为可以指定的（默认为1.）
    - `zeros_like()`：zeros_like(a)与zeros(a.shape, a.dtype)效果相同。
    - `ones_like()`
    - `empty_like()`
### 存储元素
- 数组的存取方法与python中切片方法的概念一样
- 和python列表序列不同的是：通过下标范围获取的新的数组是原始数组的一个视图，也就是说他们**共享一块数据空间**。
- **numpy提供二种存取元素的高级方法**
    - 使用整数序列（可以为list也可以为array）：原来取是这样`x[1]`，现在可以使用list代替原来的下标1`x[[3,4,3,5]]`，并且可以重复取同一下标的元素，此时新获得数组不和原始数组共享数据空间。
    - 使用布尔数组（只能为array）：建立一个与原数组x个数相同的布尔数组b进行获取，使用布尔数组b作为下标存取数组b中对应下标为True的元素。当长度不够的时候，不够的部分默认为False。
        - 布尔数组一般用ufunc产生：`x=np.random().rand(10)>0.5`
#### 多维数组
- 多维数组的存取同样可以使用整数序列和布尔数组进行存取
![多维数组](.\ref_pic\多维数组.png)
- `a[(0,1,2,3,4,5),(6,7,8,9,10,11)]`元组构成的多维数组
- `a[3:,[0,2,5]]`：选取第三行后面的所有行与竖直轴的第1，3，5列的交叉元素
![多维数组2](.\ref_pic\多维数组2.png)
#### 结构数组
- 先定义一个结构类型：
```python
import numpy as np
personType = np.dtype({'names':['name', 'age', 'weight'], 'formats':['S32', 'i', 'f']})
```
- 创建一个结构数组：
```python
import numpy as np
a = np.array([("张三",32,44.5),("里斯", 23, 44.3)], dtype=personType)
```
- 结构数组的存取与一般数组相同
```python
# 取出第一个元素中name值
a[0]["name"]
```







    
    
