from dotenv import load_dotenv
import os

from ManageAPI import ManagerAPI


if __name__ == "__main__":
    load_dotenv()
    api_key = os.getenv("X_API_KEY")
    headers = {"x-api-key": api_key}

    base_url = "https://api.clockify.me/api/v1/"

    manager = ManagerAPI(base_url, headers)

    workspaces = manager.get_workspaces()

    if workspaces:
        print("Workspases:")
        for workspace in workspaces:
            print(
                f"Workspace Name: {workspace['name']}, Workspace ID: {workspace['id']}"
            )

        workspace_id = workspaces[0]["id"]
        # If u have more than one workspace, you should uncomment this and comment the above statement
        # workspace_id = input("Enter a workspace ID to fetch projects: ")

        print("-------------")
        projects = manager.get_projects(workspace_id)

        if projects:
            for project in projects:
                print(f"Project Name: {project['name']}, Project ID: {project['id']}")

            # project_id = projects[0]["id"]
            # If u have more than one project, you should uncomment this and comment the above statement
            project_id = input("Enter a project ID to fetch tasks: ")

            print("-------------")
            tasks = manager.get_tasks(workspace_id, project_id)
            if tasks:
                for task in tasks:
                    print(f"Task Name: {task['name']}, Task ID: {task['id']}")

                # task_id = input("Enter a task ID to fetch info about task: ")

                # print(get_task_info(base_url, headers, workspace_id, project_id, task_id))
            else:
                print("There is no tasks")
        else:
            print("There is no projects")
    else:
        print("There is no workspases")
