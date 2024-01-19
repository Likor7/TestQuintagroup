from tabulate import tabulate
from datetime import timedelta

from utils import parse_iso_datetime


def get_workspace_name(workspaces, workspace_id):
    return next(
        (ws["name"] for ws in workspaces if ws["id"] == workspace_id),
        "Unknown Workspace",
    )


def prepare_time_entries(entries, task_names):
    time_entries = {}
    for entry in entries:
        task_id = entry["taskId"]
        start_time = parse_iso_datetime(entry["timeInterval"]["start"])
        end_time = (
            parse_iso_datetime(entry["timeInterval"]["end"])
            if entry["timeInterval"].get("end")
            else None
        )
        duration = end_time - start_time if end_time else None

        if task_id not in time_entries:
            time_entries[task_id] = []

        time_entries[task_id].append(
            (task_names.get(task_id, "Unknown Task"), start_time, end_time, duration)
        )

    return time_entries


def print_report(time_entries, project_names, tasks):
    for task_id, entries in time_entries.items():
        project_id = next((t["projectId"] for t in tasks if t["id"] == task_id), None)
        project_name = project_names.get(project_id, "Unknown Project")

        report_data = []
        total_duration = timedelta()
        for task_name, start_time, end_time, duration in entries:
            total_duration += duration if duration else timedelta()
            report_data.append(
                [
                    start_time.strftime("%Y-%m-%d %H:%M:%S") if start_time else "N/A",
                    end_time.strftime("%Y-%m-%d %H:%M:%S") if end_time else "N/A",
                    str(duration) if duration else "N/A",
                ]
            )

        print(f"Task: {task_name} (Project: {project_name})")
        print(
            tabulate(
                report_data,
                headers=["Start Time", "End Time", "Time Spent"],
                tablefmt="grid",
            )
        )
        print(f"Total Time Spent on Task: {total_duration}\n")


def format_report(workspaces, workspace_id, projects, tasks, entries) -> None:
    workspace_name = get_workspace_name(workspaces, workspace_id)
    print(f"Workspace: {workspace_name}\n")

    project_names = {project["id"]: project["name"] for project in projects}
    task_names = {task["id"]: task["name"] for task in tasks}

    time_entries = prepare_time_entries(entries, task_names)
    print_report(time_entries, project_names, tasks)
