import anndata as ad

## VIASH START
par = {
    'input_train': 'resources_test/task_denoising/cxg_immune_cell_atlas/train.h5ad',
    'input_test': 'resources_test/task_denoising/cxg_immune_cell_atlas/test.h5ad',
    'output': 'output_PD.h5ad',
}
meta = {
    'name': 'foo',
}
## VIASH END

print("Load input data", flush=True)
input_train = ad.read_h5ad(par['input_train'])
input_test = ad.read_h5ad(par['input_test'])

print("Process data", flush=True)
input_train.layers["denoised"] = input_test.layers['counts']

input_train.uns["method_id"] = meta['name']

print("Write Data", flush=True)
input_train.write_h5ad(par['output'],compression="gzip")
