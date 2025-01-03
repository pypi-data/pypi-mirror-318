# TangoFlux: Super Fast and Faithful Text to Audio Generation with Flow Matching and Clap-Ranked Preference Optimization 

<div align="center">
  <img src="assets/tf_teaser.png" alt="TangoFlux" width="1000" />
  <br/>
  
  [![arXiv](https://img.shields.io/badge/Read_the_Paper-blue?link=https%3A%2F%2Fopenreview.net%2Fattachment%3Fid%3DtpJPlFTyxd%26name%3Dpdf)](https://arxiv.org/abs/2412.21037) [![Static Badge](https://img.shields.io/badge/TangoFlux-Hugging_Face-violet?logo=huggingface&link=https%3A%2F%2Fhuggingface.co%2Fdeclare-lab%2FTangoFlux)](https://huggingface.co/declare-lab/TangoFlux) [![Static Badge](https://img.shields.io/badge/Demos-declare--lab-brightred?style=flat)](https://tangoflux.github.io/) [![Static Badge](https://img.shields.io/badge/TangoFlux-Hugging_Face_Space-8A2BE2?logo=huggingface&link=https%3A%2F%2Fhuggingface.co%2Fspaces%2Fdeclare-lab%2FTangoFlux)](https://huggingface.co/spaces/declare-lab/TangoFlux) [![Static Badge](https://img.shields.io/badge/TangoFlux_Dataset-Hugging_Face-red?logo=huggingface&link=https%3A%2F%2Fhuggingface.co%2Fdatasets%2Fdeclare-lab%2FTangoFlux)](https://huggingface.co/datasets/declare-lab/CRPO) [![Replicate](https://replicate.com/chenxwh/tangoflux/badge)](https://replicate.com/chenxwh/tangoflux)

</div>

## Demos

[![Hugging Face Space](https://img.shields.io/badge/Hugging_Face_Space-TangoFlux-blue?logo=huggingface&link=https%3A%2F%2Fhuggingface.co%2Fspaces%2Fdeclare-lab%2FTangoFlux)](https://huggingface.co/spaces/declare-lab/TangoFlux)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/declare-lab/TangoFlux/blob/main/Demo.ipynb)

## Overall Pipeline

TangoFlux consists of FluxTransformer blocks, which are Diffusion Transformers (DiT) and Multimodal Diffusion Transformers (MMDiT) conditioned on a textual prompt and a duration embedding to generate a 44.1kHz audio up to 30 seconds long. TangoFlux learns a rectified flow trajectory to an audio latent representation encoded by a variational autoencoder (VAE). TangoFlux training pipeline consists of three stages: pre-training, fine-tuning, and preference optimization with CRPO. CRPO, particularly, iteratively generates new synthetic data and constructs preference pairs for preference optimization using DPO loss for flow matching.

![cover-photo](assets/tangoflux.png)

🚀 **TangoFlux can generate 44.1kHz stereo audio up to 30 seconds in ~3 seconds on a single A40 GPU.**

## Installation

```bash
pip install git+https://github.com/declare-lab/TangoFlux
```

## Inference

TangoFlux can generate audio up to 30 seconds long. You must pass a duration to the `model.generate` function when using the Python API. Please note that duration should be between 1 and 30.

### Web Interface

Run the following command to start the web interface:

```bash
tangoflux-demo
```

### CLI

Use the CLI to generate audio from text.

```bash
tangoflux "Hammer slowly hitting the wooden table" output.wav --duration 10 --steps 50
```

### Python API

```python
import torchaudio
from tangoflux import TangoFluxInference

model = TangoFluxInference(name='declare-lab/TangoFlux')
audio = model.generate('Hammer slowly hitting the wooden table', steps=50, duration=10)

torchaudio.save('output.wav', audio, 44100)
```

Our evaluation shows that inference with 50 steps yields the best results. A CFG scale of 3.5, 4, and 4.5 yield similar quality output. Inference with 25 steps yields similar audio quality at a faster speed.

## Training

We use the `accelerate` package from Hugging Face for multi-GPU training. Run `accelerate config` to setup your run configuration. The default accelerate config is in the `configs` folder. Please specify the path to your training files in the `configs/tangoflux_config.yaml`. Samples of `train.json` and `val.json` have been provided. Replace them with your own audio.

`tangoflux_config.yaml` defines the training file paths and model hyperparameters:

```bash
CUDA_VISIBLE_DEVICES=0,1 accelerate launch --config_file='configs/accelerator_config.yaml' tangoflux/train.py   --checkpointing_steps="best" --save_every=5 --config='configs/tangoflux_config.yaml'
```

To perform DPO training, modify the training files such that each data point contains "chosen", "reject", "caption" and "duration" fields. Please specify the path to your training files in `configs/tangoflux_config.yaml`. An example has been provided in `train_dpo.json`. Replace it with your own audio.

```bash
CUDA_VISIBLE_DEVICES=0,1 accelerate launch --config_file='configs/accelerator_config.yaml' tangoflux/train_dpo.py   --checkpointing_steps="best" --save_every=5 --config='configs/tangoflux_config.yaml'
```

## Evaluation Scripts

## TangoFlux vs. Other Audio Generation Models

This key comparison metrics include:

- **Output Length**: Represents the duration of the generated audio.
- **FD**<sub>openl3</sub>: Fréchet Distance.
- **KL**<sub>passt</sub>: KL divergence.
- **CLAP**<sub>score</sub>: Alignment score.


All the inference times are observed on the same A40 GPU. The counts of trainable parameters are reported in the **\#Params** column.

| Model | Params | Duration | Steps | FD<sub>openl3</sub> ↓ | KL<sub>passt</sub> ↓ | CLAP<sub>score</sub> ↑ | IS ↑ | Inference Time (s) |
|---|---|---|---|---|---|---|---|---|
| **AudioLDM 2 (Large)** | 712M | 10 sec | 200 | 108.3 | 1.81 | 0.419 | 7.9 | 24.8 |
| **Stable Audio Open** | 1056M | 47 sec | 100 | 89.2 | 2.58 | 0.291 | 9.9 | 8.6 |
| **Tango 2** | 866M | 10 sec | 200 | 108.4 | 1.11 | 0.447 | 9.0 | 22.8 |
| **TangoFlux (Base)** | 515M | 30 sec | 50 | 80.2 | 1.22 | 0.431 | 11.7 | 3.7 |
| **TangoFlux** | 515M | 30 sec | 50 | 75.1 | 1.15 | 0.480 | 12.2 | 3.7 |

## Citation

```bibtex
@misc{hung2024tangofluxsuperfastfaithful,
      title={TangoFlux: Super Fast and Faithful Text to Audio Generation with Flow Matching and Clap-Ranked Preference Optimization}, 
      author={Chia-Yu Hung and Navonil Majumder and Zhifeng Kong and Ambuj Mehrish and Rafael Valle and Bryan Catanzaro and Soujanya Poria},
      year={2024},
      eprint={2412.21037},
      archivePrefix={arXiv},
      primaryClass={cs.SD},
      url={https://arxiv.org/abs/2412.21037}, 
}
```

## License

TangoFlux is licensed under the MIT License. See the `LICENSE` file for more details.
