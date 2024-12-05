#!/usr/bin/env bash

o2-ccdb-upload -f "8c67ff64-b245-11ef-a3bd-7f0000012705.root" --starttimestamp 1730505320000 --endtimestamp 1730506920690 -k "ccdb_object" --path /MID/Calib/RejectList --host alice-ccdb.cern.ch -m "JIRA=[~~O2-5618~~](/jira/browse/O2-5618);comment=Reject list period LHC24aq"
