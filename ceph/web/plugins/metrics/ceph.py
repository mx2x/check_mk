#!/usr/bin/env python
# -*- encoding: utf-8; py-indent-offset: 4 -*-

#
# (c) 2017 Heinlein Support GmbH
#          Robert Sander <r.sander@heinlein-support.de>
#

# This is free software;  you can redistribute it and/or modify it
# under the  terms of the  GNU General Public License  as published by
# the Free Software Foundation in version 2.  This file is distributed
# in the hope that it will be useful, but WITHOUT ANY WARRANTY;  with-
# out even the implied warranty of  MERCHANTABILITY  or  FITNESS FOR A
# PARTICULAR PURPOSE. See the  GNU General Public License for more de-
# ails.  You should have  received  a copy of the  GNU  General Public
# License along with GNU Make; see the file  COPYING.  If  not,  write
# to the Free Software Foundation, Inc., 51 Franklin St,  Fifth Floor,
# Boston, MA 02110-1301 USA.

metric_info['num_objects'] = {
    'title' : _('Number of Objects'),
    'unit'  : 'count',
    'color' : '51/a',
}

metric_info['num_pgs'] = {
    'title' : _('Number of Placement Groups'),
    'unit'  : 'count',
    'color' : '52/a',
}

_ceph_pgstates = ['pgstate_active_clean',
                  'pgstate_active_clean_scrubbing',
                  'pgstate_active_clean_scrubbing_deep',
                  'pgstate_active_undersized_degraded',
                  'pgstate_active_recovering_degraded',
                  'pgstate_active_recovery_wait_degraded',
                  'pgstate_active_undersized_degraded_remapped_backfilling',
                  'pgstate_active_undersized_degraded_remapped_backfill_wait',
                  'pgstate_peering',
                 ]

_ceph_num_pgstates = len(_ceph_pgstates)

for idx, _ceph_pgstate in enumerate(_ceph_pgstates):
    metric_info[_ceph_pgstate] = {
        'title' : _('PGs %s' % " + ".join(map(lambda x: x.capitalize(), _ceph_pgstate.split('_')[1:]))),
        'unit'  : 'count',
        'color' : indexed_color(idx+1, _ceph_num_pgstates),
    }

#metric_info['pgstates'] = {
#    'title' : _('Placement Groups'),
#    'unit'  : 'count',
#    'color' : '53/a',
#}

check_metrics["check_mk-cephstatus"] = {
    "Status"  : { "name"  : "fs_used", "scale" : MB },
    "fs_size" : { "scale" : MB },
    "growth"  : { "name"  : "fs_growth", "scale" : MB / 86400.0 },
    "trend"   : { "name"  : "fs_trend", "scale" : MB / 86400.0 },
}

check_metrics["check_mk-cephstatus"]['num_objects'] = {}
check_metrics["check_mk-cephstatus"]['num_pgs'] = {}
# check_metrics["check_mk-cephstatus"]['pgstates'] = { 'name': 'pgstates' }
check_metrics["check_mk-cephstatus"]['~pgstate_.*'] = {}

check_metrics["check_mk-cephdf"] = {
    "~(?!inodes_used|fs_size|growth|trend|fs_provisioning|"
      "uncommitted|overprovisioned|pgstate_|num_|disk_).*$"   : { "name"  : "fs_used", "scale" : MB },
    "fs_size" : { "scale" : MB },
    "growth"  : { "name"  : "fs_growth", "scale" : MB / 86400.0 },
    "trend"   : { "name"  : "fs_trend", "scale" : MB / 86400.0 },
}
check_metrics["check_mk-cephdf"]["num_objects"] = {}
check_metrics["check_mk-cephdf"]["disk_read_ios"] = {}
check_metrics["check_mk-cephdf"]["disk_write_ios"] = {}
check_metrics["check_mk-cephdf"]["disk_read_throughput"] = {}
check_metrics["check_mk-cephdf"]["disk_write_throughput"] = {}

check_metrics["check_mk-cephosd"] = df_translation

#graph_info.append({
#    'title'  : _('Placement Groups'),
#    'metrics': [
#        ( 'num_pgs', 'line', _('Total') ),
#        ( 'pgstate_active_clean', 'area', _('Active+Clean') ),
#        ( 'pgstate_active_scrubbing', 'stack', _('Active+Scrubbing') ),
#        ( 'pgstate_active_undersized_degraded', 'stack', _('Active+Undersized+Degraded') ),
#        ],
#    'range'  : (0, 'num_pgs:max'),
#})
