HELP_TEXT = """
GEAI CLI
--------

NAME
    geai - Command Line Interface for Globant Enterprise AI

SYNOPSIS
    geai <command> [<subcommand>] [--option] [option-arg]

DESCRIPTION
    geai is a cli utility that interacts with the PyGEAI SDK to handle common tasks in Globant Enterprise AI,
    such as creating organizations and projects, defining assistants, managing workflows, etc.
    
    The available subcommands are as follows:
    {available_commands}
    
    You can consult specific options for each command using with:
    geai <command> h
    or
    geai <command> help
    
EXAMPLES
    The command:
        geai --configure
    will help you setup the required environment variables to work with GEAI.
    
    The command:
        ...
    
AUTHORS 
    Developed and maintained by:
        - Alejandro Trinidad <alejandro.trinidad@globant.com>
        
    Copyright 2024, Globant.
"""

ORGANIZATION_HELP_TEXT = """
GEAI CLI - ORGANIZATION
-----------------------

NAME
    geai - Command Line Interface for Globant Enterprise AI

SYNOPSIS
    geai organization <subcommand> --[flag] [flag_arg]

DESCRIPTION
    geai organization is a command from geai cli utility, developed to interact with key components of GEAI
    such as creating organizations and projects, defining assistants, managing workflows, etc.
    
    The options are as follows:
    {available_commands}
    
EXAMPLES
    The command:
        geai c
    starts an interactive tool to configure API KEY and BASE URL to work with GEAI.
    
    The command:
        geai organization list-projects
    list available projects. For this, an organization API KEY is required.
    
    The command:
        ...
    
AUTHORS 
    Developed and maintained by:
        - Alejandro Trinidad <alejandro.trinidad@globant.com>
        
    Copyright 2024, Globant.
"""

ASSISTANT_HELP_TEXT = """
GEAI CLI - ASSISTANT
-----------------------

NAME
    geai - Command Line Interface for Globant Enterprise AI

SYNOPSIS
    geai assistant <subcommand> --[flag] [flag_arg]

DESCRIPTION
    geai assistant is a command from geai cli utility, developed to interact with assistant in GEAI.
    
    The options are as follows:
    {available_commands}
    
EXAMPLES
    The command:
        
    
    The command:
        ...
    
AUTHORS 
    Developed and maintained by:
        - Alejandro Trinidad <alejandro.trinidad@globant.com>
        
    Copyright 2024, Globant.
"""

CHAT_HELP_TEXT = """
GEAI CLI - CHAT
-----------------------

NAME
    geai - Command Line Interface for Globant Enterprise AI

SYNOPSIS
    geai chat <subcommand> --[flag] [flag_arg]

DESCRIPTION
    geai chat is a command from geai cli utility, developed to chat with assistant in GEAI.
    
    The options are as follows:
    {available_commands}
    
EXAMPLES
    The command:
        
    
    The command:
        ...
    
AUTHORS 
    Developed and maintained by:
        - Alejandro Trinidad <alejandro.trinidad@globant.com>
        
    Copyright 2024, Globant.
"""

ADMIN_HELP_TEXT = """
GEAI CLI - ADMIN
-----------------------

NAME
    geai - Command Line Interface for Globant Enterprise AI

SYNOPSIS
    geai admin <subcommand> --[flag] [flag_arg]

DESCRIPTION
    geai admin is a command from geai cli utility, developed to interact instance of GEAI.
    
    The options are as follows:
    {available_commands}
    
EXAMPLES
    The command:
        
    
    The command:
        ...
    
AUTHORS 
    Developed and maintained by:
        - Alejandro Trinidad <alejandro.trinidad@globant.com>
        
    Copyright 2024, Globant.
"""

CLI_USAGE = """
geai <command> [<subcommand>] [--option] [option-arg]
"""
