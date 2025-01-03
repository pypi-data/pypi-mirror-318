'''utility functions'''

import uuid

def gen_uuid(
    length: int = 8
) -> str:
    '''
        Generating a random UUID

        Parameters:
            length (int): length of the UUID
    '''
    return str(uuid.uuid4())[:length]
