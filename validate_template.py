#!/usr/bin/env python3
"""
Simple validation script for the Kanban template
"""

import json
import yaml
import sys

def validate_kanban_structure(data):
    """Validate the basic structure of the kanban board"""
    
    # Check if main structure exists
    if 'kanban_board' not in data:
        return False, "Missing 'kanban_board' root element"
    
    board = data['kanban_board']
    
    # Check required fields
    required_fields = ['name', 'description', 'columns']
    for field in required_fields:
        if field not in board:
            return False, f"Missing required field: {field}"
    
    # Check columns
    columns = board['columns']
    if not isinstance(columns, list):
        return False, "Columns must be a list"
    
    # Check if we have the required columns
    required_columns = ['To do', 'In progress', 'To Test', 'Done']
    column_names = [col['name'] for col in columns]
    
    for req_col in required_columns:
        if req_col not in column_names:
            return False, f"Missing required column: {req_col}"
    
    # Check column structure
    for col in columns:
        if 'name' not in col or 'cards' not in col:
            return False, f"Column {col.get('id', 'unknown')} missing required fields"
        
        # Check cards structure
        for card in col['cards']:
            if 'title' not in card or 'description' not in card:
                return False, f"Card {card.get('id', 'unknown')} missing required fields"
    
    return True, "Kanban structure is valid"

def main():
    print("Validating Kanban Templates...")
    print("=" * 40)
    
    # Test JSON file
    try:
        with open('kanban-template.json', 'r') as f:
            json_data = json.load(f)
        
        valid, message = validate_kanban_structure(json_data)
        print(f"JSON Template: {'✅ VALID' if valid else '❌ INVALID'}")
        print(f"Message: {message}")
        
        # Count cards in each column
        columns = json_data['kanban_board']['columns']
        print("\nColumn Summary:")
        for col in columns:
            print(f"  - {col['name']}: {len(col['cards'])} cards")
        
    except Exception as e:
        print(f"JSON Template: ❌ ERROR - {e}")
    
    print("\n" + "-" * 40)
    
    # Test YAML file
    try:
        with open('kanban-template.yaml', 'r') as f:
            yaml_data = yaml.safe_load(f)
        
        valid, message = validate_kanban_structure(yaml_data)
        print(f"YAML Template: {'✅ VALID' if valid else '❌ INVALID'}")
        print(f"Message: {message}")
        
    except Exception as e:
        print(f"YAML Template: ❌ ERROR - {e}")
    
    print("\n" + "=" * 40)
    print("Validation Complete!")

if __name__ == "__main__":
    main()