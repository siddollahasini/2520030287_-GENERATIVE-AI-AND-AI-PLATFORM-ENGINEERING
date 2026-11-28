                              Week 8 – Generative AI Programming Practical

Title:
**Implement Scaled Dot-Product Attention and Multi-Head Attention from Scratch Using PyTorch**

Aim"
To implement Scaled Dot-Product Attention and Multi-Head Attention mechanisms using PyTorch and understand how attention weights are calculated and applied to input representations.

Technologies Used:
-Python 3.12
-PyTorch
-VS Code

Requirements:
-Python 3.12
-PyTorch
-NumPy (optional, to avoid the NumPy initialization warning)

Program Structure

```text
Week-08/
│
├── main.py
├── requirements.txt
├── README.md
└── Week8_Output.png
```

Implementation:
1.Scaled Dot-Product Attention
-Calculate Query and Key transpose.
-Calculate attention scores using matrix multiplication.
-Scale the scores using the square root of the key dimension.
-Apply causal masking if required.
-Convert scores into attention weights using Softmax.
-Multiply attention weights with Value to generate the output.

2.Multi-Head Attention
-Generate Query, Key and Value using linear layers.
-Split the embeddings into multiple attention heads.
-Apply Scaled Dot-Product Attention to each head.
-Combine all attention heads.
-Apply the final linear projection to generate the output.

Installation:

Install the required packages:

```bash
python -m pip install -r requirements.txt
```

If NumPy is not installed:

```bash
python -m pip install numpy
```

Execution:
Run the Python program:

```bash
python main.py
```

Expected Output:
The program displays:
1.Query Shape
2.Key Shape
3.Value Shape
4.Attention Weights
5.Attention Output
6.Multi-Head Attention Output
7.Output Shapes

Output Shapes:
| Component | Shape |
|---|---|
| Query | (1, 3, 4) |
| Key | (1, 3, 4) |
| Value | (1, 3, 4) |
| Attention Output | (1, 3, 4) |
| Input Embeddings | (1, 3, 8) |
| Attention Weights | (1, 2, 3, 3) |
| Multi-Head Output | (1, 3, 8) |

Result:
Successfully implemented and executed Scaled Dot-Product Attention and Multi-Head Attention from scratch using PyTorch.
Both attention mechanisms generated the expected output shapes successfully.
