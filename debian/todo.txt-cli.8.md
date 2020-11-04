% todo.txt(8)
%
% November 2020

# NAME

todo.txt -- A text-bask task management CLI utility

## SYNOPSIS

`todo.txt [-fhpantvV] [-d todo_config] action [task_number]`
` [task_description]`

`todo.txt-cli [-fhpantvV] [-d todo_config] action [task_number]`
` [task_description]`

`todo [-fhpantvV] [-d todo_config] action [task_number]`
` [task_description]`

## DESCRIPTION

This is a command line tool for managing and displaying tasking information.

Tasks are stored in a plain text file using the todo.txt format. There are a
number of tools, across operating systems, that support collaboratively
managing a common tasking file.

## OPTIONS

_-\@_
: Hide context names in list output.  Use twice to show context names
(default).

_-+_
: Hide project names in list output.  Use twice to show project
names (default).

_-c_
: Color mode

_-d_ *CONFIG\_FILE*
: Use a configuration file other than the default ~/.todo/config

_-f_
: Forces actions without confirmation or interactive input

_-h_
: Display a short help message; same as action "shorthelp"

_-p_
: Plain mode turns off colors

_-P_
: Hide priority labels in list output.  Use twice to show
priority labels (default).

_-a_
: Don't auto-archive tasks automatically on completion

_-A_
: Auto-archive tasks automatically on completion

_-n_
: Don't preserve line numbers; automatically remove blank lines
on task deletion

_-N_
: Preserve line numbers

_-t_
: Prepend the current date to a task automatically
when it's added.

_-T_
: Do not prepend the current date to a task automatically
when it's added.

_-v_
: Verbose mode turns on confirmation messages

_-vv_
: Extra verbose mode prints some debugging information and
additional help text

_-V_
: Displays version, license and credits

_-x_
: Disables TODOTXT\_FINAL\_FILTER

