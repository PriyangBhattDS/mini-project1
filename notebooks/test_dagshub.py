import dagshub
import mlflow

mlflow.set_registry_uri("https://dagshub.com/bhattpriyang/mini-project1.mlflow")
dagshub.init(repo_owner='bhattpriyang', repo_name='mini-project1', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)