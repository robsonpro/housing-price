import dagshub
dagshub.init(repo_owner='robsonpro', repo_name='housing-price', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)

experiment_name = "ElasticNet"
entry_point = "Training"

# local server
# mlflow.set_tracking_uri("http://127.0.0.1:5000")

# for dagshub
# remote_server_uri = "https://dagshub.com/robsonpro/housing-price.mlflow"
# mlflow.set_tracking_uri(remote_server_uri)

# for AWS
remote_server_uri = "http://ec2-54-233-49-254.sa-east-1.compute.amazonaws.com:5000/"
mlflow.set_tracking_uri(remote_server_uri)

mlflow.projects.run(
    uri=".",
    entry_point=entry_point,
    experiment_name=experiment_name,
    env_manager="conda"
)