def Interpolate1(X : float, Y : float, SliderValue : float) -> float :
    """
    Interpolates between two float values X and Y based on a slider value.

    Parameters:
        X (float): The start value.
        Y (float): The end value.
        SliderValue (float): A float between 0 and 1 that determines the weight of interpolation.

    Returns:
        float: The interpolated value.

    Raises:
        ValueError: If SliderValue is not between 0 and 1.
    """
    if SliderValue > 1 or SliderValue < 0 :
        raise ValueError('SliderValue must be a float between 0 and 1.')
    
    return (1 - SliderValue) * X + SliderValue * Y