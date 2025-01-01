"""
ether
~~~~~~~~~~~~~~
The web3.py operation wrapper, offering interaction through Wallet instances.

Usage example:
   >>> from ether import Wallet
   ... my_wallet = Wallet('0xPrivateKey', 'Ethereum')
   ... provider = my_wallet.provider
   ... recipient = '0xe977Fa8D8AE7D3D6e28c17A868EF04bD301c583f'
   ... 
   ... usdt = my_wallet.get_token('0xdAC17F958D2ee523a2206206994597C13D831ec7')
   ... usdt_amount = provider.to_wei(0.001, 'ether')
   ...
   ... if my_wallet.get_balance() >= 0.01:
   ...     my_wallet.transfer(usdt, recipient, usdt_amount)

:copyright: (c) 2023 by Belenkov Alexey
:license: MIT, see LICENSE for more details.
"""

from .wallet import Wallet
from .async_wallet import AsyncWallet
from .types import Network, Token
