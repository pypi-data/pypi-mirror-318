import sys


def split_pairs(genes, num_files=4, output_dir='.'):
    gene_pairs = [(genes[i], genes[j]) for i in range(len(genes)) for j in range(i + 1, len(genes))]
    pairs_per_file = len(gene_pairs) // num_files
    for i in range(num_files):
        start = i * pairs_per_file
        end = (i + 1) * pairs_per_file if i < num_files - 1 else len(gene_pairs)
        with open(f'{output_dir}/gene_pairs_{i+1}.txt', 'w') as f:
            for pair in gene_pairs[start:end]:
                f.write(f'{pair[0]},{pair[1]}\n')


def read_list(fn):
    with open(fn, 'r') as f:
        l = f.read().splitlines()
    return l


if __name__ == '__main__':
    target_genes_fn = sys.argv[1]
    select_genes = read_list(target_genes_fn)
    num_files = int(sys.argv[2])
    print(f'Spliting gene pairs into {num_files} files...')
    output_dir = sys.argv[3]
    split_pairs(select_genes, num_files=num_files, output_dir=output_dir)
    print('Spliting Done') 
