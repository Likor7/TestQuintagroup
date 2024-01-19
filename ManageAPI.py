from utils import make_http_request


class ManagerAPI:
    def __init__(self, base_url: str, headers: dict):
        self.__base_url = base_url
        self.__headers = headers

    @property
    def base_url(self):
        return self.__base_url

    @property
    def headers(self):
        return self.__headers

    def get_workspaces(self):
        workspaces = make_http_request(self.base_url + "/workspaces/", self.headers)
        if workspaces and len(workspaces) > 0:
            return workspaces
        return None

    def get_projects(self, workspace_id):
        projects = make_http_request(
            self.base_url + f"/workspaces/{workspace_id}/projects", self.headers
        )
        if projects and len(projects) > 0:
            return projects
        return None

    def get_tasks(self, workspace_id, project_id):
        tasks = make_http_request(
            self.base_url + f"workspaces/{workspace_id}/projects/{project_id}/tasks",
            self.headers,
        )
        if tasks and len(tasks) > 0:
            return tasks
        return None

    def get_task_info(self, workspace_id, project_id, task_id):
        task = make_http_request(
            self.base_url
            + f"workspaces/{workspace_id}/projects/{project_id}/tasks/{task_id}",
            self.headers,
        )
        if task:
            return task
        return None
