# CD-Hit file Parser
# what is CD-HIT?
CD-HIT clusters proteins into clusters that meet a user-defined similarity threshold, usually a
sequence identity. Each cluster has one representative sequence. The input is a protein dataset in
fasta format and the output are two files: a fasta file of representative sequences and a text file of list
of clusters.
# What this code does?
This code takes a cluster file(.clstr) as input and returns a dictionary with the representaive sequence id as key and all the clustered sequence ids as values in the form of list.
# Example
Input: cluster file containing following clusters.
>Cluster 0
0	26926aa, >01787|01787_1|NP_003310.3|Titin... at 86.16%
1	33423aa, >01787|01787_2|NP_596869.3|Titin... *
2	5604aa, >01787|01787_3|NP_596870.2|Titin... at 67.70%
3	27051aa, >01787|01787_4|NP_597676.2|Titin... at 86.06%
4	27118aa, >01787|01787_5|NP_597681.2|Titin... at 85.88%
>Cluster 1
0	1148aa, >07548|07548_1|BAB14899.1|Mucin... at 99.30%
1	14507aa, >07548|07548_2|NP_078966.2|Mucin... *
>Cluster 2
0	8797aa, >09762|09762_1|NP_892006.2|Synaptic... *
1	982aa, >09762|09762_2|NP_598411.2|Synaptic... at 59.27%
2	8749aa, >09762|09762_3|NP_149062.1|Synaptic... at 58.27%
3	3321aa, >09762|09762_4|NP_056108.2|Synaptic... at 100.00%

Output:
{'01787|01787_2|NP_596869.3|Titin': ['01787|01787_1|NP_003310.3|Titin... at 86.16%','01787|01787_3|NP_596870.2|Titin... at 67.70%','01787|01787_4|NP_597676.2|Titin... at 86.06%','01787|01787_5|NP_597681.2|Titin... at 85.88%'],'07548|07548_2|NP_078966.2|Mucin':['07548|07548_1|BAB14899.1|Mucin... at 99.30%'], '09762|09762_1|NP_892006.2|Synaptic':['09762|09762_2|NP_598411.2|Synaptic... at 59.27%','09762|09762_3|NP_149062.1|Synaptic... at 58.27%','09762|09762_4|NP_056108.2|Synaptic... at 100.00%']}


