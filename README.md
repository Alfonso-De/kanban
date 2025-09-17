# Kanban Board Template

A comprehensive Kanban board template with standard workflow columns designed for project management and team collaboration.

## Overview

This repository provides a complete Kanban board template with the following columns:

1. **To do** - Tasks that need to be started
2. **In progress** - Tasks currently being worked on  
3. **To Test** - Tasks completed and ready for testing
4. **Done** - Completed and tested tasks

## Files

- `kanban-template.json` - JSON data structure for the Kanban board
- `kanban-template.yaml` - YAML configuration file (human-readable format)
- `kanban-board.html` - HTML visualization of the Kanban board
- `README.md` - This documentation file

## Quick Start

### Viewing the Board

1. **HTML Visualization**: Open `kanban-board.html` in your web browser to see a visual representation of the Kanban board
2. **Data Structure**: Use `kanban-template.json` or `kanban-template.yaml` as templates for your own Kanban implementations

### Structure

Each column contains:
- **Column Properties**: name, description, order, color, work-in-progress limit
- **Cards/Tasks**: title, description, priority, assignee, labels, dates

### Example Card Structure

```json
{
  "id": "card-1",
  "title": "Task title",
  "description": "Detailed task description",
  "priority": "high|medium|low",
  "assignee": "username",
  "labels": ["tag1", "tag2"],
  "created_date": "2024-01-01",
  "due_date": "2024-01-15"
}
```

## Workflow

The template follows a standard software development workflow:

```
To do → In progress → To Test → Done
```

### Column Descriptions

- **To do**: Backlog items and planned tasks
- **In progress**: Active work (recommended limit: 3 items per person)
- **To Test**: Completed features awaiting quality assurance
- **Done**: Verified and completed work

## Customization

### Adding Cards

Add new cards to any column by extending the `cards` array:

```yaml
cards:
  - id: "new-card"
    title: "New task"
    description: "Task description"
    priority: "medium"
    # ... other properties
```

### Modifying Columns

You can customize columns by:
- Changing names and descriptions
- Adjusting colors
- Setting work-in-progress limits
- Adding new columns

### Priority Levels

- **High**: Critical tasks requiring immediate attention
- **Medium**: Standard priority tasks
- **Low**: Nice-to-have improvements

## Usage Examples

### Project Management
- Track feature development
- Monitor bug fixes
- Manage release cycles

### Team Collaboration  
- Assign tasks to team members
- Track progress across different stages
- Identify bottlenecks in workflow

### Personal Productivity
- Organize personal projects
- Track learning goals
- Manage daily tasks

## Integration

This template can be integrated with:
- Project management tools (Trello, Jira, Asana)
- Development workflows (GitHub Projects, GitLab Boards)
- Custom applications using the JSON/YAML structure

## Contributing

Feel free to:
- Suggest improvements to the template
- Add new column types
- Enhance the HTML visualization
- Create additional formats (CSV, XML, etc.)

## License

This template is provided as-is for educational and project use.
