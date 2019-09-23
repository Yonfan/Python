## ufunc运算
### ufunc运算简介
- ufunc(universal function)，对数组每个元素进行操作的函数
```python
import numpy as np
# 对数组x中的每一个元素进行正弦运算，返回一个同样大小的新数组
x = np.linsapce(0, 2*np.pi, 10)
y = np.sin(x)
# 将sin函数所计算的结果直接覆盖到数组x上去，可以将被覆盖的数组作为第二个参数传递给ufunc
t = np.sin(x,x) 
```
- 比较和布尔运算，使用‘==’、‘>’这样的比较运算符可以对二个数组进行比较，返回的是一个布尔数组，比较的是二个数组对应元素的比较结果
```python
import numpy as np

res = np.array([1, 2, 3]) < np.array([0, 2, 5]
print(res)
```
- 判断布尔数组中的元素：
```python
# 只要数组中有一个值为True则any()返回True
np.any(a==b)
# 只有当数组中所有元素都为True时候all()函数才返回True
np.all(a==b)
```
- `formpyfunc(func(计算单个元素的函数),nin(func参数的个数),nout(func返回值个数))`：可以将计算单个值的函数转换成为一个能会数组的每个元素进行计算的ufunc函数。返回的数组元素类型是object，需要偶用astype()将其转换。
- `vectorize(func, otype='np.float')`，与formpyfunc相似。
### 广播
- 当使用ufunc对二个数组进行计算的时候，会对这二个数组的对应元素进行计算，所以需要这二个数组有相同的大小（shape相同）。如果不同，会进行广播处理。
