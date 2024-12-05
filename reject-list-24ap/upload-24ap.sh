#!/usr/bin/env bash

o2-ccdb-upload -f "82588d42-b245-11ef-a3bd-7f0000012705.root" --starttimestamp 1730345009000 --endtimestamp 1730351020519 -k "ccdb_object" --path /MID/Calib/RejectList --host alice-ccdb.cern.ch -m "JIRA=[~~O2-5616~~](/jira/browse/O2-5616);comment=Reject list period LHC24ap"
