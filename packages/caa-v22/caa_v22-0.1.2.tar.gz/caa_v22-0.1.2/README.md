# CA-ToMe: Cached Adaptive Token Merging for Efficient Stable Diffusion

This repository contains the official implementation of CA-ToMe (Cached Adaptive Token Merging), a novel optimization technique for accelerating Stable Diffusion inference while maintaining high image quality.

## Overview

CA-ToMe builds upon Token Merging (ToMe) by introducing an adaptive caching mechanism that intelligently merges similar tokens at strategic timesteps during the diffusion process. This approach significantly reduces computational overhead while preserving the quality of generated images.

## Key Features

- **Adaptive Token Merging**: Dynamically merges similar tokens based on cosine similarity thresholds
- **Strategic Caching**: Pre-computed merge patterns at carefully selected timesteps
- **Multiple Configuration Options**: Various checkpoint configurations optimized for different performance-quality tradeoffs
- **Easy Integration**: Simple API to apply CA-ToMe to existing Stable Diffusion pipelines

## Installation
