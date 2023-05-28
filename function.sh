#! /bin/bash
echo "Enter smallest number: "
read a
echo "Enter largest number: "
read b

prime(){
   if [ $1 -lt 2 ];
     then
       return
   fi
   flag=0
   for((i=2;i<$1;i++)){
       if [ $(( $1 % i )) -eq 0 ];
         then
           flag=$(( flag +1 ))
       fi
   }
   if [ $flag -eq 0 ]; then
       printf "%d " "$1"
   fi
}
printf "Prime Numbers between %d and %d are: " "$a" "$b"
  for((i=a;i<=b;i++)){
   prime $i
}
