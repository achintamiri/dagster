'''
import julia
julia.install()
from julia import Base # install PyCall.jl etc.
Base.sind(90)
#from julia import Base
j = julia.Julia()
j.include("julia_sample.jl")
'''
'''
import julia
#julia.install()
#from julia import Base
#Base.sind(90)
from dagster import execute_pipeline, pipeline, solid,as_dagster_type,lambda_solid
import pandas as pd

@solid
def Input1(_) :
    j = julia.Julia()
    j.include("julia_sample.jl")
    return j

@pipeline
def hello_world_pipeline():
    Input1()
'''
import julia
from dagster import execute_pipeline, pipeline, solid,as_dagster_type,lambda_solid
import pandas as pd
# Data Validations which check that source and destination files should be in PandasDataFrame format in all the nodes.
DataFrame = as_dagster_type(
    pd.DataFrame,
    name='PandasDataFrame',
)
@lambda_solid #Defines a node in the workflow.
def Input1() -> DataFrame:  #Represents first node which read input file -> file1.csv from external path.
    r = pd.read_csv('file1.csv')
    return r

@lambda_solid
def Input2() -> DataFrame: #Represents second node which read input file -> file2.csv from external path.
    r2 = pd.read_csv('file2.csv')
    return r2

@lambda_solid  #Represents third node which merges input from file1 and file 2 ny calling julia_sample.jl.
def Merge(r:DataFrame,r2:DataFrame) -> DataFrame:
    j = julia.Julia()
    j.include("julia_sample.jl")
    r3 = j.filesmeth(r, r2)
    # r4 = j.include("test_systemA4-toolbox.jl")
    return r3

@lambda_solid # Fourth node which contains the output merged file.
def Result_output(y:DataFrame) -> DataFrame:
    y3=y
    y3.to_csv(r'merged_output.csv')
    return y3

@pipeline # definition for pipeline execution
def actual_dag_pipeline() -> DataFrame:
    y=Merge(Input1(),Input2())
    Result_output(y)
