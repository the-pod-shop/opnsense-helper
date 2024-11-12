
from  opnsense_helper.utils.exec_class import Exec_Class
Exec_Class
scripts_folder="/usr/local/opnsense/scripts/"

class Scripts():
     def __init__(self,base):
          self.unbound=unbound(base)
          self.system=system(base)
          self.syslog=syslog(base)
          self.suricata=suricata(base)
          self.shell=shell(base)
          self.shaper=shaper(base)
          self.routes=routes(base)
          self.openvpn=openvpn(base)
          self.openssh=openssh(base)
          self.netflow=netflow(base)
          self.ipsec=ipsec(base)
          self.interfaces=interfaces(base)
          self.health=health(base)
          self.firmware=firmware(base)
          self.filter=filter(base)
          self.dns=dns(base)
          self.dhcp=dhcp(base)
          self.auth=auth(base)
          self.Wireguard=Wireguard(base)

class unbound(Exec_Class):
     def __init__(self, base):
          super(Exec_Class).__init__()
          if base is not None:
            self.__dict__.update(base.__dict__)

          self.commands={
          "wrapper":{ "command":scripts_folder+"ubound/wrapper.py*","flags":[]},
          "stats":{ "command":scripts_folder+"ubound/stats.py*","flags":[]},
          "start":{ "command":scripts_folder+"ubound/start.sh*","flags":[]},
          "restore_db":{ "command":scripts_folder+"ubound/restore_db.py*","flags":[]},
          "logger":{ "command":scripts_folder+"ubound/logger.py*","flags":[]},
          "check":{ "command":scripts_folder+"ubound/check.sh*","flags":[]},
          "cache":{ "command":scripts_folder+"ubound/cache.sh*","flags":[]},
          "blocklists":{ "command":scripts_folder+"ubound/blocklists.py*","flags":[]},
          "blocklists":{ "command":scripts_folder+"ubound/blocklists/","flags":[]},
          }
class system(Exec_Class):
     def __init__(self, base):
          super(Exec_Class).__init__()
          if base is not None:
            self.__dict__.update(base.__dict__)

          self.commands={
          "trigger_config_changed_events":{"command":scripts_folder+"system/trigger_config_changed_events.py*", "flags":[]},
          "temperature":{"command":scripts_folder+"system/temperature.sh*", "flags":[]},
          "sysctl":{"command":scripts_folder+"system/sysctl.py*", "flags":[]},
          "status":{"command":scripts_folder+"system/status.php*", "flags":[]},
          "ssl_ciphers":{"command":scripts_folder+"system/ssl_ciphers.py*", "flags":[]},
          "rrd_pfstate_info":{"command":scripts_folder+"system/rrd_pfstate_info.py*", "flags":[]},
          "rfc5246_cipher_suites":{"command":scripts_folder+"system/rfc5246_cipher_suites.csv", "flags":[]},
          "remote_backup":{"command":scripts_folder+"system/remote_backup.php*", "flags":[]},
          "nameservers":{"command":scripts_folder+"system/nameservers.php*", "flags":[]},
          "certctl":{"command":scripts_folder+"system/certctl.py*", "flags":[]},
          "activity":{"command":scripts_folder+"system/activity.py*", "flags":[]},
          }
class syslog(Exec_Class):
     def __init__(self, base):
          super(Exec_Class).__init__()
          if base is not None:
            self.__dict__.update(base.__dict__)

          self.commands={
          "queryLog":{"command":scripts_folder+"syslog/ queryLog.py*", "flags":[]},
          "logformats":{"command":scripts_folder+"syslog/ logformats/", "flags":[]},
          "log_archive":{"command":scripts_folder+"syslog/ log_archive*", "flags":[]},
          "lockout_handler":{"command":scripts_folder+"syslog/ lockout_handler*", "flags":[]},
          "list_applications":{"command":scripts_folder+"syslog/ list_applications.php*", "flags":[]},
          "generate_certs":{"command":scripts_folder+"syslog/ generate_certs*", "flags":[]},
          "clearlog":{"command":scripts_folder+"syslog/ clearlog.php*", "flags":[]},
          }
