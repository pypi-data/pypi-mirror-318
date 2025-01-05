import io
import torch
import torchaudio

def pad(audio, p=2**16):
    B,C,L = audio.shape
    padding_size = (p - (L % p)) % p
    if padding_size > 0:
        audio = torch.nn.functional.pad(audio, (0, padding_size), mode='constant', value=0)
    return audio

def compress_opus(sample):
    x, fs = torchaudio.load(sample['path'],normalize=False)
    x = x.to(torch.float)
    x = x - x.mean()
    max_abs = x.abs().max()
    x = x / (max_abs + 1e-8)
    x = x/2
    L = x.shape[-1]
    x_padded = pad(x.unsqueeze(0), 3*2**10)[0]
    
    buff = io.BytesIO()
    torchaudio.save(
        uri=buff,
        src=x_padded,
        sample_rate=32000,
        channels_first=True,
        format='opus',
        encoding='OPUS',
        compression=torchaudio.io.CodecConfig(bit_rate=24000)
    )
    opus_bytes = buff.getbuffer()

    # with tempfile.NamedTemporaryFile(delete=False, suffix='.opus') as temp_file:
    #     temp_file.write(opus_bytes)
    #     temp_file_path = temp_file.name
    # x_hat, fs2 = torchaudio.load(temp_file_path,normalize=False)
    # display(Audio(x_hat,rate=fs2))
    
    return {
        'opus': opus_bytes
    }