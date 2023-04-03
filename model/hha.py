"""hha exports the containers for the different Happy Home Academy entities."""
from typing import List, Literal, Optional, TypeVar
from model.http import BaseTypeT, BaseDetailTypeT, BaseResponseTypeT



class CategoryDetailTypeT(BaseDetailTypeT):
    """CategoryDetailTypeT is the full container for Happy Home Academy: Category."""
    resource: Literal["hha_category"]


class CollectionDetailTypeT(BaseDetailTypeT):
    """CollectionDetailTypeT is the full container for Happy Home Academy: Collection."""
    resource: Literal["hha_collection"]


class ConceptDetailTypeT(BaseDetailTypeT):
    """ConceptDetailTypeT is the full container for Happy Home Academy: Concept."""
    resource: Literal["hha_concept"]


class SeriesDetailTypeT(BaseDetailTypeT):
    """SeriesDetailTypeT is the full container for Happy Home Academy: Series."""
    resource: Literal["hha_series"]


DetailTypeT = TypeVar("DetailTypeT",
                      CategoryDetailTypeT,
                      CollectionDetailTypeT,
                      ConceptDetailTypeT,
                      SeriesDetailTypeT)


class ResponseBasicCollectionTypeT(BaseResponseTypeT):
    """ResponseBasicCollectionTypeT"""
    collection: Optional[List[BaseTypeT]]


class ResponseDetailTypeT(BaseResponseTypeT):
    """ResponseDetailTypeT"""
    content: Optional[DetailTypeT]
