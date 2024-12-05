#!/usr/bin/env bash

o2-ccdb-upload -f "6d2fe9d3-70e1-11ef-aba2-7f0000010000.root" --starttimestamp 1723140418000 --endtimestamp 1723149167771 -k "ccdb_object" --path /MID/Calib/RejectList --host alice-ccdb.cern.ch -m "JIRA=[~~O2-5343~~](/jira/browse/O2-5343);comment=Reject list period LHC24am"
o2-ccdb-upload -f "7a9057cc-70e1-11ef-aba2-7f0000010000.root" --starttimestamp 1723937142000 --endtimestamp 1723944259932 -k "ccdb_object" --path /MID/Calib/RejectList --host alice-ccdb.cern.ch -m "JIRA=[~~O2-5343~~](/jira/browse/O2-5343);comment=Reject list period LHC24am"