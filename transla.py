import os
import json,yaml
import pandas as pd
from dagster import execute_pipeline, pipeline, solid,as_dagster_type,lambda_solid
import julia

with open('cwldemo.yaml') as f:
        data_str = json.dumps(yaml.load(f))
        data_json = json.loads(data_str)
def read_input_files1():
        if((data_json['inputs']['Input1']['type']=='File?') and (data_json['inputs']['Input1']['extract']=='string') and (data_json['inputs']['Input1']['format']=='csv')):
          read_input1 = pd.read_csv(data_json['inputs']['Input1']['inputSource'])
          return read_input1
        else:
           return(print("Invalid File Format "))
def read_input_files2():
    if ((data_json['inputs']['Input2']['type'] == 'File?') and (data_json['inputs']['Input2']['extract'] == 'string') and (data_json['inputs']['Input2']['format'] == 'csv')):
        read_input2 = pd.read_csv(data_json['inputs']['Input2']['inputSource'])
        return read_input2
    else:
        return (print("Invalid File Format "))
@lambda_solid
def task1():
    if (data_json['steps']['task1']['in']['files']['source']):
         task1out = read_input_files1()
         return task1out
    else:
       return(print("Error in Task1"))
@lambda_solid
def task2():
    if (data_json['steps']['task2']['in']['files']['source']):
         task2out = read_input_files2()
         return task2out
    else:
       return(print("Error in Task2"))
@lambda_solid
def task3(task1out,task2out):
    if(data_json['steps']['task3']['in']['files']['source']):
        if(data_json['steps']['task3']['in']['files']['script']=='julia'):
            j = julia.Julia()
            j.include(data_json['steps']['task3']['in']['files']['name'])
            r4 = j.include(data_json['steps']['task3']['in']['files']['name2'])
            outfile = j.filesmeth(task1out, task2out)
            return outfile
        else:
            return(print("Error in Task3"))
@lambda_solid
def task4(outfile):
    if (data_json['steps']['task3']['in']['files']['source']):
        if(data_json['steps']['task4']['in']['files']['format']=='csv'):
            output = outfile.to_csv(r'merged_output.csv')
            return output
        else:
            return(print("Error in Task4"))
@pipeline # definition for pipeline execution
def actual_dag_pipeline() :
    y = task3(task1(),task2())
    task4(y)


