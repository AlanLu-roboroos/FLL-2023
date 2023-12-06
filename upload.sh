#!/bin/bash -e

robots=("dingo")
robot=$1
shift
files=(${@})
folders=("configurations" "modules")

function exit_usage() {
  echo "Usage: $0 robot_name"
  exit $1
}

if [ -z $robot ]; then
  exit_usage -1
fi

if [ ${#files[@]} -gt 0 ]; then
  for file in ${files[@]}; do
    echo -e "Sending $file to ${robot}:~/FLL-2023/$(dirname $file)"
    scp $file robot@${robot}.local:~/FLL-2023/$(dirname $file)
  done
else
  echo -e "\nSending all files to ${robot}:"
  for folder in ${folders[@]}; do
    echo -e "\nSending $folder to ${robot}:~/FLL-2023/$folder"
    scp -r ~/Desktop/FLL-2023/$folder robot@${robot}.local:~/FLL-2023/
  done
  scp ~/Desktop/FLL-2023/*.py robot@${robot}.local:~/FLL-2023/
  [[ $? -eq 0 ]] || (echo "Error sending files to ${robot}"; exit -1)
  # scp -r ~/repo/software/FLL/modules robot@${robot}.local:~/FLL-2023/
  # [[ $? -eq 0 ]] || (echo "Error sending files to ${robot}"; exit -1)
fi

echo "done"
