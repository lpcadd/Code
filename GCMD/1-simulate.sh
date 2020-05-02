sed -i "s/MOF-199/UIO-66/g" `grep MOF-199 -rl ./charge`
wait
sed -i "s/13.170/10.350/g" `grep 13.170 -rl ../`
wait
cd ./charge
wait
sh ~/.gcmc

