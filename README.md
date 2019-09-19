# Dagster workflow
Workflow created is a functional  basic DAG workflow using Dagster Library to implement Data Pipeline using which consists of 4 nodes where 3 nodes are executed via python and 1 node via Julia script.

## Getting Started
There are currently 4 relevant files in the Dagster Repository which important for the execution of the created Dagster workflow

[File1.csv](https://github.com/achintamiri/dagster/blob/master/file1.csv)

[File2.csv](https://github.com/achintamiri/dagster/blob/master/file2.csv)

[juliatest.py](https://github.com/achintamiri/dagster/blob/master/juliatest.py)

[julia_sample.jl](https://github.com/achintamiri/dagster/blob/master/julia_sample.jl)

## Installation Instructions
1.Clone the master branch  onto your computer.

2.Install Python (3.6->)

3.Open Anaconda prompt

4.Create a new environment by typing the below command or you can use (base) also.

    `conda create -n dagster python=3.7 `

5.Activate the new environment

    `conda activate dagster`

6.cd to dagster(cloned) root directory (the one with requirements.txt)

    `pip install dagster dagit`

            OR
    `pip install -r requirements.txt`
    
 ## Workflow Execution
