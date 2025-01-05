# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# Time       ：2025/1/4 11:05
# Author     ：Maxwell
# Description：
"""
import re
import base64
import json
import yaml
from pathlib import Path
from typing import Dict, Optional
from hwhkit.utils.security.rsa import RSACipher
from hwhkit.utils.security.aes import AESCipher
from hwhkit.connection.mqtt.plugins import PluginBase


class EncryptionPlugin(PluginBase):
    def __init__(self, key_pairs_file: str):
        self.topic_keys: Dict[str, Dict[str, str]] = {}
        self.load_key_pairs(key_pairs_file)

    def clean_key(self, key):
        return re.sub(r'\s+', '', key)

    def load_key_pairs(self, key_pairs_file: str):
        if not Path(key_pairs_file).exists():
            raise FileNotFoundError(f"KeyPairs file not found: {key_pairs_file}")

        with open(key_pairs_file, "r") as f:
            data = yaml.safe_load(f)

        if "key_pairs" not in data:
            raise ValueError("Invalid key_pairs file format: missing 'key_pairs' key")

        for topic, keys in self.topic_keys.items():
            # keys['pub_key'] = self.clean_key(keys['pub_key'])
            # keys['pri_key'] = self.clean_key(keys['pri_key'])
            for k in keys:
                if k == 'public':
                    start = "-----BEGIN PUBLIC KEY-----"
                    end = "-----END PUBLIC KEY-----"
                else:
                    start = "-----BEGIN PRIVATE KEY-----"
                    end = "-----END PRIVATE KEY-----"

                if not k.startswith(start) or not k.endswith(end):
                    raise ValueError(f"Invalid {k} key format")

        self.topic_keys = data["key_pairs"]

    def get_keys(self, topic: str) -> Dict[str, str]:
        if topic not in self.topic_keys:
            raise ValueError(f"No keypair found for topic: {topic}")
        return self.topic_keys[topic]

    def on_message_published(self, topic: str, message: str) -> str:
        try:
            keys = self.get_keys(topic)
            public_key_pem = keys["pub_key"]
            aes_cipher = AESCipher()
            aes_key = aes_cipher.get_key()
            public_key_pem_bytes = public_key_pem.encode('utf-8')
            public_key = RSACipher.deserialize_public_key(public_key_pem_bytes)
            rsa_cipher = RSACipher(public_key=public_key)
            encrypted_aes_key = rsa_cipher.encrypt(aes_key.encode('utf-8'))
            encrypted_message = aes_cipher.encrypt(message)

            payload = {
                "k": base64.b64encode(encrypted_aes_key).decode('utf-8'),
                "v": encrypted_message
            }
            return json.dumps(payload)
        except Exception as e:
            raise ValueError(f"Encryption failed: {str(e)}")

    def on_message_received(self, topic: str, message: str) -> str:
        try:
            keys = self.get_keys(topic)
            private_key_pem = keys["pri_key"]

            payload = json.loads(message)
            if 'k' not in payload or 'v' not in payload:
                raise ValueError("Invalid payload format")

            private_key_pem_bytes = private_key_pem.encode('utf-8')
            private_key = RSACipher.deserialize_private_key(private_key_pem_bytes)
            rsa_cipher = RSACipher(private_key=private_key)
            encrypted_aes_key = base64.b64decode(payload['k'].encode('utf-8'))
            aes_key = rsa_cipher.decrypt(encrypted_aes_key).decode('utf-8')

            aes_cipher = AESCipher(key=base64.b64decode(aes_key))
            return aes_cipher.decrypt(payload['v'])
        except Exception as e:
            raise ValueError(f"Decryption failed: {str(e)}")


