import sys
import os

files = ['agents.py', 'app.py', 'pipeline.py', 'tools.py']

for f in files:
    print(f"Checking imports in {f}...")
    try:
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
            # This is a very crude way to check imports, but it works for missing packages
            exec(content, {'__name__': '__main__', 'st': type('Mock', (), {'set_page_config': lambda *args, **kwargs: None, 'markdown': lambda *args, **kwargs: None, 'session_state': {}})})
    except ImportError as e:
        print(f"ImportError in {f}: {e}")
    except Exception as e:
        # Ignore other errors for now as we just want to check imports
        print(f"Error in {f}: {e}")
