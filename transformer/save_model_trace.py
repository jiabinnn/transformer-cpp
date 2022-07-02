import torch
from config import MyConfig

config = MyConfig('config/config.ini')

model1_entire_path = config.model1_entire_path
model1_trace_path = config.model1_trace_path
max_len = config.max_len
device = config.device


print('loading', model1_entire_path)
model = torch.load(model1_entire_path).to(device)
model.eval()

demo_encoder_inputs = torch.zeros((1, max_len), dtype=torch.long).to(device)
demo_decoder_inputs = torch.zeros((1, max_len), dtype=torch.long).to(device)
mask = torch.ones((1, max_len), dtype=torch.bool).to(device)

traced_script_module = torch.jit.trace(model, (demo_encoder_inputs, demo_decoder_inputs, mask, mask, mask))
print('saving', model1_trace_path)
traced_script_module.save(model1_trace_path)
print('done')

model2_entire_path = config.model2_entire_path
model2_trace_path = config.model2_trace_path
print('loading', model2_entire_path)
model = torch.load(model2_entire_path).to(device)
model.eval()

traced_script_module = torch.jit.trace(model, (demo_encoder_inputs, demo_decoder_inputs))
print('saving', model2_trace_path)
traced_script_module.save(model2_trace_path)
print('done')
