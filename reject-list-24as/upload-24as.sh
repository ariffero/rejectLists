#!/usr/bin/env bash

o2-ccdb-upload -f "d75d0332-b3b1-11ef-9952-7f0000012705.root" --starttimestamp 1732158754000 --endtimestamp 1732171096659 -k "ccdb_object" --path /MID/Calib/RejectList --host alice-ccdb.cern.ch -m "JIRA=[~~O2-5622~~](/jira/browse/O2-5622);comment=Reject list period LHC24as"
