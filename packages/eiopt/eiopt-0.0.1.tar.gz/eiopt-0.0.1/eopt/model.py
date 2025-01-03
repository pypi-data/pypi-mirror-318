from .common import *
from .variables import VariableBase, Variable
from .objective import Objective
from .constraint import Constraint
import pyomo.environ as pyo
from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.optimize import minimize
from pymoo.core.problem import Problem
from .algorithms.ga import GA

class MoProblem(Problem):
    def __init__(self,
                 n_var,
                 n_obj,
                 n_constr,
                 xl,
                 xu, 
                 vtype,
                 model):
        super().__init__(n_var=n_var, 
                         n_obj=n_obj, 
                         n_constr=n_constr, 
                         xl=xl, 
                         xu=xu,
                         vtype=vtype)
        self.model = model

    def _evaluate(self, x, out):
        obj_list = []
        for v in x:
            self.model.variables[0].set_value(v)
            obj_list.append([obj(self.model).value[0] * obj.sense for obj in self.model.objectives])
        out["F"] = np.array(obj_list)
        
        G_list = []
        for v in x:
            self.model.variables[0].set_value(v)
            G_list.append([constr(self.model) for constr in self.model.ieq_constraints])
        out["G"] = np.array(G_list)
        
        H_list = []
        for v in x:
            self.model.variables[0].set_value(v)
            H_list.append([constr(self.model) for constr in self.model.eq_constraints])
        out["H"] = np.array(H_list)

    # def _calc_pareto_front(self, n_pareto_points=100):
    #     x = np.linspace(0, 1, n_pareto_points)
    #     return np.array([x, 1 - np.sqrt(x)]).T

class Model:
    def __init__(self, name: str = ""):
        self.name = name
        self.variables = []
        self.objectives = []
        self.constraints = []
        self.eq_constraints = []
        self.ieq_constraints = []
        self.result = {"status":1,
                       "objetives":[],
                       "variables":[],
                       "constraints":[]}

    def addVariable(self, *args, **kwargs):
        var = Variable(*args, **kwargs)
        self.variables.append(var)
        return var
    
    def addObjective(self, *args, **kwargs):
        obj = Objective(*args, **kwargs)
        self.objectives.append(obj)
        return obj

    def addConstraint(self, *args, **kwargs):
        con = Constraint(*args, **kwargs)
        self.constraints.append(con)
        if con.ctype:
            self.ieq_constraints.append(con)
        else:
            self.eq_constraints.append(con)
        return con

    def to_pyomo(self):
        return pyo.ConcreteModel()
    
    def to_pyomo_str(self):
        if len(self.objectives) > 1:
            raise ValueError(f"Please input only 1 objective")

        self._pyomo_code = ["import pyomo.environ as pyo",
                            "model = pyo.ConcreteModel()"]
        for var in self.variables:
            self._pyomo_code.append(var.to_pyomo())
        for obj in self.objectives:
            self._pyomo_code.append(obj.to_pyomo())
        for con in self.variables:
            self._pyomo_code.append(con.to_pyomo())
        return "\n".join(self._pyomo_code)



    def solve_by_lp(self, solver="gurobi"):
        model = self.to_moo()
        for i, var in enumerate(self.variables):
            name = var.name if var.name else f"var{i}"
            setattr(model, name, var.to_pyomo())
        for obj in self.objectives:
            setattr(model, f"obj", obj.to_pyomo())
        for j, con in enumerate(self.constraints):
            setattr(model, f"con{j}", con.to_pyomo())
        solver = pyo.SolverFactory(solver)
        self.model = model
        results = solver.solve(model)
        self.result = results
 
    def solve_by_EA(self, solver="GA"):
        globals()[solver](model=self).solve()


    def solve_by(self, solver="gurobi"):
        if len(self.objectives) <= 1:
            if solver in ['cbc', 'gurobi', 'glpk', 'copt', 'cplex']:
                results = self.solve_by_lp(self, solver=solver)
            else:
                results = self.solve_by_EA(self, solver=solver)
        else:
            problem = self.to_moo()
            algorithm = globals()[solver](pop_size=100)
            results = minimize(problem,
                        algorithm,
                        ('n_gen', 200),
                        seed=1,
                        verbose=True)
            self.result = results.__dict__
        return self.result

    def pprint(self):
        self.model.pprint()

    def to_moo(self):
        if len(self.variables) < 1:
            raise ValueError(f"You must define one variable, like:\n model.addVariable('C', name='x')")
        var = self.variables[0]
        n_var = var.shape[0]
        return MoProblem(n_var = n_var,
                n_obj = len(self.objectives),
                n_constr = len(self.constraints),
                xl = -999999 if var.lb == -np.inf else var.lb,
                xu = 999999 if var.ub == np.inf else var.ub,
                model = self,
                vtype=float)
