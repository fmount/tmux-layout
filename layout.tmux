#!/usr/bin/env bash

CURRENT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
SCRIPTS_DIR="$CURRENT_DIR/scripts"

source "$SCRIPTS_DIR/variables.sh"


layout_options() {
	
	tmux bind-key "${MENU_KEY}" run-shell "${RUN_MENU}"
}


main() {
	layout_options
}
