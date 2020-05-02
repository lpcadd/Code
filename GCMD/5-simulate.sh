cd ./adsorption/Output/System_0
wait
ls | xargs sed -n "/Average loading absolute \[molecules\/unit cell\]/p" > ../../../adsoption.log
wait
cd -
