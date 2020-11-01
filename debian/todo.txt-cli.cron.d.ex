#
# Regular cron jobs for the todo.txt-cli package
#
0 4	* * *	root	[ -x /usr/bin/todo.txt-cli_maintenance ] && /usr/bin/todo.txt-cli_maintenance
