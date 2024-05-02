#!/bin/bash
echo 'Deploying bot-backend procedure'

repository='https://github.com/shamir0xe/bot-manager-backend.git'
app_dir=$(pwd)
output_dir=$app_dir/output
release_dir=$output_dir/releases
release=$(date +"%Y%m%d-%H%M%S")
new_release_dir=$release_dir/$release

echo 'Cloning repository'
[ -d "$release_dir" ] || mkdir -p "$release_dir"
git clone --depth 1 $repository "$new_release_dir" --recursive

echo 'Linking Environments'
rm -rf "$new_release_dir"/configs/env.json || true
ln -nfs "$app_dir"/configs/env.json "$new_release_dir"/configs/env.json

# echo 'Linking Assets'
# rm -rf "$new_release_dir"/assets
# ln -nfs "$app_dir"/assets "$new_release_dir"/assets

echo 'Unlinking previous release'
unlink "$output_dir"/current

echo 'Linking current release'
ln -nfs "$new_release_dir" "$output_dir"/current

# echo 'Stop and remove the previous server'
# cd "$new_release_dir" || exit
# docker container stop bot-backend-container || true
# docker container rm bot-backend-container || true

echo 'running the new container'
cd "$new_release_dir" || exit
docker compose up -d --build

