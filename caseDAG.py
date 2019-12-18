import os
import json,yaml
import pandas as pd
from dagster import execute_pipeline, pipeline, solid,as_dagster_type,lambda_solid
import julia

with open('caseA4.yaml') as f:
        data_str = json.dumps(yaml.load(f))
        data_json = json.loads(data_str)
def read_input_files1():
        if((data_json['inputs']['Input1']['type']=='File?') and (data_json['inputs']['Input1']['extract']=='string') and (data_json['inputs']['Input1']['format']=='xlsx')):
          read_input1 = pd.read_excel(data_json['inputs']['Input1']['inputSource'])
          return read_input1
        else:
           return(print("Invalid File Format "))

@lambda_solid
def xlsx_inputs():
    if (data_json['steps']['xlsx_inputs']['in']['files']['source']):
         task1out = read_input_files1()
         return task1out
    else:
       return(print("Error in Task1"))
@lambda_solid
def coverter(task1out):
    if (data_json['steps']['coverter']['in']['files']['source']):
        with open('testsystemA4.sqlite', 'r') as f:
            sqlfile = f.read()
            sqlfile.close
        return sqlfile

@lambda_solid
def converted_inputs(sqlfile):
    covertedfile =sqlfile
    return covertedfile

@lambda_solid
def case_study_A4(covertedfile):
    if(data_json['steps']['case_study_A4']['in']['files']['source']):
        if(data_json['steps']['case_study_A4']['in']['files']['script']=='julia'):
            j = julia.Julia()
            j.include(data_json['steps']['case_study_A4']['in']['files']['name'])
            outfile = covertedfile
            return outfile
        else:
            return(print("Error in Task3"))
@lambda_solid
def output_db(outfile):
    if (data_json['steps']['output_db']['in']['files']['source']):
        if(data_json['steps']['output_db']['in']['files']['format']=='csv'):
            output = outfile.to_csv(r'merged_output.csv')
            return output
        else:
            return(print("Error in Task4"))
@pipeline # definition for pipeline execution
def actual_dag_pipeline() :
    a = coverter(xlsx_inputs())
    b = converted_inputs(a)
    c=case_study_A4(b)
    output_db(c)


