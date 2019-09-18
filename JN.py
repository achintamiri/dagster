import collections
import dagstermill as dm
from dagster import pipeline, execute_pipeline, lambda_solid
from dagster import PipelineDefinition,InputDefinition, OutputDefinition, Int
from dagster import Any, Field, lambda_solid, solid, pipeline, as_dagster_type

#context = dm.get_context(solid_config=3)
notebook_solid = dm.define_dagstermill_solid(
    name='hello_world1',
    notebook_path='hello_world1.ipynb')
def notebook_pipeline():
    return PipelineDefinition(name='pipeline', solid_defs=[notebook_solid])