class suricata(Exec_Class):
     def __init__(self, base):
          super(Exec_Class).__init__()
          if base is not None:
            self.__dict__.update(base.__dict__)

          self.commands={
          "setup":{"command":scripts_folder+"suricata/setup.sh*", "flags":[]},
          "rule-updater":{"command":scripts_folder+"suricata/rule-updater.py*", "flags":[]},
          "queryInstalledRules":{"command":scripts_folder+"suricata/queryInstalledRules.py*", "flags":[]},
          "queryAlertLog":{"command":scripts_folder+"suricata/queryAlertLog.py*", "flags":[]},
          "metadata":{"command":scripts_folder+"suricata/metadata/", "flags":[]},
          "listRuleMetadata":{"command":scripts_folder+"suricata/listRuleMetadata.py*", "flags":[]},
          "listInstallableRulesets":{"command":scripts_folder+"suricata/listInstallableRulesets.py*", "flags":[]},
          "listAlertLogs":{"command":scripts_folder+"suricata/listAlertLogs.py*", "flags":[]},
          "lib":{"command":scripts_folder+"suricata/lib/", "flags":[]},
          "installRules":{"command":scripts_folder+"suricata/installRules.py*", "flags":[]},
          "dropAlertLog":{"command":scripts_folder+"suricata/dropAlertLog.py*", "flags":[]},
          "__init__":{"command":scripts_folder+"suricata/__init__.py*", "flags":[]},
          }
class shell(Exec_Class):
     def __init__(self, base):
          super(Exec_Class).__init__()
          if base is not None:
            self.__dict__.update(base.__dict__)

          self.commands={
          "setports":{"command":scripts_folder+"shell/setports.php*","flags":[]},
          "setaddr":{"command":scripts_folder+"shell/setaddr.php*","flags":[]},
          "restore":{"command":scripts_folder+"shell/restore.sh*","flags":[]},
          "reboot":{"command":scripts_folder+"shell/reboot.php*","flags":[]},
          "ping":{"command":scripts_folder+"shell/ping.php*","flags":[]},
          "password":{"command":scripts_folder+"shell/password.php*","flags":[]},
          "halt":{"command":scripts_folder+"shell/halt.php*","flags":[]},
          "firmware":{"command":scripts_folder+"shell/firmware.sh*","flags":[]},
          "defaults":{"command":scripts_folder+"shell/defaults.php*","flags":[]},
          "banner":{"command":scripts_folder+"shell/banner.php*","flags":[]},
          }
class shaper(Exec_Class):
     def __init__(self, base):
          super(Exec_Class).__init__()
          if base is not None:
            self.__dict__.update(base.__dict__)

          self.commands={
          "update_tables":{"command":scripts_folder+"shaper/update_tables*","flags":[]},
          "lib":{"command":scripts_folder+"shaper/lib/","flags":[]},
          "dummynet_stats":{"command":scripts_folder+"shaper/dummynet_stats.py*","flags":[]},
          }
class routes(Exec_Class):
     def __init__(self, base):
          super(Exec_Class).__init__()
          if base is not None:
            self.__dict__.update(base.__dict__)

          self.commands={
          "show_routes":{"command":scripts_folder+"routes/show_routes.py*","flags":[]},
          "gateways":{"command":scripts_folder+"routes/gateways.php*","flags":[]},
          "gateway_watcher":{"command":scripts_folder+"routes/gateway_watcher.php*","flags":[]},
          "gateway_status":{"command":scripts_folder+"routes/gateway_status.php*","flags":[]},
          "del_route":{"command":scripts_folder+"routes/del_route.py*","flags":[]},
          }
class openvpn(Exec_Class):
     def __init__(self, base):
          super(Exec_Class).__init__()
          if base is not None:
            self.__dict__.update(base.__dict__)

          self.commands={
          "user_pass_verify":{"command":scripts_folder+"openvpn/user_pass_verify.php*", "flags":[]},
          "tls_verify":{"command":scripts_folder+"openvpn/tls_verify.php*", "flags":[]},
          "ovpn_status":{"command":scripts_folder+"openvpn/ovpn_status.py*", "flags":[]},
          "ovpn_service_control":{"command":scripts_folder+"openvpn/ovpn_service_control.php*", "flags":[]},
          "ovpn_event":{"command":scripts_folder+"openvpn/ovpn_event.py*", "flags":[]},
          "kill_session":{"command":scripts_folder+"openvpn/kill_session.py*", "flags":[]},
          "client_disconnect":{"command":scripts_folder+"openvpn/client_disconnect.sh*", "flags":[]},
          "client_connect":{"command":scripts_folder+"openvpn/client_connect.php*", "flags":[]},
          }
