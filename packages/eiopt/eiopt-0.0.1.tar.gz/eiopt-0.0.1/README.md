
# eopt

This simple project is an example of a rainpy project build.

[Learn more](https://github.com/zmdsn/rainpy)


```python
from pyomo.environ import *
model = ConcreteModel() # 定义模型
model.x = Var(within=NonNegativeReals) # 声明决策变量 x
model.y = Var(within=NonNegativeReals) # 声明决策变量 y
model.obj = Objective(expr=model.x + model.y, sense = minimize) # 声明目标函数为 x+y, minimize 表示极小化
model.constrs = Constraint(expr=model.x + model.y <= 1) # 添加约束 x+y <= 1
model.write('model.lp') # 输出模型文件
model.pprint() # 打印模型信息
opt = SolverFactory('gurobi') # 指定Gurobi为求解器
solution = opt.solve(model) # 调用求解器求解
```