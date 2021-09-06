import os
import time
import logging
import shutil

from openbrokerapi.service_broker import OperationState

from .config import INSTANCES_PATH
from .tasks import deprovision
from .utils import get_instance_file, load_instance_meta

logger = logging.getLogger(__name__)


def clean_instance():
    for instance_id in os.listdir(INSTANCES_PATH):
        if os.path.exists(get_instance_file(instance_id)):
            data = load_instance_meta(instance_id)
            interval = time.time() - data["last_modified_time"]
            state = data["last_operation"]["state"]
            operation = data["last_operation"]["operation"]
            if interval > 3600 * 24 and (
                operation == "deprovision"
                    and state != OperationState.SUCCEEDED):
                deprovision.delay(instance_id)
            if operation == "deprovision":
                if state == OperationState.SUCCEEDED or (
                    interval > 3600 * 24
                        and state != OperationState.SUCCEEDED):
                    shutil.rmtree(
                        os.path.join(INSTANCES_PATH, instance_id),
                        ignore_errors=True)
        else:
            shutil.rmtree(
                os.path.join(INSTANCES_PATH, instance_id), ignore_errors=True)


if __name__ == "__main__":
    clean_instance()