class openssh(Exec_Class):
     def __init__(self, base):
          super(Exec_Class).__init__()
          if base is not None:
            self.__dict__.update(base.__dict__)

          self.commands={ 
          "ssh_query":{"command":scripts_folder+"openssh/ssh_query.py*","flags":[]}
          }

class netflow(Exec_Class):
     def __init__(self, base):
          super(Exec_Class).__init__()
          if base is not None:
            self.__dict__.update(base.__dict__)

          self.commands={
          "lib":{"command":scripts_folder+"netflow/lib/","flags":[]},
          "get_top_usage":{"command":scripts_folder+"netflow/get_top_usage.py*","flags":[]},
          "get_timeseries":{"command":scripts_folder+"netflow/get_timeseries.py*","flags":[]},
          "flush_all":{"command":scripts_folder+"netflow/flush_all.sh*","flags":[]},
          "flowd_aggregate_metadata":{"command":scripts_folder+"netflow/flowd_aggregate_metadata.py*","flags":[]},
          "flowd_aggregate":{"command":scripts_folder+"netflow/flowd_aggregate.py*","flags":[]},
          "flowctl_stats":{"command":scripts_folder+"netflow/flowctl_stats.py*","flags":[]},
          "export_details":{"command":scripts_folder+"netflow/export_details.py*","flags":[]},
          "dump_log":{"command":scripts_folder+"netflow/dump_log.py*","flags":[]},
          }
class ipsec(Exec_Class):
     def __init__(self, base):
          super(Exec_Class).__init__()
          if base is not None:
            self.__dict__.update(base.__dict__)

          self.commands={
          "updown_event":{"command":scripts_folder+"ipsec/updown_event.py*","flags":[]},
          "spddelete":{"command":scripts_folder+"ipsec/spddelete.py*","flags":[]},
          "saddelete":{"command":scripts_folder+"ipsec/saddelete.py*","flags":[]},
          "list_status":{"command":scripts_folder+"ipsec/list_status.py*","flags":[]},
          "list_spd":{"command":scripts_folder+"ipsec/list_spd.py*","flags":[]},
          "list_sad":{"command":scripts_folder+"ipsec/list_sad.py*","flags":[]},
          "list_leases":{"command":scripts_folder+"ipsec/list_leases.py*","flags":[]},
          "lib":{"command":scripts_folder+"ipsec/lib/","flags":[]},
          "get_legacy_vti.":{"command":scripts_folder+"ipsec/get_legacy_vti.php*","flags":[]},
          "disconnect":{"command":scripts_folder+"ipsec/disconnect.py*","flags":[]},
          "connect":{"command":scripts_folder+"ipsec/connect.py*","flags":[]},
          }
class interfaces(Exec_Class):
     def __init__(self, base):
          super(Exec_Class).__init__()
          if base is not None:
            self.__dict__.update(base.__dict__)

          self.commands={
          "traffic_top":{"command": scripts_folder+"interfaces/traffic_top.py*", "flags":[]},
          "traffic_stats":{"command": scripts_folder+"interfaces/traffic_stats.php*", "flags":[]},
          "traceroute":{"command": scripts_folder+"interfaces/traceroute.py*", "flags":[]},
          "rtsold_resolvconf":{"command": scripts_folder+"interfaces/rtsold_resolvconf.sh*", "flags":[]},
          "reconfigure_vlans":{"command": scripts_folder+"interfaces/reconfigure_vlans.php*", "flags":[]},
          "reconfigure_vips":{"command": scripts_folder+"interfaces/reconfigure_vips.php*", "flags":[]},
          "reconfigure_neighbors":{"command": scripts_folder+"interfaces/reconfigure_neighbors.php*", "flags":[]},
          "reconfigure_laggs":{"command": scripts_folder+"interfaces/reconfigure_laggs.php*", "flags":[]},
          "ppp-uptime":{"command": scripts_folder+"interfaces/ppp-uptime.sh*", "flags":[]},
          "ppp-rename":{"command": scripts_folder+"interfaces/ppp-rename.sh*", "flags":[]},
          "ppp-linkup":{"command": scripts_folder+"interfaces/ppp-linkup.sh*", "flags":[]},
          "ppp-linkdown":{"command": scripts_folder+"interfaces/ppp-linkdown.sh*", "flags":[]},
          "portprobe":{"command": scripts_folder+"interfaces/portprobe.py*", "flags":[]},
          "ping":{"command": scripts_folder+"interfaces/ping.py*", "flags":[]},
          "mpd":{"command": scripts_folder+"interfaces/mpd.script*", "flags":[]},
          "macinfo":{"command": scripts_folder+"interfaces/macinfo.py*", "flags":[]},
          "list_sockstat":{"command": scripts_folder+"interfaces/list_sockstat.py*", "flags":[]},
          "list_ndp":{"command": scripts_folder+"interfaces/list_ndp.py*", "flags":[]},
          "list_macdb":{"command": scripts_folder+"interfaces/list_macdb.py*", "flags":[]},
          "list_arp":{"command": scripts_folder+"interfaces/list_arp.py*", "flags":[]},
          "ifctl":{"command": scripts_folder+"interfaces/ifctl.sh*", "flags":[]},
          "dhclient":{"command": scripts_folder+"interfaces/dhclient-script*", "flags":[]},
          "carp_set_status":{"command": scripts_folder+"interfaces/carp_set_status.php*", "flags":[]},
          "carp_global_status":{"command": scripts_folder+"interfaces/carp_global_status.php*", "flags":[]},
          "capture":{"command": scripts_folder+"interfaces/capture.py*", "flags":[]},
          }
