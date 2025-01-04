# <img src=./images/logo.png width=40/> Tile Language (tile-lang)

Tile Language (**tile-lang**) is a concise domain-specific language designed to streamline the development of high-performance GPU/CPU kernels (e.g., GEMM, Dequant GEMM, FlashAttention, LinearAttention). By employing a Pythonic syntax with an underlying compiler infrastructure on top of [TVM](https://tvm.apache.org/), tile-lang allows developers to focus on productivity without sacrificing the low-level optimizations necessary for state-of-the-art performance.

## Tested Devices
Although tile-lang aims to be portable across a range of Devices, it has been specifically tested and validated on the following devices:
- **NVIDIA GPUS**: 
    - H100 (**with Auto TMA/WGMMA Support**), 
    - A100
    - V100
    - RTX 4090
    - RTX 3090
    - RTX A600
- **AMD GPUS**:
    - MI250 (**with Auto MatrixCore Support**)
    - MI300 (**with Async Copy Support**)

## OP Implementation Examples
**tile-lang** provides the building blocks to implement a wide variety of operators. Some examples include:

- [Matrix Multiplication](./examples/gemm/)
- [Dequantization GEMM](./examples/dequantize_gemm/)
- [Flash Attention](./examples/flash_attention/)
- [Flash Linear Attention](./examples/linear_attention/)

Within the `examples` repository, you will also find additional complex kernels—such as convolutions, forward/backward passes for FlashAttention.

## Benchmark Summary

TileLang achieves exceptional performance across a variety of computational patterns. Below are selected results showcasing its capabilities:

- Operator Performance Vs. Baselines on H100

  <div>
    <img src="./images/op_benchmark_h100.png" alt="operator performance on H100" />
  </div>

- MatrixCore FP16 GEMM Performance Vs. Baselines on MI300X

  <div>
    <img src="./images/op_benchmark_mi300_fp16_gemm_normalized_latency.png" alt="gemm fp16 performance on MI300X" />
  </div>

## Installation
### Method 1: Install with Pip

The quickest way to get started is to install the latest release from PyPI:

```bash
pip install tilelang
```

Alternatively, you can install directly from the GitHub repository:

```bash
pip install git+https://github.com/microsoft/TileLang
```

Or install locally:

```bash
pip install .  # with -e option if you want to install in editable mode
```

### Method 2: Build from Source
We currently provide three ways to install **tile-lang** from source:
 - [Install from Source (using your own TVM installation)](./docs/Installation.md#install-from-source-with-your-own-tvm-installation)
 - [Install from Source (using the bundled TVM submodule)](./docs/Installation.md#install-from-source-with-our-tvm-submodule)
 - [Install Using the Provided Script](./docs/Installation.md#install-with-provided-script)


## Quick Start

In this section, you’ll learn how to write and execute a straightforward GEMM (matrix multiplication) kernel using tile-lang, followed by techniques for layout optimizations, pipelining, and L2-cache–friendly swizzling.

### Basic GEMM Example

Below is a minimal example showing how to define and run a matrix multiplication kernel in tile-lang. This serves as a gentle introduction to the language’s key concepts.

```python
import tilelang
from tilelang import Profiler
import tilelang.language as T

def matmul(M, N, K, block_M, block_N, block_K, dtype="float16", accum_dtype="float"):
    @T.prim_func
    def main(
        A: T.Buffer((M, K), dtype),
        B: T.Buffer((K, N), dtype),
        C: T.Buffer((M, N), dtype),
    ):
        # Define a GPU kernel launch configuration:
        #   - Grid dimension: (ceildiv(N, block_N), ceildiv(M, block_M))
        #   - Threads per block: 128
        with T.Kernel(T.ceildiv(N, block_N), T.ceildiv(M, block_M), threads=128) as (bx, by):

            # Allocate on-chip memory (shared and fragment buffers)
            A_shared = T.alloc_shared((block_M, block_K), dtype)
            B_shared = T.alloc_shared((block_K, block_N), dtype)
            C_local  = T.alloc_fragment((block_M, block_N), accum_dtype)

            # Initialize the accumulation buffer
            T.clear(C_local)

            # Primary compute loop, with pipelining across chunks of size block_K
            for k in T.Pipelined(T.ceildiv(K, block_K), num_stages=3):
                # Copy a tile of A into shared memory
                T.copy(A[by * block_M, k * block_K], A_shared)
                # Copy a tile of B into shared memory
                T.copy(B[k * block_K, bx * block_N], B_shared)

                # Perform a tile-level GEMM on the shared buffers into C_local
                T.gemm(A_shared, B_shared, C_local)

            # Write the accumulated result from local memory back to global memory
            T.copy(C_local, C[by * block_M, bx * block_N])

    return main

# 1. Define the kernel (matmul) and compile/lower it into an executable module
func = matmul(1024, 1024, 1024, 128, 128, 32)
rt_mod, params = tilelang.lower(func)

# 2. Create a Profiler object for running performance and correctness tests
profiler = Profiler(rt_mod, params, result_idx=[2])

# 3. Test the kernel in Python with PyTorch data
import torch

# Create random input tensors on the GPU
a = torch.randn(1024, 1024, device="cuda", dtype=torch.float16)
b = torch.randn(1024, 1024, device="cuda", dtype=torch.float16)

# Run the kernel through the Profiler
c = profiler(a, b)

# Reference multiplication using PyTorch
ref_c = a @ b

# Validate correctness
torch.testing.assert_close(c, ref_c, rtol=1e-2, atol=1e-2)
print("Kernel output matches PyTorch reference.")

# 4. Retrieve and inspect the generated CUDA source (optional)
cuda_source = rt_mod.imported_modules[0].get_source()
print("Generated CUDA kernel:\n", cuda_source)
```

### Enhanced Example with Annotations (Layout, L2 Cache Swizzling, and Pipelining, etc.)

Below is an example that demonstrates more advanced features: layout annotation, parallelized copy, and swizzle for improved L2 cache locality. This snippet shows how to adapt your kernel to maximize performance on complex hardware.

```python
import tilelang.language as T
# `make_mma_swizzle_layout` is a python defined layout function
# specifically designed for for MMA operations
# which ensures the consistency with the nvidia CUTLASS Library.
# to avoid bank conflicts and maximize the performance.
from tilelang.intrinsics import (
    make_mma_swizzle_layout as make_swizzle_layout,)

def matmul(M, N, K, block_M, block_N, block_K, dtype="float16", accum_dtype="float"):
    @T.prim_func
    def main(
        A: T.Buffer((M, K), dtype),
        B: T.Buffer((K, N), dtype),
        C: T.Buffer((M, N), dtype),
    ):
        # Kernel configuration remains similar
        with T.Kernel(T.ceildiv(N, block_N), T.ceildiv(M, block_M), threads=128) as (bx, by):
            A_shared = T.alloc_shared((block_M, block_K), dtype)
            B_shared = T.alloc_shared((block_K, block_N), dtype)
            C_local  = T.alloc_fragment((block_M, block_N), accum_dtype)

            # Apply layout optimizations or define your own layout
            T.annotate_layout({
                A_shared: make_swizzle_layout(A_shared),
                B_shared: make_swizzle_layout(B_shared),
            })

            # Enable rasterization for better L2 cache locality
            T.use_swizzle(panel_size=10, enable=True)

            # Clear local accumulation
            T.clear(C_local)

            for k in T.Pipelined(T.ceildiv(K, block_K), num_stages=3):
                # Copy tile of A
                T.copy(A[by * block_M, k * block_K], A_shared)

                # Demonstrate parallelized copy from global to shared for B
                for ko, j in T.Parallel(block_K, block_N):
                    B_shared[ko, j] = B[k * block_K + ko, bx * block_N + j]

                # Perform a tile-level GEMM on the shared buffers
                T.gemm(A_shared, B_shared, C_local)

            # Copy result back to global memory
            T.copy(C_local, C[by * block_M, bx * block_N])

    return main
```

### Dive Deep into TileLang Beyond GEMM

In addition to GEMM, we provide a variety of examples to showcase the versatility and power of TileLang, including:

- [Dequantize GEMM](./examples/dequantize_gemm/): Achieve high-performance dequantization by **fine-grained control over per-thread operations**, with many features now adopted as default behaviors in [BitBLAS](https://github.com/microsoft/BitBLAS), which utilzing magic layout transformation and intrins to accelerate dequantize gemm.
- [FlashAttention](./examples/flash_attention/): Enable cross-operator fusion with simple and intuitive syntax, and we also provide an example of auto tuning.
- [LinearAttention](./examples/linear_attention/): Examples include RetNet and Mamba implementations.
- [Convolution](./examples/convolution/): Implementations of Convolution with IM2Col.

More operators will continuously be added.

---

TileLang has now been used in project [BitBLAS](https://github.com/microsoft/BitBLAS).

## Contributing

This project welcomes contributions and suggestions. Most contributions require you to agree to a Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the Microsoft Open Source Code of Conduct. For more information see the Code of Conduct FAQ or contact opencode@microsoft.com with any additional questions or comments.

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft trademarks or logos is subject to and must follow Microsoft's Trademark & Brand Guidelines. Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship. Any use of third-party trademarks or logos are subject to those third-party's policies.

## Acknowledgements

We learned a lot from the [TVM](https://github.com/apache/tvm) community and would like to thank them for their contributions.

This project was initiated by [yining shi](https://github.com/nox-410), and continued by [lei wang](https://github.com/LeiWang1999) and [yu cheng](https://github.com/chengyupku). It was completed under the guidance of [yuqing xia](https://github.com/xiayuqing0622), [lingxiao ma](https://github.com/xysmlx) and [jilong xue](https://github.com/jlxue) from [MSRA System Research Group](https://www.microsoft.com/en-us/research/group/systems-and-networking-research-group-asia/).
