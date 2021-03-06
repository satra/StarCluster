condor_tmpl = """\
CONDOR_HOST = %(CONDOR_HOST)s
LOCAL_DIR = /var/lib/condor
LOCAL_CONFIG_FILE =
RUN = $(LOCAL_DIR)
LOG     = $(LOCAL_DIR)/log
LOCK = $(LOG)
SPOOL       = $(LOCAL_DIR)/spool
EXECUTE     = $(LOCAL_DIR)/execute
CRED_STORE_DIR = $(LOCAL_DIR)/cred_dir
UID_DOMAIN      = $(CONDOR_HOST)
FILESYSTEM_DOMAIN   = $(CONDOR_HOST)
TRUST_UID_DOMAIN = True
DAEMON_LIST = %(DAEMON_LIST)s
ALLOW_ADMINISTRATOR = $(CONDOR_HOST), node*
ALLOW_OWNER = $(FULL_HOSTNAME), $(ALLOW_ADMINISTRATOR), $(CONDOR_HOST), node*
ALLOW_READ = $(FULL_HOSTNAME), $(CONDOR_HOST), node*
ALLOW_WRITE = $(FULL_HOSTNAME), $(CONDOR_HOST), node*
SCHEDD_HOST = $(CONDOR_HOST)
START = True
SUSPEND = FALSE
PREEMPT = FALSE
KILL = FALSE
DedicatedScheduler = "DedicatedScheduler@$(CONDOR_HOST)"
STARTD_ATTRS = $(STARTD_ATTRS), DedicatedScheduler
SEC_DEFAULT_AUTHENTICATION_METHODS = FS, KERBEROS, GSI, FS_REMOTE
FS_REMOTE_DIR = %(FS_REMOTE_DIR)s
"""