class health(Exec_Class):
     def __init__(self, base):
          super(Exec_Class).__init__()
          if base is not None:
            self.__dict__.update(base.__dict__)

          self.commands={
          "listReports":{"command":scripts_folder+"health/listReports.py*","flags":[]},
          "flush_rrd":{"command":scripts_folder+"health/flush_rrd.py*","flags":[]},
          "fetchData":{"command":scripts_folder+"health/fetchData.py*","flags":[]},
          }
class firmware(Exec_Class):
     def __init__(self, base):
          super(Exec_Class).__init__()
          if base is not None:
            self.__dict__.update(base.__dict__)

          self.commands={
          "upgrade":{"command":scripts_folder+"firmware/upgrade.sh*","flags":[]},
          "update":{"command":scripts_folder+"firmware/update.sh*","flags":[]},
          "unlock":{"command":scripts_folder+"firmware/unlock.sh*","flags":[]},
          "sync.subr":{"command":scripts_folder+"firmware/sync.subr.sh*","flags":[]},
          "sync":{"command":scripts_folder+"firmware/sync.sh*","flags":[]},
          "security":{"command":scripts_folder+"firmware/security.sh*","flags":[]},
          "running":{"command":scripts_folder+"firmware/running.sh*","flags":[]},
          "resync":{"command":scripts_folder+"firmware/resync.sh*","flags":[]},
          "remove":{"command":scripts_folder+"firmware/remove.sh*","flags":[]},
          "reinstall":{"command":scripts_folder+"firmware/reinstall.sh*","flags":[]},
          "register.":{"command":scripts_folder+"firmware/register.php*","flags":[]},
          "reboot":{"command":scripts_folder+"firmware/reboot.sh*","flags":[]},
          "read":{"command":scripts_folder+"firmware/read.sh*","flags":[]},
          "query":{"command":scripts_folder+"firmware/query.sh*","flags":[]},
          "product.":{"command":scripts_folder+"firmware/product.php*","flags":[]},
          "plugin":{"command":scripts_folder+"firmware/plugin.sh*","flags":[]},
          "lock":{"command":scripts_folder+"firmware/lock.sh*","flags":[]},
          "license":{"command":scripts_folder+"firmware/license.sh*","flags":[]},
          "launcher":{"command":scripts_folder+"firmware/launcher.sh*","flags":[]},
          "latest.":{"command":scripts_folder+"firmware/latest.php*","flags":[]},
          "install":{"command":scripts_folder+"firmware/install.sh*","flags":[]},
          "health":{"command":scripts_folder+"firmware/health.sh*","flags":[]},
          "connection":{"command":scripts_folder+"firmware/connection.sh*","flags":[]},
          "check":{"command":scripts_folder+"firmware/check.sh*","flags":[]},
          "changelog":{"command":scripts_folder+"firmware/changelog.sh*","flags":[]},
          }
