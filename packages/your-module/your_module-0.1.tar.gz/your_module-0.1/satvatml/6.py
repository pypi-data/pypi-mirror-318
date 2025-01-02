import pandas as pd
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.models import BayesianNetwork
from pgmpy.inference import VariableElimination

data=pd.read_csv("ds4.csv")
model=BayesianNetwork([('age','lifestyle'),('gender','lifestyle'),('diet','cholestrol'),('lifestyle','diet'),('cholestrol','heartdisease')
                       ,('heartdisease','family')])
model.fit(data,estimator=MaximumLikelihoodEstimator)

infer=VariableElimination(model)

q=infer.query(variables=['heartdisease'],
              evidence={
                  'age':int(input(f"Enter age: 0 for senior\n citizen 1 for aged 2")),
                  'gender':int(input("enter gender")),
                  'lifestyle':int(input("enter lifestyle")),
                  'diet':int(input("enter diet")),
                  'family':int(input("enter family")),
                  'cholestrol':int(input("enter cholestrol"))
              })
print(q)