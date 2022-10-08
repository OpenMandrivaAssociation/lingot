#!/bin/sh
curl https://download.savannah.gnu.org/releases/lingot/ 2>/dev/null | grep lingot |sed -ne 's,\.tar\.gz.*,,;s,.*lingot-,,p' | tail -n1

