#!/usr/bin/env python3
"""Update Claude Code MCP configuration with FiftyOne credentials from .env"""

import json
import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get FiftyOne credentials
api_uri = os.getenv("FIFTYONE_API_URI")
api_key = os.getenv("FIFTYONE_API_KEY")

if not api_uri or not api_key:
    print("❌ Error: FIFTYONE_API_URI and FIFTYONE_API_KEY must be set in .env")
    exit(1)

# Update Claude Code config
config_path = Path.home() / ".claude" / "claude_desktop_config.json"

with open(config_path) as f:
    config = json.load(f)

config["mcpServers"]["fiftyone"]["env"]["FIFTYONE_API_URI"] = api_uri
config["mcpServers"]["fiftyone"]["env"]["FIFTYONE_API_KEY"] = api_key

with open(config_path, "w") as f:
    json.dump(config, f, indent=2)

print("✅ Claude Code MCP configuration updated successfully!")
print(f"   API URI: {api_uri}")
print(f"   Config file: {config_path}")
print("\n🔄 Please restart Claude Code to load the MCP server")
