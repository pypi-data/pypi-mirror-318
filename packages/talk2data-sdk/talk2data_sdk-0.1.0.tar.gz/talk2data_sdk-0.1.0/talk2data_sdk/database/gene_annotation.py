from typing import List, Dict, Optional

from pydantic import BaseModel


class GenesAnnotation(BaseModel):
  """
  Gene names and aliases.
  """
  names: List[str]
  aliases: Dict[str, int]

  def idxs2names(self, idxs: Optional[List[int]]) -> List[str]:
    """
    Convert gene indices to gene names.
    """
    if idxs is None:
      return self.names
    return [self.names[idx] for idx in idxs]

  def get_gene_id(self, gene_name: str) -> int:
    """
    Get the gene ID by gene name.
    """
    if gene_name not in self.aliases:
      raise ValueError(f"Invalid gene name: {gene_name}")
    return self.aliases[gene_name]

  def get_gene_name(self, gene_id: int) -> str:
    """
    Get the gene name by gene ID.
    """
    if gene_id < 0 or gene_id >= len(self.names):
      raise ValueError(f"Invalid gene id: {gene_id}")
    return self.names[gene_id]

  def is_valid_gene_name(self, gene_name: str) -> bool:
    """
    Check if the gene name is valid.
    """
    return gene_name in self.aliases
