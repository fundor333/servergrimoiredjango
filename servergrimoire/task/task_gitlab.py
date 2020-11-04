from servergrimoire.errors import GitLabTokenAbsent
from servergrimoire.models import GitLabInstallation
import logging

logger = logging.getLevelName(__name__)


def task_gitlab(gitlab: GitLabInstallation):
    try:
        gitlab.last_version_gitlab()
    except GitLabTokenAbsent:
        logging.error(f"Error with {gitlab.base_url}")
