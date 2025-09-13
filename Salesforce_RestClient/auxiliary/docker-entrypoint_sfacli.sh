#!/bin/bash
# Salesforce CLIへJWT認証でログインするスクリプト
set -e
SFA_CLI_ALIAS="cli-dev-hub"
# Pythonのsrcディレクトリに移動し証明書のパスを合わせる
cd /sfa_cli/src
echo "Salesforce CLI login start..."
echo "SAF_CONSUMER_ID: ${SAF_CONSUMER_ID}"
echo "SAF_USERNAME: ${SAF_USERNAME}"
echo "SAF_ALIAS: ${SFA_CLI_ALIAS}"
echo "SAF_ACCESS_PEM: ${SAF_ACCESS_PEM}"
sf org login jwt \
--client-id ${SAF_CONSUMER_ID} \
--jwt-key-file ${SAF_ACCESS_PEM} \
--username ${SAF_USERNAME} \
--alias ${SFA_CLI_ALIAS}
echo Aias ${SFA_CLI_ALIAS} was created for the org with username ${SAF_USERNAME}.

exec "$@"