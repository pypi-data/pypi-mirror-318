import os
import datetime
from typing import List

from ansibleconnect.ansiblehostadapter import AnsibleHostAdapter


def in_tmux() -> bool:
    return 'TMUX' in os.environ


def tmux_start_command() -> str:
    tmux_session_or_window_name = datetime.datetime.now().strftime("ansibleconnect-%Y-%m-%d-%H-%M")
    if in_tmux():
        start_command = "tmux new-window -n {}".format(tmux_session_or_window_name)
    else:
        start_command = "tmux new-session -s {}".format(tmux_session_or_window_name)
    return start_command


def ssh_auth_socket_env_var_command() -> str:
    auth_socket = os.environ.get("SSH_AUTH_SOCK", "")
    if auth_socket != "":
        return "export SSH_AUTH_SOCK={}".format(auth_socket)
    else:
        return ""


def create_tmux_script(hosts: List[AnsibleHostAdapter], use_windows: bool) -> str:
    tmux_file_lines = [tmux_start_command()]
    for index, host in enumerate(hosts):
        first_line = "send-keys '"
        extra_commands = ssh_auth_socket_env_var_command()
        if extra_commands != "":
            first_line += "{extra_commands};".format(
                extra_commands=ssh_auth_socket_env_var_command())
        first_line += "{conn_command}' C-m".format(
            conn_command=host.connection_command)
        tmux_file_lines.append(first_line)
        if index != len(hosts) - 1:
            if use_windows:
                tmux_file_lines.append(f"new-window -n {hosts[index+1].host_name}")
            else:
                tmux_file_lines.append("split-window -h")
            # tiled layout rearranges panes so that each pane has the same size
            tmux_file_lines.append("select-layout tiled")
    # \; is printed so that ; can be interpreted by tmux instead of shell
    tmux_script = " \\; ".join(tmux_file_lines)
    return tmux_script
