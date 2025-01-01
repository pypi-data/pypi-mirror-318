#! /usr/bin/env bash

function test_blue_codespace_version() {
    local options=$1

    abcli_eval ,$options \
        "blue_codespace version ${@:2}"
}
