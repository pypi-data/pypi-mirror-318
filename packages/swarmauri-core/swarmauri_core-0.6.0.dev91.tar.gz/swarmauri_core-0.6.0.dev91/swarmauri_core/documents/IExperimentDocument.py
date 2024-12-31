from abc import ABC, abstractmethod
from typing import Dict, Any, List, Optional
from datetime import datetime
from swarmauri_core.documents.IDocument import IDocument

class IExperimentDocument(IDocument, ABC):
    """
    Interface for an Experiment Document, extending the general IDocument interface
    with additional properties and methods specific to experimental data.
    """
    @property
    @abstractmethod
    def parameters(self) -> Dict[str, Any]:
        """
        Get the parameters used in the experiment.
        """
        pass

    @parameters.setter
    @abstractmethod
    def parameters(self, value: Dict[str, Any]) -> None:
        """
        Set the parameters used in the experiment.
        """
        pass

    @property
    @abstractmethod
    def results(self) -> Dict[str, Any]:
        """
        Get the results obtained from the experiment.
        """
        pass

    @results.setter
    @abstractmethod
    def results(self, value: Dict[str, Any]) -> None:
        """
        Set the results obtained from the experiment.
        """
        pass

    @property
    @abstractmethod
    def instruction(self) -> str:
        """
        An instructional or descriptive text about what the experiment aims to achieve or how.
        """
        pass

    @instruction.setter
    @abstractmethod
    def instruction(self, value: str) -> None:
        pass

    @property
    @abstractmethod
    def feature_set(self) -> List[Any]:
        """
        Description of the set of features or data used in the experiment.
        """
        pass

    @feature_set.setter
    @abstractmethod
    def feature_set(self, value: List[Any]) -> None:
        pass

    @property
    @abstractmethod
    def version(self) -> str:
        """
        The version of the experiment, useful for tracking iterations and changes over time.
        """
        pass

    @version.setter
    @abstractmethod
    def version(self, value: str) -> None:
        pass

    @property
    @abstractmethod
    def artifacts(self) -> List[str]:
        """
        A list of paths or identifiers for any artifacts generated by the experiment,
        such as models, charts, or data dumps.
        """
        pass

    @artifacts.setter
    @abstractmethod
    def artifacts(self, value: List[str]) -> None:
        pass

    @property
    @abstractmethod
    def datetime_created(self) -> datetime:
        """
        Timestamp marking when the experiment was initiated or created.
        """
        pass

    @datetime_created.setter
    @abstractmethod
    def datetime_created(self, value: datetime) -> None:
        pass

    @property
    @abstractmethod
    def datetime_completed(self) -> Optional[datetime]:
        """
        Timestamp of when the experiment was completed. None if the experiment is still running.
        """
        pass

    @datetime_completed.setter
    @abstractmethod
    def datetime_completed(self, value: Optional[datetime]) -> None:
        pass
