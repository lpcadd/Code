sed -i "s/0.738283/0.313959/g" `grep 0.738283 -rl ../`
wait
cd ./adsorption
wait
sh ~/.gcmc &
wait
