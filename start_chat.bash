#! /bin/bash
source .devel/setup.bash
export CONF_FILE_PATH="./config.yaml"

roslaunch ascent_car top_level_launcher.launch