class filter(Exec_Class):
     def __init__(self, base):
          super(Exec_Class).__init__()
          if base is not None:
            self.__dict__.update(base.__dict__)

          self.commands={
          "update_tables":{"commands":scripts_folder+"filter/update_tables.py*","flags":[]},
          "update_bogons":{"commands":scripts_folder+"filter/update_bogons.sh*","flags":[]},
          "run_unittests":{"commands":scripts_folder+"filter/run_unittests.py*","flags":[]},
          "rule_stats":{"commands":scripts_folder+"filter/rule_stats.py*","flags":[]},
          "rollback_timer.":{"commands":scripts_folder+"filter/rollback_timer.php*","flags":[]},
          "rollback_cancel.":{"commands":scripts_folder+"filter/rollback_cancel.php*","flags":[]},
          "read_log":{"commands":scripts_folder+"filter/read_log.py*","flags":[]},
          "pftop":{"commands":scripts_folder+"filter/pftop.py*","flags":[]},
          "pftablecount":{"commands":scripts_folder+"filter/pftablecount.py*","flags":[]},
          "pfstatistics":{"commands":scripts_folder+"filter/pfstatistics.py*","flags":[]},
          "list_tables":{"commands":scripts_folder+"filter/list_tables.py*","flags":[]},
          "list_table":{"commands":scripts_folder+"filter/list_table.py*","flags":[]},
          "list_states":{"commands":scripts_folder+"filter/list_states.py*","flags":[]},
          "list_rule_ids":{"commands":scripts_folder+"filter/list_rule_ids.py*","flags":[]},
          "list_pfsync":{"commands":scripts_folder+"filter/list_pfsync.py*","flags":[]},
          "list_osfp":{"commands":scripts_folder+"filter/list_osfp.py*","flags":[]},
          "kill_table":{"commands":scripts_folder+"filter/kill_table.py*","flags":[]},
          "kill_states":{"commands":scripts_folder+"filter/kill_states.py*","flags":[]},
          "find_table_references":{"commands":scripts_folder+"filter/find_table_references.py*","flags":[]},
          "download_geoip":{"commands":scripts_folder+"filter/download_geoip.py*","flags":[]},
          "delete_table":{"commands":scripts_folder+"filter/delete_table.py*","flags":[]},
          }
class dns(Exec_Class):
     def __init__(self, base):
          super(Exec_Class).__init__()
          if base is not None:
            self.__dict__.update(base.__dict__)

          self.commands={
          "query_dns":{"commands":scripts_folder+"dns/query_dns.py*","flags":[]}
          }

class dhcp(Exec_Class):
     def __init__(self, base):
          super(Exec_Class).__init__()
          if base is not None:
            self.__dict__.update(base.__dict__)

          self.commands={
          "unbound_watche":{"command":scripts_folder+"dhcp/unbound_watcher.py*","flags":[]},
          "prefixe":{"command":scripts_folder+"dhcp/prefixes.sh*","flags":[]},
          "prefixes":{"command":scripts_folder+"dhcp/prefixes.php*","flags":[]},
          "get_leases":{"command":scripts_folder+"dhcp/get_leases6.py*","flags":[]},
          "get_lease":{"command":scripts_folder+"dhcp/get_leases.py*","flags":[]},
          "get_kea_lease":{"command":scripts_folder+"dhcp/get_kea_leases.py*","flags":[]},
          "dnsmasq_watche":{"command":scripts_folder+"dhcp/dnsmasq_watcher.py*","flags":[]},
          "cleanup_leases6":{"command":scripts_folder+"dhcp/cleanup_leases6.php*","flags":[]},
          "cleanup_leases4":{"command":scripts_folder+"dhcp/cleanup_leases4.php*","flags":[]},
          }
class auth(Exec_Class):
     def __init__(self, base):
          super(Exec_Class).__init__()
          if base is not None:
            self.__dict__.update(base.__dict__)

          self.commands={
          "list_group_members":{"command":scripts_folder+"auth/list_group_members.php*","flags":[]},
          "add_user":{"command":scripts_folder+"auth/add_user.php*","flags":[]},
          }
class Wireguard(Exec_Class):
     def __init__(self, base):
          super(Exec_Class).__init__()
          if base is not None:
            self.__dict__.update(base.__dict__)

          self.commands={
          "wg_show":{"command":scripts_folder+"wireguard/wg_show.py*","flags":[]},
          "wg-service-control":{"command":scripts_folder+"wireguard/wg-service-control.php*","flags":[]},
          "reresolve-dns":{"command":scripts_folder+"wireguard/reresolve-dns.py*","flags":[]},
          "gen_keypair":{"command":scripts_folder+"wireguard/gen_keypair.py*","flags":[]},
          }