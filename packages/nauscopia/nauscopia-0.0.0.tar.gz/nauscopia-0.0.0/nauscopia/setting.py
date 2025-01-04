import platformdirs

from nauscopia import __appname__

datasets_cache_path = platformdirs.user_cache_path(appname=__appname__) / "datasets"
model_cache_path = platformdirs.user_cache_path(appname=__appname__) / "models"
