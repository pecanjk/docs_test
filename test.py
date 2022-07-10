from distutils.sysconfig import get_config_h_filename
import string


def test(i:float,a:int=1,**kwargs)-> string :
    """
    Args:
        i (float): _description_
        a (int, optional): _description_. Defaults to 1.

    Returns:
        string: _description_
    """
    #print
    print(a)

    return 'hello'