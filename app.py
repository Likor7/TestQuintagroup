import os
from dotenv import load_dotenv

from ManageAPI import ManagerAPI
from report_generator import format_report

if __name__ == "__main__":
    load_dotenv()
    api_key = os.getenv("X_API_KEY")
    headers = {"x-api-key": api_key}

    base_url = "https://api.clockify.me/api/v1/"

    manager = ManagerAPI(base_url, headers)

    user = manager.get_user()

    workspaces = manager.get_workspaces()

    if user and workspaces:
        # print("Workspases:")
        # for workspace in workspaces:
        #     print(
        #         f"Workspace Name: {workspace['name']}, Workspace ID: {workspace['id']}"
        #     )
        user_id = user["id"]
        workspace_id = workspaces[0]["id"]
        # If u have more than one workspace, you should uncomment this and comment the above statement
        # workspace_id = input("Enter a workspace ID to fetch projects: ")

        # print("-------------")
        projects = manager.get_projects(workspace_id)

        if projects:
            # for project in projects:
            #     print(f"Project Name: {project['name']}, Project ID: {project['id']}")

            project_id = projects[0]["id"]
            # If u have more than one project, you should uncomment this and comment the above statement
            # project_id = input("Enter a project ID to fetch tasks: ")
            # print("-------------")

            tasks = manager.get_tasks(workspace_id, project_id)
            if tasks:
                # for task in tasks:
                #     print(f"Task Name: {task['name']}, Task ID: {task['id']}")
                entries = manager.get_entries(user_id, workspace_id)

                format_report(workspaces, workspace_id, projects, tasks, entries)
                # if you want to check info about the specific task, you should uncomment below statements
                # task_id = input("Enter a task ID to fetch info about task: ")

                # print(manager.get_task_info(workspace_id, project_id, task_id))
            else:
                print("There is no tasks")
        else:
            print("There is no projects")
    else:
        print("There is no workspases")
