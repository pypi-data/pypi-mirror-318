#! /usr/bin/env bash

function test_blue_codespace_help() {
    local options=$1

    local module
    for module in \
        "@codespace" \
        \
        "@codespace pypi" \
        "@codespace pypi browse" \
        "@codespace pypi build" \
        "@codespace pypi install" \
        \
        "@codespace pytest" \
        \
        "@codespace test" \
        "@codespace test list" \
        \
        "@codespace browse" \
        \
        "blue_codespace"; do
        abcli_eval ,$options \
            abcli_help $module
        [[ $? -ne 0 ]] && return 1

        abcli_hr
    done

    return 0
}
