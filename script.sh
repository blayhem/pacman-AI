if [ "$1" = "" ];then
 1="smallGrid2"
fi
mean=0
for i in 1 2 3 4 5 6 7 8 9 10; do
	# WIN_RATE=$(python pacman.py -p EstimatePacmanMdpAgent -x 200 -n 220 -k 1 -l layouts/minimaxClassic.lay  -a "iterations=100,discount=0.9" -q | grep Rate |cut -d '.' -f 2|cut -d ')' -f 1)
	WIN_RATE=$(python pacman.py -p EstimatePacmanMdpAgent -x 200 -n 220 -k 1 -l $1 -a "iterations=100,discount=0.9" -q | grep Rate|cut -d '(' -f 2|cut -d ')' -f 1)
	if [ "$WIN_RATE" = "1.00" ];then
		WIN_RATE=100
	else
		WIN_RATE=$(echo -e $WIN_RATE|cut -d '.' -f 2)
	fi
	#echo $WIN_RATE
	mean=$(($WIN_RATE+$mean))
	# echo $i
done
echo $(($mean/10))
