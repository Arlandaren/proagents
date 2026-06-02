#!/usr/bin/env python3
import os
import sys
import argparse
import fnmatch

REPO_ROOT = os.path.dirname(os.path.abspath(__file__))

def get_all_skills():
    """Scan the repository for all markdown rules, personas, and workflows."""
    skills = []
    for root, _, files in os.walk(REPO_ROOT):
        # Exclude git, assets, templates folders
        if any(p in root for p in [".git", "assets", "templates"]):
            continue
        for f in files:
            if f.endswith(".md") and f not in ["README.md", "CREDITS.md"]:
                full_path = os.path.join(root, f)
                rel_path = os.path.relpath(full_path, REPO_ROOT)
                parts = rel_path.split(os.sep)
                
                # Deduce category and subcategory
                category = parts[0] if len(parts) > 0 else "unknown"
                subcategory = parts[1] if len(parts) > 1 else "unknown"
                name = os.path.splitext(f)[0]
                
                skills.append({
                    "name": name,
                    "filename": f,
                    "rel_path": rel_path,
                    "full_path": full_path,
                    "category": category,
                    "subcategory": subcategory
                })
    return skills

def cmd_list(args):
    skills = get_all_skills()
    if not args.domain:
        # Group by category/subcategory
        stats = {}
        for s in skills:
            cat_key = f"{s['category']}/{s['subcategory']}" if s['subcategory'] != "unknown" else s['category']
            stats[cat_key] = stats.get(cat_key, 0) + 1
        
        print("=== proagents Domains ===")
        for cat, count in sorted(stats.items()):
            print(f"  {cat:<30} ({count} items)")
        print("\nUse 'python proagents.py list <domain>' (e.g. 'personas/engineering') to view items.")
    else:
        domain = args.domain.replace("/", os.sep)
        matching = [s for s in skills if s['rel_path'].startswith(domain)]
        if not matching:
            print(f"No skills found in domain '{args.domain}'")
            return
        
        print(f"=== proagents in '{args.domain}' ===")
        for s in sorted(matching, key=lambda x: x['name']):
            print(f"  {s['name']:<35} | {s['rel_path']}")

def cmd_search(args):
    skills = get_all_skills()
    query = args.query.lower()
    matching = []
    
    for s in skills:
        # Search by filename
        if query in s['name'].lower() or query in s['subcategory'].lower():
            matching.append((s, "Name Match"))
            continue
            
        # Search content
        try:
            with open(s['full_path'], 'r', encoding='utf-8') as f:
                content = f.read().lower()
                if query in content:
                    matching.append((s, "Content Match"))
        except Exception:
            pass
            
    if not matching:
        print(f"No results found for query '{args.query}'")
        return
        
    print(f"=== Search Results for '{args.query}' ({len(matching)} matches) ===")
    for s, match_type in sorted(matching, key=lambda x: x[0]['name']):
        print(f"  {s['name']:<35} | {s['rel_path']:<45} ({match_type})")

def cmd_install(args):
    skills = get_all_skills()
    # Find matching skill
    matches = [s for s in skills if s['name'] == args.name or s['filename'] == args.name]
    
    if not matches:
        # Try fuzzy match
        matches = [s for s in skills if fnmatch.fnmatch(s['name'], f"*{args.name}*")]
        
    if not matches:
        print(f"Error: Skill '{args.name}' not found.")
        sys.exit(1)
        
    if len(matches) > 1:
        print("Multiple matches found. Please specify:")
        for m in matches:
            print(f"  {m['rel_path']}")
        sys.exit(1)
        
    skill = matches[0]
    
    # Read prompt content
    try:
        with open(skill['full_path'], 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)
        
    if args.info:
        print(f"=== Info: {skill['name']} ===")
        print(f"Path: {skill['rel_path']}")
        # Extract preamble/first few lines
        lines = content.split('\n')
        preamble = []
        for line in lines:
            if line.startswith('#'):
                break
            preamble.append(line)
        print('\n'.join(preamble).strip())
        return
        
    if args.stdout:
        print(content)
        return
        
    # Determine target file
    target = args.target
    if args.cursor:
        target = ".cursorrules"
        
    if not target:
        print(f"Error: Specify target file via '--target <file>' or '--cursor' or '--stdout'")
        sys.exit(1)
        
    # Write to target
    try:
        # Check if folder exists
        parent = os.path.dirname(target)
        if parent:
            os.makedirs(parent, exist_ok=True)
            
        with open(target, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Successfully installed '{skill['name']}' to '{target}'!")
    except Exception as e:
        print(f"Error writing target file: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="proagents: CLI tool to list, search, and install AI personas/workflows.")
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    # List command
    list_parser = subparsers.add_parser("list", help="List domains or skills in a domain.")
    list_parser.add_argument("domain", nargs="?", help="Optional domain category (e.g. personas/engineering).")
    
    # Search command
    search_parser = subparsers.add_parser("search", help="Search for rules/personas by keyword.")
    search_parser.add_argument("query", help="Keyword to search for in filename and content.")
    
    # Install command
    install_parser = subparsers.add_parser("install", help="Copy a prompt to a file/IDE config.")
    install_parser.add_argument("name", help="Name of the persona/workflow to install.")
    install_parser.add_argument("--target", help="Local file path to write the prompt to.")
    install_parser.add_argument("--cursor", action="store_true", help="Install directly to local .cursorrules file.")
    install_parser.add_argument("--stdout", action="store_true", help="Output content to standard output.")
    install_parser.add_argument("--info", action="store_true", help="Display metadata and header info about the skill.")
    
    args = parser.parse_args()
    
    if args.command == "list":
        cmd_list(args)
    elif args.command == "search":
        cmd_search(args)
    elif args.command == "install":
        cmd_install(args)

if __name__ == "__main__":
    main()
