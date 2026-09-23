class PipelineError(Exception):
    """Base exception for all pipeline-related errors."""
    pass


class FileLoadError(PipelineError):
    """Raised when a file cannot be loaded."""
    pass


class DataValidationError(PipelineError):
    """Raised when input data is invalid."""
    pass


class ProcessingError(PipelineError):
    """Raised when processing fails."""
    pass