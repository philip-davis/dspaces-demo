#!/bin/bash

dig demo-dspaces | grep "ANSWER SECTION" -A1 | awk 'NF==5 {print $5}'
