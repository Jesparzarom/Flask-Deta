from deta import Deta
from urllib.error import HTTPError


def verify_setups(key, name, host, type):
    """Verifies the connection to DetaSpace Base or Drive.

    This method checks whether the provided project key and base name are correct, and
    attempts to establish a connection to the specified DetaSpace Base or Drive. If the connection
    is successful, it returns Base or Drive instance; otherwise, it returns Error.
    """

    error_msg = f">>> ERROR in Deta{type}"

    try:
        if not key:
            raise KeyError("The project key has not been provided.")
        
        if not name:
            raise ValueError(f"The {type} has not been provided")
        
        deta_instance = Deta(key)
        deta_type = type  # Base o Drive
        full_instance = getattr(deta_instance, deta_type)(name, host)
        
        # Attempt an internal test to check the connection by fetching an element,
        # either a "Base" or "Drive" depending on the specified Deta type.
        connection = (
            full_instance.fetch(limit=1).items 
            if deta_type == "Base" 
            else full_instance.list(limit=1)['names']
        )
        
        if not connection:
            raise ValueError(
                f"Incorrect {type} Name => {type} '{name}' not found"
            )
        else:
            connection = None
        
        return full_instance
        
    except (HTTPError, KeyError) as e:

        if isinstance(e, KeyError):
            raise KeyError(
                f"{error_msg} ==> Bad key. {e}"
            )
        
        elif isinstance(e, HTTPError):
            raise KeyError(
                f"{error_msg} ==> Key does not exist. {e.msg}"
            )
    
    except (ValueError) as e:
        raise TypeError(f"{error_msg} ==> {e}")

    except Exception as e:
        raise TypeError(f"{error_msg} ==> {e}")
    