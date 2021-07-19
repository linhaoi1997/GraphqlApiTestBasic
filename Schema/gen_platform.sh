python \
    -m sgqlc.introspection \
    --exclude-deprecated \
    --exclude-description \
    https://test.teletraan.io/graphql/ \
    platform_schema.json || exit 1

sgqlc-codegen schema platform_schema.json platform_schema.py;
#
#get-graphql-schema http://192.168.1.5:11000/graphql/ > ~/graphql/platform_only_eam.graphql
#rm -rf ~/graphql/platform_only_eam
#gqlg --schemaFilePath  ~/graphql/platform_only_eam.graphql --destDirPath ~/graphql/platform_only_eam
