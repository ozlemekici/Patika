# [16,21,11,8,12,22] -> Merge Sort
# Yukarıdaki dizinin sort türüne göre aşamalarını yazınız.
# Big-O gösterimini yazınız.


#        [16,21,11,8,12,22]
#     [16,21,11]      [8,12,22]
#   [16] [21,11]      [8,12] [22]
# [16] [21] [11]      [8] [12] [22]
#   [16] [11,21]      [8,12] [22]
#     [11,16,21]      [8,12,22]
#        [8,11,12,16,21,22]




# Sayı dizimiz değişmediğinden, sadece bölmelere ayırdığımızdan ve her kademede taradığımız eleman sayısı 
# aynı olduğundan O(n) olur. Bu O(n) işlemini de 2^x = n'den logn = x yani logn kere yaparız. 
# Bu nedenle Big-O gösterimi: O(nlogn) şeklindedir