## BUILT-IN ACTIONS

  * _add_|_a_ "THING I NEED TO DO +project @context"

    Adds THING I NEED TO DO to your todo.txt file on its own line.

    Project and context notation optional.

    Quotes optional.


  * _addm_ "FIRST THING I NEED TO DO +project1 @context \n
    SECOND THING I NEED TO DO +project2 @context"

    Adds FIRST THING I NEED TO DO to your todo.txt on its own line and

    Adds SECOND THING I NEED TO DO to you todo.txt on its own line.

    Project and context notation optional.

  * _addto_ DEST "TEXT TO ADD"

    Adds a line of text to any file located in the todo.txt directory.

    For example, addto inbox.txt "decide about vacation"

  * _append_ ITEM# "TEXT TO APPEND"

    ```app ITEM# "TEXT TO APPEND"```

    Adds TEXT TO APPEND to the end of the task on line ITEM#.

    Quotes optional.

  * _archive_

    Moves all done tasks from todo.txt to done.txt and removes blank lines.

  * command [ACTIONS]

    Runs the remaining arguments using only todo.sh builtins.

    Will not call any .todo.actions.d scripts.

  * _deduplicate_

    Removes duplicate lines from todo.txt.

  * _del_|_rm_ ITEM# [TERM]

    Deletes the task on line ITEM# in todo.txt.

    If TERM specified, deletes only TERM from the task.

  * _depri_|_dp_ ITEM#[, ITEM#, ITEM#, ...]

    Deprioritizes (removes the priority) from the task(s)

    on line ITEM# in todo.txt.

  * _done_|_do_ ITEM#[, ITEM#, ITEM#, ...]

    Marks task(s) on line ITEM# as done in todo.txt.

  * _help_ [ACTION...]

    Display help about usage, options, built-in and add-on actions,
    or just the usage help for the passed ACTION(s).

  * _list_|_ls_ [TERM...]

    Displays all tasks that contain TERM(s) sorted by priority with line
    numbers.  Each task must match all TERM(s) (logical AND); to display
    tasks that contain any TERM (logical OR), use
    "TERM1\|TERM2\|..." (with quotes), or TERM1\\|TERM2 (unquoted).
    Hides all tasks that contain TERM(s) preceded by a
    minus sign (i.e. -TERM). If no TERM specified, lists entire todo.txt.

  * _listall_|_lsa_ [TERM...]

    Displays all the lines in todo.txt AND done.txt that contain TERM(s)
    sorted by priority with line  numbers.  Hides all tasks that
    contain TERM(s) preceded by a minus sign (i.e. -TERM).  If no
    TERM specified, lists entire todo.txt AND done.txt
    concatenated and sorted.

  * _listaddons_

    Lists all added and overridden actions in the actions directory.

  * _listcon_|_lsc_ [TERM...]

    Lists all the task contexts that start with the @ sign in todo.txt.
    If TERM specified, considers only tasks that contain TERM(s).

  * _listfile_|_lf_ [SRC [TERM...]]

    Displays all the lines in SRC file located in the todo.txt directory,
    sorted by priority with line  numbers.  If TERM specified, lists
    all lines that contain TERM(s) in SRC file.  Hides all tasks that
    contain TERM(s) preceded by a minus sign (i.e. -TERM).
    Without any arguments, the names of all text files in the todo.txt
    directory are listed.

  * _listpri_|_lsp_ [PRIORITIES] [TERM...]

    Displays all tasks prioritized PRIORITIES.
    PRIORITIES can be a single one (A) or a range (A-C).
    If no PRIORITIES specified, lists all prioritized tasks.
    If TERM specified, lists only prioritized tasks that contain TERM(s).
    Hides all tasks that contain TERM(s) preceded by a minus sign
    (i.e. -TERM).

  * _listproj_|_lsprg_ [TERM...]

    Lists all the projects (terms that start with a + sign) in
    todo.txt.
    If TERM specified, considers only tasks that contain TERM(s).

  * _move_|_mv_ ITEM# DEST [SRC]

    Moves a line from source text file (SRC) to destination text file (DEST).
    Both source and destination file must be located in the directory defined
    in the configuration directory.  When SRC is not defined
    it's by default todo.txt.

  * _prepend_|_prep_ ITEM# "TEXT TO PREPEND"

    Adds TEXT TO PREPEND to the beginning of the task on line ITEM#.
    Quotes optional.

  * _pri_|_p_ ITEM# PRIORITY

    Adds PRIORITY to task on line ITEM#.  If the task is already
    prioritized, replaces current priority with new PRIORITY.
    PRIORITY must be a letter between A and Z.

  * _replace_ ITEM# "UPDATED TODO"

    Replaces task on line ITEM# with UPDATED TODO.

  * _report_

    Adds the number of open tasks and done tasks to report.txt.

  * _shorthelp_

    List the one-line usage of all built-in and add-on actions.

## TODO.TXT TASK FORMAT

A todo.txt task is a single line of text, which may contain specially notated
words to define metadata for the task. These tags are all optional.

  * (\<PRIORITY\>)

    A task _priority_ can be defined by prepending a single letter in
    parenthesis, followed by a space. By convention, capital letters are used,
    with 'A' denoting the highest priority.

  * +\<PROJECT\>

    A word in the task beginning with "+" defines the _project_ associated with
    the task. This provides a means to group tasks according to the tasks
    assocated with a particular effort.

  * @\<CONTEXT\>

    A word in the task beginning with the "@" character defines the _context_
    associated with the task. Possible contexts are @phone, @email, or @home.
    This provides a means to group tasks according to the context of when they
    can be completed.

  * due:\<yyyy-mm-dd\>

    Define the due date of the task.

  * x \<TASK\>

    A task may be marked complete by prepending an "x" followed by a space.
    This is used by the utility to remove tasks from active task lists without
    affecting the line numbers of the remaining tasks.

A task may also contain one or two bare dates that define the creation and
completion date of the task. A completed task should have the completion date
following the "x".

The core todo.txt format is described in full at
https://github.com/todotxt/todo.txt.

## CONFIGURATION FILE

The global configuration file is at /etc/todo/config. It may be overriden by a
file at ~/todo.cfg, ~/.todo.cfg, ~/.config/todo/config, or a file named
todo.cfg in the same directory as the script. The configuration file location
may also be specified in the command line using the "-d" option.
