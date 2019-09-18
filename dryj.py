import julia
from dagster import execute_pipeline, pipeline, solid,as_dagster_type,lambda_solid
import pandas as pd

@solid
def Merge(_) :
    #r3=pd.concat([r,r2], axis=1)
    j = julia.Julia()
    r3 = j.include("julia_sample.jl")
    return r3

@pipeline
def actual_dag_pipeline() :
       Merge()