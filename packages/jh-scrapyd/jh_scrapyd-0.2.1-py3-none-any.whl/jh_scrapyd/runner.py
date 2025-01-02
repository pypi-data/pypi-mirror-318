import os
import sys
import shutil
import tempfile
from contextlib import contextmanager

from importlib.metadata import distributions

from jh_scrapyd import Config
from jh_scrapyd.exceptions import BadEggError
from jh_scrapyd.utils import initialize_component


def activate_egg(eggpath):
    """ Activate a Scrapy egg file using importlib.metadata. """
    try:
        dist = next(distributions(path=[eggpath]))
    except StopIteration:
        raise BadEggError("No valid distribution found at the specified path.")

    # Dynamically add eggpath to sys.path to simulate activation
    if eggpath not in sys.path:
        sys.path.insert(0, eggpath)

    # Find and set Scrapy settings module from entry points
    entry_points = dist.entry_points
    settings_entry = next((ep for ep in entry_points if ep.group == "scrapy" and ep.name == "settings"), None)
    if not settings_entry:
        raise BadEggError("The egg does not contain a valid Scrapy settings entry.")

    os.environ.setdefault("SCRAPY_SETTINGS_MODULE", settings_entry.value)


@contextmanager
def project_environment(project):
    config = Config()
    eggstorage = initialize_component(config, "eggstorage", "scrapyd.eggstorage.FilesystemEggStorage")

    eggversion = os.environ.get("SCRAPYD_EGG_VERSION", None)
    sanitized_version, egg = eggstorage.get(project, eggversion)

    tmp = None
    # egg can be None if the project is not in egg storage: for example, if Scrapyd is invoked within a Scrapy project.
    if egg:
        try:
            if hasattr(egg, "name"):  # for example, FileIO
                activate_egg(egg.name)
            else:  # for example, BytesIO
                prefix = f"{project}-{sanitized_version}-"
                tmp = tempfile.NamedTemporaryFile(suffix=".egg", prefix=prefix, delete=False)
                shutil.copyfileobj(egg, tmp)
                tmp.close()
                activate_egg(tmp.name)
        finally:
            egg.close()

    try:
        yield
    finally:
        if tmp:
            os.remove(tmp.name)


def main():
    project = os.environ["SCRAPY_PROJECT"]
    with project_environment(project):
        from scrapy.cmdline import execute

        # This calls scrapy.utils.project.get_project_settings(). It uses SCRAPY_SETTINGS_MODULE if set. Otherwise, it
        # calls scrapy.utils.conf.init_env(), which reads Scrapy's configuration sources, looks for a project matching
        # SCRAPY_PROJECT in the [settings] section, and uses its value for SCRAPY_SETTINGS_MODULE.
        # https://docs.scrapy.org/en/latest/topics/commands.html#configuration-settings
        execute()


if __name__ == "__main__":
    main()
