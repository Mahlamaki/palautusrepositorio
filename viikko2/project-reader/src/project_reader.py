from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = toml.loads(request.urlopen(self._url).read().decode("utf-8"))

        name = content.get("tool").get("poetry").get("name")
        description = content.get("tool").get("poetry").get("description")
        license = content.get("tool").get("poetry").get("license")
        authors = content.get("tool").get("poetry").get("authors")
        dependencies = content.get("tool").get("poetry").get("dependencies")
        dev_dependencies = content.get("tool").get("poetry").get("group").get("dev").get("dependencies")

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name,description,license,authors,dependencies,dev_dependencies)

    