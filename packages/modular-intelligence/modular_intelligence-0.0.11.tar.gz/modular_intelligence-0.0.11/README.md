# Modular Intelligence

**Modular Intelligence** is a Python library designed to simplify the process of creating, managing, and deploying AI agents. The library leverages an SQLite database for seamless portability and enables you to define and organize agents into **stacks**, which can be shared and deployed across multiple workspaces.

## Features

- **Easy Installation**: Install via pip with a single command.
- **SQLite-Powered**: Store agents and stacks in a local SQLite database at `~/.modular-intelligence/modular-intelligence.db`.
- **Agent Portability**: Create agents in one workspace and access them in another.
- **Stack System**: Organize agents into stacks for better modularity. Each stack can hold up to 5 agents, and you can have an unlimited number of stacks.
- **Flexible Deployment**: Define agents and stacks in one workspace and deploy them effortlessly in another.

## Installation

Install the library using pip:

```bash
pip install modular_intelligence
```

## Quick Start

Here is an example to get you started:

### Creating an AI Agent

```python
from modular_intelligence.agents import BaseAgent

# Create a new agent
agent = BaseAgent(name="ChatBot", description="A conversational AI agent", prompt="Hello! How can I help you today?")

# Save the agent to the database
agent.save_to_db()
print("Agent created and saved!")
```

### Accessing an Agent in Another Workspace

```python
from modular_intelligence.agents import BaseAgent

# Load the agent from the database
agent = BaseAgent()
agent.load_from_db("ChatBot")
print(f"Loaded agent: {agent.name}")
```

### Creating and Managing Stacks

#### Stacks are updated in real time. There is no need for a "save()" function.

```python
from modular_intelligence.agents import BaseAgent
from modular_intelligence.stacks import AgentStack

# Create agents
agent1 = BaseAgent(name="Agent1", description="Agent 1 description", prompt="Prompt for Agent 1")
agent2 = BaseAgent(name="Agent2", description="Agent 2 description", prompt="Prompt for Agent 2")

# Save agents to the database
agent1.save_to_db()
agent2.save_to_db()

# Create a stack with up to 5 agents
stack = AgentStack(name="ExampleStack", agents=[agent1, agent2])
stack.create(agents=[agent1, agent2])

print("Stack created and saved!")

# Load the stack in another workspace
stack.load_from_db(stack_name="ExampleStack")
print(f"Loaded stack: {stack.name} with agents: {[agent.name for agent in stack.agents]}")
```

### Deploying Stacks

Deploy stacks in different workspaces by loading them from the database ( Not yet available ):

```python
from modular_intelligence.stacks import AgentStack

# Load and deploy the stack
stack = AgentStack.load_from_db("ExampleStack") or AgentStack.load_from_db(stack_id=1)
stack.deploy()
```

## Demo Script

The library includes a demo script to showcase its capabilities. This script demonstrates:

1. Initializing the database.
2. Creating AI agents for specific use cases (e.g., Math Tutor, English Tutor, Science Explainer, History Buff, Code Helper).
3. Organizing agents into stacks.
4. Managing agent conversations and creating checkpoints.
5. Displaying database tables.

### Demo Code Example

```python
from modular_intelligence.database.init_db import init_database
from modular_intelligence.agents import BaseAgent
from modular_intelligence.stacks import AgentStack
from modular_intelligence.scripts.conversations.convos_for_demo_script import get_conversations

# Initialize the database
init_database()
print("Database initialized successfully!")

# Step 1: Create agents
agent1 = BaseAgent(name="MathTutor", description="An AI that helps with math problems.",
                   default_system_prompt="You are a math tutor helping students understand mathematical concepts.")
agent2 = BaseAgent(name="EnglishTutor", description="An AI that helps with English grammar and writing.",
                   default_system_prompt="You are an English tutor assisting students with grammar and composition.")

# Save agents to the database
agent1.save_to_db()
agent2.save_to_db()

# Step 2: Create a stack and add agents
stack = AgentStack(name="Education Stack", description="Stack for educational AI agents")
stack.create()
stack.add_slot(bot=agent1)
stack.add_slot(bot=agent2)

# Step 3: Simulate conversations and create checkpoints
conversations = get_conversations()
for agent, convo in zip([agent1, agent2], conversations):
    for user_input in convo:
        agent.generate_response(user_input)
    agent.save_to_db()

# Step 4: Display database tables
import sqlite3
import pandas as pd
from modular_intelligence.database.init_db import Config

def display_table(table_name):
    db_connection = sqlite3.connect(Config.DATABASE)
    cursor = db_connection.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    columns = [description[0] for description in cursor.description]
    df = pd.DataFrame(rows, columns=columns)
    print(f"\nTable: {table_name}")
    print(df)
    cursor.close()
    db_connection.close()

tables_to_display = ['Bots', 'Stacks', 'StackSlots']
for table in tables_to_display:
    display_table(table_name=table)
```

Run this script to see agents and stacks in action. The output will display the database tables with details of agents, stacks, and their configurations.

## File Structure

When installed, the SQLite database is located at:

```
~/.modular-intelligence/modular-intelligence.db
```

This ensures all agents and stacks are accessible across different projects or workspaces.

## API Reference

### Agent Class

- **`agent = BaseAgent(name, description, prompt)`**: Create a new AI agent.
- **`agent.save_to_db(status="optional custom checkpoint name")`**: Save the agent to the database.
- **`agent.load_from_db(name or id)`**: Load an agent by name.

### Stack Class

- **`stack = AgentStack(name, agents)`**: Create a new stack with up to 5 agents.
- **`stack.save_to_db()`**: Save the stack to the database.
- **`stack.load_from_db(name or stack_id)`**: Load a stack by name.

## Use Cases

- **Agent Sharing**: Create reusable AI agents that can be accessed from any workspace.
- **Workspace Organization**: Group agents into modular stacks for better manageability.
- **Deployment Across Workspaces**: Define agents and stacks in one environment and use them seamlessly elsewhere.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests to improve the library.

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Support

For issues or questions, open a GitHub issue or reach out to the maintainer.

---

**Start building your AI agents with Modular Intelligence today!**
