from nacl.signing import SigningKey

from nacl.public import (
    SealedBox,
    PrivateKey,
    PublicKey,
    Box
)

from nacl.bindings import (
    crypto_sign_ed25519_sk_to_curve25519,
    crypto_sign_ed25519_pk_to_curve25519
)

def encrypt_mutual_auth(sender_private_key: str, receiver_public_key: str, cleartext_msg: str) -> str:
    """
    Encrypts a message using the sender's private key and the receiver's public key.

    This function creates a mutual-authentication encryption scheme where the sender's
    identity is authenticated via their private key, and the message is encrypted
    such that only the intended receiver with the corresponding private key can decrypt it.

    Args:
        sender_private_key (str): The sender's Ed25519 private key in hexadecimal format.
        receiver_public_key (str): The receiver's Ed25519 public key in hexadecimal format.
        cleartext_msg (str): The plaintext message to encrypt.

    Returns:
        str: The encrypted message as a hexadecimal string.
    """
    ed25519_seed = bytes.fromhex(sender_private_key)
    signing_key = SigningKey(ed25519_seed)

    full_ed25519_sk = ed25519_seed + signing_key.verify_key.encode()
    x25519_sk = crypto_sign_ed25519_sk_to_curve25519(full_ed25519_sk)
    sender_pk = PrivateKey(x25519_sk)

    ed25519_pk = bytes.fromhex(receiver_public_key)
    x25519_pk = crypto_sign_ed25519_pk_to_curve25519(ed25519_pk)
    recipient_pk = PublicKey(x25519_pk)

    box = Box(sender_pk, recipient_pk)
    encrypted = box.encrypt(cleartext_msg.encode('utf-8'))
    return encrypted.hex()


def decrypt_mutual_auth_as_receiver(sender_public_key: str, receiver_private_key: str, encrypted_msg: str) -> str:
    """
    Decrypts a message as the intended receiver using the receiver's private key and sender's public key.

    This function assumes that the message was encrypted using the sender's private key
    and the receiver's public key in a mutual-authentication encryption scheme.

    Args:
        sender_public_key (str): The sender's Ed25519 public key in hexadecimal format.
        receiver_private_key (str): The receiver's Ed25519 private key in hexadecimal format.
        encrypted_msg (str): The encrypted message as a hexadecimal string.

    Returns:
        str: The decrypted plaintext message.
    """
    ed25519_seed = bytes.fromhex(receiver_private_key)
    signing_key = SigningKey(ed25519_seed)
    full_ed25519_sk = ed25519_seed + signing_key.verify_key.encode()

    x25519_sk = crypto_sign_ed25519_sk_to_curve25519(full_ed25519_sk)
    recipient_sk = PrivateKey(x25519_sk)

    ed25519_pk = bytes.fromhex(sender_public_key)
    x25519_pk = crypto_sign_ed25519_pk_to_curve25519(ed25519_pk)
    sender_pk = PublicKey(x25519_pk)

    recipient_box = Box(recipient_sk, sender_pk)
    decrypted_plaintext = recipient_box.decrypt(bytes.fromhex(encrypted_msg))
    return decrypted_plaintext.decode('utf-8')

def decrypt_mutual_auth_as_sender(sender_private_key: str, receiver_public_key: str, encrypted_msg: str) -> str:
    """
    Decrypts a message as the sender using the sender's private key and the receiver's public key.

    This function assumes that the message was encrypted using the receiver's private key
    and the sender's public key, allowing the sender to decrypt it.

    Args:
        sender_private_key (str): The sender's Ed25519 private key in hexadecimal format.
        receiver_public_key (str): The receiver's Ed25519 public key in hexadecimal format.
        encrypted_msg (str): The encrypted message as a hexadecimal string.

    Returns:
        str: The decrypted plaintext message.
    """
    ed25519_seed = bytes.fromhex(sender_private_key)
    signing_key = SigningKey(ed25519_seed)
    full_ed25519_sk = ed25519_seed + signing_key.verify_key.encode()

    x25519_sk = crypto_sign_ed25519_sk_to_curve25519(full_ed25519_sk)
    sender_sk = PrivateKey(x25519_sk)

    ed25519_pk = bytes.fromhex(receiver_public_key)
    x25519_pk = crypto_sign_ed25519_pk_to_curve25519(ed25519_pk)
    receiver_pk = PublicKey(x25519_pk)

    sender_box = Box(sender_sk, receiver_pk)
    decrypted_plaintext = sender_box.decrypt(bytes.fromhex(encrypted_msg))
    return decrypted_plaintext.decode('utf-8')

def encrypt_single_recipient(receiver_public_key: str, cleartext_msg: str) -> str:
    """
    Encrypts a message for a single recipient using only the recipient's public key.

    This function is used for one-way encryption where only the recipient can decrypt
    the message using their private key. The sender's identity is not authenticated.

    Args:
        receiver_public_key (str): The recipient's Ed25519 public key in hexadecimal format.
        cleartext_msg (str): The plaintext message to encrypt.

    Returns:
        str: The encrypted message as a hexadecimal string.
    """
    ed25519_pk_bytes = bytes.fromhex(receiver_public_key)
    x25519_pk_bytes = crypto_sign_ed25519_pk_to_curve25519(ed25519_pk_bytes)
    x25519_pk = PublicKey(x25519_pk_bytes)

    sealed_box = SealedBox(x25519_pk)
    encrypted = sealed_box.encrypt(cleartext_msg.encode('utf-8'))
    return encrypted.hex()

def decrypt_single_recipient(receiver_private_key: str, encrypted_msg: str) -> str:
    """
    Decrypts a one-way encrypted message using the recipient's private key.

    This function assumes the message was encrypted using the recipient's public key,
    allowing only the intended recipient to decrypt it.

    Args:
        receiver_private_key (str): The recipient's Ed25519 private key in hexadecimal format.
        encrypted_msg (str): The encrypted message as a hexadecimal string.

    Returns:
        str: The decrypted plaintext message.
    """
    ed25519_seed = bytes.fromhex(receiver_private_key)
    sk = SigningKey(ed25519_seed)
    x25519_sk = sk.to_curve25519_private_key()

    sealed_box = SealedBox(x25519_sk)
    plaintext = sealed_box.decrypt(bytes.fromhex(encrypted_msg))
    return plaintext.decode('utf-8')
