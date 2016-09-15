#!/usr/bin/env python
import sys, os, pwd, re, subprocess

def get_settings():
    procname = os.environ['PROCMEM_PROCESS']
    username = os.environ['PROCMEM_USERNAME']
    uid = pwd.getpwnam(username).pw_uid
    print uid
    return procname, username, uid

def proc_cmdline(pid):
    with open(os.path.join("/proc", str(pid), "cmdline"), "r") as f:
        return f.read()

def page_size():
    proc = subprocess.Popen(["getconf", "PAGE_SIZE"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    size, _ = proc.communicate()
    return int(size)

def proc_meminfo(pid):
    with open(os.path.join("/proc", str(pid), "statm"), "r") as f:
        match = re.match(r'(\d+) (\d+)', f.read())
        if match:
            vm_pages = int(match.group(1))
            rss_pages = int(match.group(2))
            ps = page_size()

            return vm_pages * ps, rss_pages * ps
        else:
            raise Exception("Unable to parse statm")

def matching_processes(procname, uid):
    for pid in os.listdir("/proc"):
        dirpath = os.path.join("/proc", pid)
        if os.path.isdir(dirpath) and re.match(r'^\d+$', pid) and os.stat(dirpath).st_uid == uid:
            cmdline = proc_cmdline(pid)
            if cmdline.startswith(procname):
                yield pid

#print(len(sys.argv))
#print sys.argv[1]
#for item in os.environ:
#    print item
#print os.environ['PROCMEM_PROCESS']
#print os.environ['PROCMEM_USERNAME']
if len(sys.argv) == 2:
    if sys.argv[1] == "autoconf":
        print "yes"
    elif sys.argv[1] == "config":
        procname, username, _ = get_settings()
        print "graph_title Memory usage: %s/%s" % (procname, username)
        print "graph_category processes"
        print "graph_args --base 1024 --vertical-label memory -l 0"
        print "vmsize.label VmSize"
        print "vmsize.info Virtual memory size"
        print "rss.label VmRss"
        print "rss.info Resident set size"
else:
    procname, _, uid = get_settings()
    processes = list(matching_processes(procname, uid))
    if len(processes) == 0:
        raise Exception("No matching processes")
    elif len(processes) > 1:
        raise Exception("Multiple matching processes")
    else:
        vm_bytes, rss_bytes = proc_meminfo(processes[0])
        print "vmsize.value %d" % vm_bytes
        print "rss.value %d" % rss_bytes