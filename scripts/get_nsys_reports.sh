#!/bin/sh


for a in tabnet; do
	if [ -d "$a" ]
	then
		cd $a
		echo "Entering $a"
		outdir="$1/$a"
		mkdir -p $outdir
		for y in *nsys-rep; do
			batch_size=`python3 $CASIO/scripts/get_batch_size_from_name.py $y`
			echo $y" "$batch_size
			$CASIO/scripts/process_nsys.sh $y $batch_size $outdir
		done
		cd ..
	fi
done

