
#Working complete workflow with Data Validation Dataframe Datatype
from dagster import execute_pipeline, pipeline, solid,as_dagster_type,lambda_solid
import pandas as pd

DataFrame = as_dagster_type(
    pd.DataFrame,
    name='PandasDataFrame',
)
@lambda_solid
def Input1() -> DataFrame:
    r = pd.read_csv('file1.csv')
    return r

@lambda_solid
def Input2() -> DataFrame:
    r2 = pd.read_csv('file2.csv')
    return r2

@lambda_solid
def Merge(r:DataFrame,r2:DataFrame) -> DataFrame:
    r3=pd.concat([r,r2], axis=1)
    return r3

@lambda_solid
def Result_output(y:DataFrame) -> DataFrame:
    y3=y
    y3.to_csv(r'y3.csv')
    return y3

@pipeline
def actual_dag_pipeline() -> DataFrame:
    y=Merge(Input1(),Input2())
    Result_output(y)


'''
import collections
import dagstermill as dm
from dagster import Any, Field, lambda_solid, solid, pipeline, as_dagster_type,PipelineDefinition,InputDefinition, OutputDefinition, Int


my_notebook_solid = dm.define_dagstermill_solid(
                                name='DM1',
                                notebook_path='DM1.ipynb',
                                input_defs = [
                                    InputDefinition(name='a'),
                                    InputDefinition(name='b')
                                ],
                                output_defs  = [OutputDefinition()]
                            )

def notebook_pipeline():
    return PipelineDefinition(name='pipeline', solid_defs =[my_notebook_solid])


from dagster import pipeline,PipelineDefinition
import dagstermill as dm

solid1 = dm.define_dagstermill_solid(
    name='first_solid',
    notebook_path='first_solid.ipynb'
)


solid2 = dm.define_dagstermill_solid(
    name='juljul1',
    notebook_path='juljul1.ipynb'
)



solid2 = dm.define_dagstermill_solid(
    name='third_solid',
    notebook_path='third_solid.ipynb'
)


def notebook_pipeline():
    return PipelineDefinition(name='node_1', solid_defs=[solid2])
'''