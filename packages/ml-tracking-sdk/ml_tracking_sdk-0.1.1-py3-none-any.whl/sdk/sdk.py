import mlflow
from functools import wraps
from .config_manager import load_config

# Global configuration
CONFIG = load_config()


class MLflowWrapper:
    def __init__(self, config: dict):
        self.config = config
        self.experiment = None
        self.run = None

        if self.config["mlflow"]["enable"]:
            self._init_mlflow()
        else:
            print("[MLflowWrapper] MLflow is disabled.")

    def _init_mlflow(self):
        mlflow.set_tracking_uri(self.config["mlflow"]["tracking_uri"])
        self.experiment = mlflow.get_experiment_by_name(
            self.config["mlflow"]["experiment_name"])
        if not self.experiment:
            self.experiment_id = mlflow.create_experiment(
                self.config["mlflow"]["experiment_name"])
        else:
            self.experiment_id = self.experiment.experiment_id
        self.run = mlflow.start_run(
            experiment_id=self.experiment_id, run_name=self.config["mlflow"]["run_name"])
        print("[MLflowWrapper] MLflow initialization completed.")

    def log_metrics(self, metrics: dict, step=None):
        if not self.config["mlflow"]["enable"]:
            return
        if step is not None:
            mlflow.log_metrics(metrics, step=step)
        else:
            mlflow.log_metrics(metrics)

    def log_params(self, params: dict):
        if not self.config["mlflow"]["enable"]:
            return
        mlflow.log_params(params)

    def log_artifacts(self, local_dir: str, artifact_path: str = None):
        if not self.config["mlflow"]["enable"]:
            return
        mlflow.log_artifacts(local_dir, artifact_path)

    def log_model(self, model, artifact_path: str):
        if not self.config["mlflow"]["enable"]:
            return
        mlflow.sklearn.log_model(model, artifact_path)

    def finish(self):
        if self.run:
            mlflow.end_run()
            print("[MLflowWrapper] MLflow run ended.")


# Create global MLflowWrapper instance
GLOBAL_MLFLOW_WRAPPER = MLflowWrapper(CONFIG)


def init_mlflow(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if GLOBAL_MLFLOW_WRAPPER.run is None and CONFIG["mlflow"]["enable"]:
            GLOBAL_MLFLOW_WRAPPER._init_mlflow()
        try:
            return func(*args, **kwargs)
        finally:
            if GLOBAL_MLFLOW_WRAPPER.run:
                GLOBAL_MLFLOW_WRAPPER.finish()
    return wrapper


def log_metrics(metrics: dict, step=None):
    GLOBAL_MLFLOW_WRAPPER.log_metrics(metrics, step)


def log_params(params: dict):
    GLOBAL_MLFLOW_WRAPPER.log_params(params)


def log_artifacts(local_dir: str, artifact_path: str = None):
    GLOBAL_MLFLOW_WRAPPER.log_artifacts(local_dir, artifact_path)


def log_model(model, artifact_path: str):
    GLOBAL_MLFLOW_WRAPPER.log_model(model, artifact_path)
