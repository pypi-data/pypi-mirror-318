#! /usr/bin/env bash

function test_blue_codespace_README() {
    local options=$1

    abcli_eval ,$options \
        blue_codespace build_README
}
