# HO xApp

Example of a Radio Resource Connected Mobility Control (RC) xApp built using the xDevSM framework.

This xApp subscribes to all CONNECTED E2 nodes exposing both KPM (ranFunctionId=2) and RC (ranFunctionId=3), collects per-node KPM indications, and triggers a handover to move a UE from the most loaded E2 node to the least loaded one.



### Options
```python
  -r <route_file>, --route_file <route_file>
                        path of xApp route file
  -p <plmn>, --plmn <plmn>
                        PLMN ID target cell
  -n <nr_cell_id>, --nr_cell_id <nr_cell_id>
                        NR Cell ID target cell
  -e <event_trigger_period>, --event_trigger <event_trigger_period>
                        event trigger period in seconds
  -s <sst>, --sst <sst>
                        SST
  -l <log_level>, --log_level <log_level>
                        Log level
  -d <sd>, --sd <sd>    SD
  -g <gnb_target>, --gnb_target <gnb_target>
                        comma-separated allowlist of gNB inventory names (default: all CONNECTED)
```
