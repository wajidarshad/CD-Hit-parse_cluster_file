import os, itertools
def read_clstr(file_path):

	# parse through the .clstr file and create a dictionary
	# with the sequences per cluster

	# open the cluster file and set the output dictionary
	cluster_file, cluster_dic = open(file_path), {}

	# parse through the cluster file and store the cluster name + sequences in the dictionary
	cluster_groups = (x[1] for x in itertools.groupby(cluster_file, key=lambda line: line[0] == '>'))
	for cluster in cluster_groups:
         name = cluster.next().strip()
         #seqs = [seq.split('>')[1].split('...')[0] for seq in cluster_groups.next()]
         seqs = [seq for seq in cluster_groups.next()]
         cluster_dic[name[1:]] = seqs

	# return the cluster dictionary
	return cluster_dic
def filt_clust_rep_prot(cluster_file_path):
    """
    This fcuntion filter each cluster w.r.t representative protein
    and output a new  dictionary with key as representative protein
    and value as [] or clusterd proteins list.
    """
    input_dict=read_clstr(cluster_file_path)
    new_dict={}
    for key in input_dict.keys():
        if len(input_dict[key])==1:
            new_dict[input_dict[key][0].split('...')[0].split('>')[1]]=[]
        else:
            id_prots=[]
            for prot in input_dict[key]:
                if prot.rstrip().endswith('*'):
                    new_key= prot.split('...')[0].split('>')[1]
                else:
                    id_prots.append(prot.split('>')[1])
            new_dict[new_key]=id_prots
    return new_dict
if __name__ == '__main__':
    dic=filt_clust_rep_prot('cd-hit-out.clstr')
