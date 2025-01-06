# test_xmss.py
import xmssmt_wrapper as xmssmt

from xmssmt import XMSSMT


def set_ots_index(params, sk, new_index):
    
    """
    Set the OTS index in the secret key.

    Parameters:
        params (XmssParams): The XMSS parameters.
        sk (bytearray): The secret key as a mutable bytearray.
        new_index (int): The new OTS index to set.

    Raises:
        ValueError: If the new index is invalid.
    """
    sk = bytearray(sk)
    # Determine the number of bytes used for the index
    index_bytes = params.get_index_bytes()

    # Compute the maximum index (total number of signatures - 1)
    max_index = (2 ** params.get_height()) - 1

    # Extract the current index
    current_index = int.from_bytes(sk[:index_bytes], byteorder='big')

    # Validate the new index
    if new_index < current_index:
        raise ValueError("New index cannot be less than the current index to prevent OTS key reuse.")
    if new_index > max_index:
        raise ValueError(f"New index exceeds maximum index {max_index}.")

    # Convert the new index to bytes (big-endian)
    new_index_bytes = new_index.to_bytes(index_bytes, byteorder='big')

    # Update the index in the secret key
    sk[:index_bytes] = new_index_bytes
    return sk



def get_ots_index_and_remaining_signatures(params, sk):
    """
    Extract the OTS index from the secret key and compute remaining signatures.

    Parameters:
        params (XmssParams): The XMSS parameters.
        sk (bytes): The secret key.

    Returns:
        index (int): The current OTS index.
        remaining_signatures (int): The number of signatures remaining.
    """
    # Determine the number of bytes used for the index
    index_bytes = params.get_index_bytes()

    # Extract the index bytes from the secret key
    index_bytes_value = sk[:index_bytes]

    # Convert the bytes to an integer (assuming big-endian)
    index = int.from_bytes(index_bytes_value, byteorder='big')

    # Compute the total number of signatures
    total_signatures = 2 ** params.get_height()

    # Compute the number of remaining signatures
    remaining_signatures = total_signatures - index

    return index, remaining_signatures



def main():
    # Convert parameter string to OID
    param_str = "XMSSMT-SHA2_20/2_192"
    try:
        oid = xmssmt.str_to_oid(param_str)
        print(f"OID for '{param_str}': {oid}")
    except ValueError as e:
        print(f"Error converting string to OID: {e}")
        return

    # Initialize parameters
    try:
        params = xmssmt.XmssParams(oid)
        n = params.get_n()
        print(f"Parameter n: {n}")
    except ValueError as e:
        print(f"Error initializing parameters: {e}")
        return

    # Generate seed
    seed = b'\x00' * n  # Example seed; in practice, use a secure random seed

    # Generate keypair
    try:
        pk, sk = xmssmt.core_seed_keypair(params, seed)
        print(f"Public Key ({len(pk)} bytes): {pk.hex()}")
        print(f"Secret Key ({len(sk)} bytes): {sk.hex()}")
    except ValueError as e:
        print(f"Error generating keypair: {e}")
        return
    

    ots_idx, rs = get_ots_index_and_remaining_signatures(params, sk)
    print(f'-> {ots_idx}, {rs}')

    # Message to sign
    message = b"Hello, XMSS!"
    print(f'-> sign message: {message}')
    # Generate signature
    try:
        signature = xmssmt.core_sign(params, sk, message)
        print(f"Signature ({len(signature)} bytes): {signature.hex()}")
    except ValueError as e:
        print(f"Error signing message: {e}")
        return

    ots_idx, rs = get_ots_index_and_remaining_signatures(params, sk)
    print(f'-> {ots_idx}, {rs}')

    # Verify signature
    try:
        original_message = xmssmt.core_sign_open(params, pk, signature)
        print(f"Original message: {original_message}")
        if original_message == message:
            print("Signature verification succeeded.")
        else:
            print("Signature verification failed.")
    except ValueError as e:
        print(f"Error verifying signature: {e}")
        return
    
    new_ots_idx = 100
    sk = set_ots_index(params, sk, new_ots_idx)

    ots_idx, rs = get_ots_index_and_remaining_signatures(params, sk)
    print(f'-> after new OTS={new_ots_idx}: {ots_idx}, {rs}')





if __name__ == "__main__":
    #main()
    seed = [i for i in range(48)] #b'\x00' * 24
    xmss = XMSSMT(seed)

    message = b"Hello, XMSS!"
    signature = xmss.sign(message)
    print(f"Signature: {signature.hex()}")

    result = XMSSMT.validate_signature(message, signature, xmss.pk)
    if result:
        print("Signature verification succeeded.")
    else:
        print("Signature verification failed.")

    rs = xmss.getRemainingSignatures()
    ots_idx = xmss.getIndex()
    print(f'-> {ots_idx}, {rs}')

    new_ots_idx = 100
    xmss.setIndex(new_ots_idx)
    rs = xmss.getRemainingSignatures()
    ots_idx = xmss.getIndex()
    print(f'->after setting OTS={new_ots_idx}: {ots_idx}, {rs}')

