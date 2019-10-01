# Dagster workflow
Workflow created is a functional  basic DAG workflow using Dagster Library to implement Data Pipeline using which consists of 4 nodes where 3 nodes are executed via python and 1 node via Julia script.

## Getting Started
There are currently 5 relevant files in the Dagster Repository which important for the execution of the created Dagster workflow

[File1.csv](https://github.com/achintamiri/dagster/blob/master/file1.csv)  (Consists 1st input file)

[File2.csv](https://github.com/achintamiri/dagster/blob/master/file2.csv) (Consists 2nd input file)

[juliatest.py](https://github.com/achintamiri/dagster/blob/master/juliatest.py) (Consists Actual workflow pipeline file)

[julia_sample.jl](https://github.com/achintamiri/dagster/blob/master/julia_sample.jl) (Consists Julia Script)

[test_systemA4-toolbox.jl](https://github.com/achintamiri/dagster/blob/master/test_systemA4-toolbox.jl) (Consists Spine Julia Script Which Executes in Dagster).

## Installation Instructions
1.Clone the master branch  onto your computer.

2.Install Python (3.6->) and JuliaPy(In Julia REPL and Pycall. For more instructions Refer : 

[JuliaPy](https://github.com/JuliaPy/pyjulia) 

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

1. Load the project in any IDE like PyCharm

2. Use the below command to execute the workflow

    `dagit-cli -f juliatest.py -n actual_dag_pipeline`  ( For Windows)
    
    `dagit -f juliatest.py -n actual_dag_pipeline `( For Linux)

3.If it is successful you will see the below message:

     `Loading repository...`
     
     `Serving on http://127.0.0.1:3000` 

4.click on http://127.0.0.1:3000 to see the workflow in Dagit.

5.Click on `select a Pipeline - > actual_dag_pipiline` . You should see a graph with 4 nodes.

6.Click on Execute->Start Execution 


