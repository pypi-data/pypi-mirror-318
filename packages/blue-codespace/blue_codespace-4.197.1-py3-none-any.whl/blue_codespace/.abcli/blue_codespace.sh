#! /usr/bin/env bash

function blue_codespace() {
    local task=$(abcli_unpack_keyword $1 version)

    abcli_generic_task \
        plugin=blue_codespace,task=$task \
        "${@:2}"
}

abcli_log $(blue_codespace version --show_icon 1)
