import os
import yaml

DEFAULT_CONFIG = {
    "mlflow": {
        "enable": True,
        "tracking_uri": "http://mlflow.internal.sais.com.cn",
        "experiment_name": "default_experiment",
        "run_name": "default_run",
    }
}


def load_config(config_path: str = "config.yaml"):
    if not os.path.exists(config_path):
        print(f"[config_manager] {config_path} 未找到，使用默认配置。")
        return DEFAULT_CONFIG

    with open(config_path, "r", encoding="utf-8") as f:
        try:
            user_config = yaml.safe_load(f)
        except Exception as e:
            print(f"[config_manager] 加载 {config_path} 时出错: {e}。使用默认配置。")
            return DEFAULT_CONFIG

    # 合并默认配置与用户配置（用户配置覆盖默认）
    merged_config = DEFAULT_CONFIG.copy()
    if "mlflow" in user_config:
        merged_config["mlflow"].update(user_config["mlflow"])

    return merged_config
