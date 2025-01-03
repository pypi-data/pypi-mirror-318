from vame.logging.logger import VameLogger
from vame.preprocessing.cleaning import lowconf_cleaning, outlier_cleaning
from vame.preprocessing.alignment import egocentrically_align_and_center
from vame.preprocessing.filter import savgol_filtering


logger_config = VameLogger(__name__)
logger = logger_config.logger


def preprocessing(
    config: dict,
    centered_reference_keypoint: str = "snout",
    orientation_reference_keypoint: str = "tailbase",
    save_logs: bool = False,
) -> None:
    """
    Preprocess the data by:
        - Cleaning low confidence data points
        - Egocentric alignment
        - Outlier cleaning
        - Savitzky-Golay filtering

    Parameters
    ----------
    config : dict
        Configuration dictionary.
    centered_reference_keypoint : str, optional
        Keypoint to use as centered reference.
    orientation_reference_keypoint : str, optional
        Keypoint to use as orientation reference.

    Returns
    -------
    None
    """
    # Low-confidence cleaning
    logger.info("Cleaning low confidence data points...")
    lowconf_cleaning(
        config=config,
        read_from_variable="position",
        save_to_variable="position_cleaned_lowconf",
    )

    # Egocentric alignment
    logger.info("Egocentrically aligning and centering...")
    egocentrically_align_and_center(
        config=config,
        centered_reference_keypoint=centered_reference_keypoint,
        orientation_reference_keypoint=orientation_reference_keypoint,
        read_from_variable="position_cleaned_lowconf",
        save_to_variable="position_egocentric_aligned",
    )

    # Outlier cleaning
    logger.info("Cleaning outliers...")
    outlier_cleaning(
        config=config,
        read_from_variable="position_egocentric_aligned",
        save_to_variable="position_processed",
    )

    # Savgol filtering
    logger.info("Applying Savitzky-Golay filter...")
    savgol_filtering(
        config=config,
        read_from_variable="position_processed",
        save_to_variable="position_processed",
    )
