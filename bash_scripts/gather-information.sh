#!/bin/bash

echo "Starting at: $(date)"; echo

echo "UPTIME"; uptime; echo

echo "FREE"; sysctl -a | awk '/hw./' && '/mem/'; echo

echo "WHO"; who; echo

echo "Finishing at: $(date)"
