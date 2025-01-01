import logging
import socket
from io import BytesIO
from typing import List
from cbor2 import dumps, CBORDecoder

from rewrite_remote.handlers.project_helper import list_projects
from rewrite_remote.remote_utils import COMMAND_END
from rewrite_remote.remoting import OK, RemotingContext, RemotingMessageType
from rewrite_remote.handlers.handler_helpers import respond_with_error


# Main command handler with the specified signature
def list_projects_handler(
    stream: BytesIO, sock: socket.socket, remoting_ctx: RemotingContext
) -> None:
    remoting_ctx.reset()

    # 1. Read input from stream
    try:
        data = stream.read()
        decoder = CBORDecoder(BytesIO(data))
        root_project_file = str(decoder.decode())
    except Exception as e:  # pylint: disable=broad-except
        respond_with_error(f"Failed to decode arguments: {e}", sock)
        return

    if root_project_file == "" or root_project_file is None:
        respond_with_error("root_project_file is required", sock)
        return

    # 2. Log the request
    logging.info(
        f"""[Server] Handling install-recipe request: {{
        root_project_file: {root_project_file},
    }}"""
    )

    # 3. Find projects
    projects = list_projects(root_project_file)

    # 4. Log the result
    logging.info("[Server] Found %d project(s)", len(projects))
    for project in projects:
        logging.info(
            " %s root at %s using %s",
            project.project_name,
            project.project_root,
            project.project_tool,
        )

    # 5. Write response to stream
    response: List[str] = []

    for project in projects:
        response.append(project.project_root)

    # Encode the response using CBOR
    encoded_response = b""
    encoded_response += dumps(RemotingMessageType.Response)
    encoded_response += dumps(OK)
    encoded_response += dumps(response)
    encoded_response += COMMAND_END
    sock.sendall(encoded_response)

    logging.info("[Server] Request completed.")
