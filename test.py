import pytorch_lightning as pl
import torch
from torch import Tensor


class Model(pl.LightningModule):
    """Test model."""

    def forward(self, x: Tensor) -> Tensor:
        """Forward with error:

        test.py:9: error: Signature of "forward" incompatible with supertype "LightningModule".
        """
        mean = torch.mean(x)
        return mean

    # def forward(self, *args, **kwargs) -> Tensor:
    #     """Forward without error."""
    #     x = args[0]
    #     mean = torch.mean(x)
    #     return mean
