#
# Regular cron jobs for the stipo.1.0 package.
#
0 4	* * *	root	[ -x /usr/bin/stipo.1.0_maintenance ] && /usr/bin/stipo.1.0_maintenance
