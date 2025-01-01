import os
import glob
import toml
from typing import Any

from dataclasses import dataclass


@dataclass
class Project:
    project_name: str
    project_root: str
    project_tool: str


def list_projects(pyproject_path: str) -> list[Project]:
    """
    Parses the pyproject.toml file to identify sub projects in a monorepo and returns a list of Projects.
    """
    if not os.path.isfile(pyproject_path):
        raise FileNotFoundError(f"{pyproject_path} does not exist.")

    # Load and parse the pyproject.toml file
    with open(pyproject_path, "r") as file:
        data = toml.load(file)

    sub_projects: list[Project] = []

    if is_poetry_project(data):
        sub_projects = find_sub_projects_in_poetry(data, pyproject_path)
    elif is_hatch_project(data):
        sub_projects = find_sub_projects_in_hatch(data, pyproject_path)
    elif is_uv_project(data):
        sub_projects = find_sub_projects_in_uv_sources(data, pyproject_path)
    else:
        sub_projects = find_sub_projects_in_project_dependencies(data, pyproject_path)

    return sub_projects


def is_poetry_project(tomlData: dict[str, Any]) -> bool:
    return (
        "tool" in tomlData
        and "poetry" in tomlData["tool"]
        and "dependencies" in tomlData["tool"]["poetry"]
    )


def is_hatch_project(tomlData: dict[str, Any]) -> bool:
    return "tool" in tomlData and "hatch" in tomlData["tool"]


def is_uv_project(tomlData: dict[str, Any]) -> bool:
    return "tool" in tomlData and "uv" in tomlData["tool"]


def find_sub_projects_in_poetry(tomlData: dict[str, Any], toml_path: str) -> list[Project]:
    """
    Finds sub projects in a poetry project by looking for dependencies with a "path" key:
        [tool.poetry.dependencies]
        python = "^3.9"
        service-a = { path = "./services/service-a" }
        service-b = { path = "./services/service-b" }
        shared-lib = { path = "./shared-libraries/shared-lib" }
    """
    subProjects: list[Project] = []
    for dep_name, dep_value in tomlData["tool"]["poetry"]["dependencies"].items():
        if isinstance(dep_value, dict) and "path" in dep_value:
            subProjects.append(
                Project(
                    project_name=dep_name,
                    project_root=get_absolute_path(toml_path, dep_value["path"]),
                    project_tool="poetry",
                )
            )
    return subProjects


def find_sub_projects_in_hatch(tomlData: dict[str, Any], toml_path: str) -> list[Project]:
    """
    Finds sub projects in a hatch project by looking for dependencies with a "path" key:
        [tool.hatch.envs.default.dependencies]
        service-a = { path = "./services/service-a" }
        service-b = { path = "./services/service-b" }
    """
    subProjects: list[Project] = []
    hatch_envs = tomlData["tool"]["hatch"].get("envs", {})
    for env_name, env_data in hatch_envs.items():
        if isinstance(env_data, dict) and "dependencies" in env_data:
            dependencies = env_data["dependencies"]
            if isinstance(dependencies, dict):
                for dep_name, dep_value in dependencies.items():
                    if isinstance(dep_value, dict) and "path" in dep_value:
                        subProjects.append(
                            Project(
                                project_name=dep_name,
                                project_root=get_absolute_path(toml_path, dep_value["path"]),
                                project_tool=f"hatch:{env_name}",
                            )
                        )
    return subProjects


def find_sub_projects_in_uv_sources(tomlData: dict[str, Any], toml_path: str) -> list[Project]:
    """
    Finds sub projects in a uv project by looking at sources and workspace:
    [tool.uv.sources]
    service-a = { path = "./services/service-a" }
    service-b = { path = "./services/service-b" }

    [tool.uv.workspace]
    members = ["packages/*"]
    exclude = ["packages/excluded/*"]
    """
    subProjects: list[Project] = []
    uv_sources = tomlData["tool"]["uv"].get("sources", {})
    uv_workspace = tomlData["tool"]["uv"].get("workspace", {})
    for source_name, source_data in uv_sources.items():
        if isinstance(source_data, dict) and "path" in source_data:
            subProjects.append(
                Project(
                    project_name=source_name,
                    project_root=get_absolute_path(toml_path, source_data["path"]),
                    project_tool="uv.sources",
                )
            )
    if isinstance(uv_workspace, dict) and "members" in uv_workspace:
        excluded_directories = []
        exclude_globs = uv_workspace.get("exclude", [])
        for exclude_glob in exclude_globs:
            excluded_directories.extend(
                glob.glob(
                    os.path.join(os.path.dirname(toml_path), exclude_glob),
                    recursive=True,
                )
            )

        for glob_pattern in uv_workspace["members"]:
            # Every directory included by the members globs (and not excluded by the exclude globs) must contain a pyproject.toml file
            directories = glob.glob(
                os.path.join(os.path.dirname(toml_path), glob_pattern),
                recursive=True,
            )

            for directory in directories:
                if (
                    os.path.exists(os.path.join(directory, "pyproject.toml"))
                    and directory not in excluded_directories
                ):
                    subProjects.append(
                        Project(
                            project_name=os.path.basename(directory),
                            project_root=directory,
                            project_tool="uv.workspace",
                        )
                    )

    return subProjects


def find_sub_projects_in_project_dependencies(
    tomlData: dict[str, Any], toml_path: str
) -> list[Project]:
    """
    Finds sub projects in a project dependencies by looking for dependencies with
    the @ file:///${PROJECT_ROOT}//${SUBPROJECT_PATH} format:
        [project]
        dependencies = [
            "service-a @ file:///${PROJECT_ROOT}//services/service-a",
            "service-b @ file:///${PROJECT_ROOT}//services/service-b"
        ]
    """
    subProjects: list[Project] = []
    for dep in tomlData["project"]["dependencies"]:
        if isinstance(dep, str) and dep.find("@ file:///${PROJECT_ROOT}//"):
            rel_path = dep.split("@ file:///${PROJECT_ROOT}//")[1]
            subProjects.append(
                Project(
                    project_name=os.path.basename(dep),
                    project_root=get_absolute_path(toml_path, rel_path),
                    project_tool="project.dependencies",
                )
            )
    return subProjects


def get_absolute_path(path_to_root_toml: str, path_to_sub_project: str) -> str:
    path_to_root = os.path.dirname(path_to_root_toml)
    return os.path.abspath(os.path.join(path_to_root, path_to_sub_project))
