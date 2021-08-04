python \
    -m sgqlc.introspection \
    --exclude-deprecated \
    --exclude-description \
    https://seely.teletraan.io/graphql/ \
    seely_schema.json || exit 1

sgqlc-codegen schema seely_schema.json seely_schema.py;
#
#get-graphql-schema http://192.168.1.5:11000/graphql/ > ~/graphql/platform_only_eam.graphql
#rm -rf ~/graphql/platform_only_eam
#gqlg --schemaFilePath  ~/graphql/platform_only_eam.graphql --destDirPath ~/graphql/platform_only_eam
