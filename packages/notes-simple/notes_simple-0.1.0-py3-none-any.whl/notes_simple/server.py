import logging
from datetime import datetime

import mcp.server.stdio
import mcp.types as types
from mcp.server import NotificationOptions, Server
from mcp.server.models import InitializationOptions
from pydantic import AnyUrl

# Set up logging - make it the root logger to capture everything
root_logger = logging.getLogger()  # Root logger
root_logger.setLevel(logging.DEBUG)  # Set root to DEBUG to allow all levels through

# Add stderr handler for local debugging
stderr_handler = logging.StreamHandler()
stderr_handler.setFormatter(
    logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
)
root_logger.addHandler(stderr_handler)

# Add file handler for persistent logging
file_handler = logging.FileHandler("notes_server.log")
file_handler.setFormatter(
    logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
)
root_logger.addHandler(file_handler)

# Get a specific logger for this module and configure it
notes_logger = logging.getLogger("notes-server")
notes_logger.setLevel(logging.DEBUG)  # Set to desired level
notes_logger.propagate = True  # Ensure logs propagate to root logger

# Also capture MCP framework logs
mcp_logger = logging.getLogger("mcp.server")
mcp_logger.setLevel(logging.DEBUG)
mcp_logger.propagate = True

# Store notes as a simple key-value dict to demonstrate state management
notes: dict[str, str] = {}

server = Server("notes_simple")


@server.list_resources()
async def handle_list_resources() -> list[types.Resource]:
    """
    List available note resources.
    Each note is exposed as a resource with a custom note:// URI scheme.
    """
    notes_logger.info(f"Listing resources - current notes count: {len(notes)}")
    resources = [
        types.Resource(
            uri=AnyUrl(f"note://internal/{name}"),
            name=f"Note: {name}",
            description=f"A simple note named {name}",
            mimeType="text/plain",
        )
        for name in notes
    ]
    notes_logger.debug(f"Returning resources: {[r.name for r in resources]}")
    return resources


@server.read_resource()
async def handle_read_resource(uri: AnyUrl) -> str:
    notes_logger.info(f"Reading resource: {uri}")

    if uri.scheme != "note":
        error_msg = f"Unsupported URI scheme: {uri.scheme}"
        notes_logger.error(error_msg)
        raise ValueError(error_msg)

    if uri.path is None:
        error_msg = "Missing path in URI"
        notes_logger.error(error_msg)
        raise ValueError(error_msg)

    name = uri.path.lstrip("/")
    if name not in notes:
        error_msg = f"Note not found: {name}"
        notes_logger.error(error_msg)
        raise ValueError(error_msg)

    note_content = notes[name]
    notes_logger.debug(f"Found note '{name}' with content length: {len(note_content)}")

    # Return just the string content - the decorator will wrap it in the proper response type
    return note_content


@server.list_prompts()
async def handle_list_prompts() -> list[types.Prompt]:
    """
    List available prompts.
    Each prompt can have optional arguments to customize its behavior.
    """
    notes_logger.info("Listing available prompts")
    prompts = [
        types.Prompt(
            name="summarize-notes",
            description="Creates a summary of all notes",
            arguments=[
                types.PromptArgument(
                    name="style",
                    description="Style of the summary (brief/detailed)",
                    required=False,
                )
            ],
        )
    ]
    notes_logger.debug(f"Returning prompts: {[p.name for p in prompts]}")
    return prompts


@server.get_prompt()
async def handle_get_prompt(
    name: str, arguments: dict[str, str] | None
) -> types.GetPromptResult:
    """
    Generate a prompt by combining arguments with server state.
    The prompt includes all current notes and can be customized via arguments.
    """
    notes_logger.info(f"Getting prompt '{name}' with arguments: {arguments}")

    if name != "summarize-notes":
        error_msg = f"Unknown prompt: {name}"
        notes_logger.error(error_msg)
        raise ValueError(error_msg)

    style = (arguments or {}).get("style", "brief")
    notes_logger.debug(f"Using style: {style}")

    # Log the notes being included
    notes_logger.debug(f"Including {len(notes)} notes in prompt")

    result = types.GetPromptResult(
        description="Summarize the current notes",
        messages=[
            types.PromptMessage(
                role="user",
                content=types.TextContent(
                    type="text",
                    text=f"Here are the current notes to summarize:{' Give extensive details.' if style == 'detailed' else ''}\n\n"
                    + "\n".join(
                        f"- {name}: {content}" for name, content in notes.items()
                    ),
                ),
            )
        ],
    )
    return result


@server.list_tools()
async def handle_list_tools() -> list[types.Tool]:
    """
    List available tools.
    Each tool specifies its arguments using JSON Schema validation.
    """
    notes_logger.info("Listing available tools")
    tools = [
        types.Tool(
            name="add-note",
            description="Add a new note",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "content": {"type": "string"},
                },
                "required": ["name", "content"],
            },
        )
    ]
    notes_logger.debug(f"Returning tools: {[t.name for t in tools]}")
    return tools


@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict | None
) -> list[types.TextContent | types.ImageContent | types.EmbeddedResource]:
    """
    Handle tool execution requests.
    Tools can modify server state and notify clients of changes.
    """
    notes_logger.info(f"Calling tool '{name}' with arguments: {arguments}")

    if name != "add-note":
        error_msg = f"Unknown tool: {name}"
        notes_logger.error(error_msg)
        raise ValueError(error_msg)

    if not arguments:
        error_msg = "Missing arguments"
        notes_logger.error(error_msg)
        raise ValueError(error_msg)

    note_name = arguments.get("name")
    content = arguments.get("content")

    if not note_name or not content:
        error_msg = "Missing name or content"
        notes_logger.error(error_msg)
        raise ValueError(error_msg)

    # Update server state
    notes[note_name] = content
    notes_logger.info(
        f"Added new note '{note_name}' with content length: {len(content)}"
    )

    # Notify clients that resources have changed
    await server.request_context.session.send_resource_list_changed()
    notes_logger.debug("Sent resource list changed notification")

    # Also send a log message to the client
    await server.request_context.session.send_log_message(
        level="info", data=f"Added note '{note_name}' at {datetime.now().isoformat()}"
    )

    return [
        types.TextContent(
            type="text",
            text=f"Added note '{note_name}' with content: {content}",
        )
    ]


async def main():
    notes_logger.info("Starting notes server...")

    # Run the server using stdin/stdout streams
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        notes_logger.info("Server streams initialized")

        init_options = InitializationOptions(
            server_name="notes_simple",
            server_version="0.1.0",
            capabilities=server.get_capabilities(
                notification_options=NotificationOptions(),
                experimental_capabilities={},
            ),
        )
        notes_logger.debug(f"Initialization options: {init_options}")

        try:
            await server.run(
                read_stream,
                write_stream,
                init_options,
                raise_exceptions=True,
            )
        except Exception as e:
            notes_logger.error(f"Server error: {e}", exc_info=True)
            raise
        finally:
            notes_logger.info("Server shutting down")
