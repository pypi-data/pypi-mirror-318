# Agentis Framework

A comprehensive toolkit for Solana blockchain interactions, offering seamless integration of DeFi operations, token management, and AI-powered automation.

## Core Capabilities

### Token Management 🪙
- Execute SOL and SPL token transfers
- Monitor wallet balances
- Participate in SOL staking
- Create custom tokens
- Access development funds via faucet
- Manage token accounts (burn/close operations)
- Perform bulk token account maintenance

### DeFi Operations 💱
- Seamless Jupiter DEX integration
- Execute token swaps with configurable slippage
- Access direct routing capabilities
- Interface with Raydium liquidity pools

### Yield Generation 🏦
- Access Lulo lending protocols
- Earn passive income on idle assets

### AI Integration 🔗
- Leverage LangChain's intelligent tools
- Automate blockchain interactions
- Access comprehensive tooling for financial operations

### Network Analytics 📈
- Monitor Solana network performance
- Track real-time TPS (Transactions Per Second)

### Token Intelligence 📊
- Retrieve token information via symbol
- Access token data through address lookup

### Token Launch Tools 🚀
- Deploy Pump & Fun tokens
- Customize token parameters

### Liquidity Management 🏦
- Configure and deploy Meteora DLMM pools
- Fine-tune pool parameters

## Getting Started

### Setup
```bash
pip install agentis
```

### Basic Configuration
```python
from agentis import SolanaAgentKit, create_solana_tools

# Initialize framework
agent = SolanaAgentKit(
    private_key="your-base58-private-key",
    rpc_url="https://api.mainnet-beta.solana.com",
    openai_key="your-openai-api-key"
)

# Set up AI tools
tools = create_solana_tools(agent)
```

## Implementation Examples

### Price Discovery
```python
from agentis import SolanaAgentKit

async def main():
    agent = SolanaAgentKit(
        private_key="your-base58-private-key",
        rpc_url="https://api.mainnet-beta.solana.com",
        openai_key="your-openai-api-key"
    )

    price = await agent.fetch_price("FKMKctiJnbZKL16pCmR7ig6bvjcMJffuUMjB97YD7LJs")
    print(f"Current Price: {price} SOL")

import asyncio
asyncio.run(main())
```

### Token Exchange
```python
from agentis import SolanaAgentKit
from solders.pubkey import Pubkey

async def main():
    agent = SolanaAgentKit(
        private_key="your-base58-private-key",
        rpc_url="https://api.mainnet-beta.solana.com",
        openai_key="your-openai-api-key"
    )

    tx_sig = await agent.trade(
        agent,
        output_mint=Pubkey.from_string("target-token-mint"),
        input_amount=100,
        input_mint=Pubkey.from_string("source-token-mint"),
        slippage_bps=300  # 3% slippage tolerance
    )

import asyncio
asyncio.run(main())
```

### Asset Lending
```python
from agentis import SolanaAgentKit

async def main():
    agent = SolanaAgentKit(
        private_key="your-base58-private-key",
        rpc_url="https://api.mainnet-beta.solana.com",
        openai_key="your-openai-api-key"
    )
    
    tx_sig = await agent.lend_assets(amount=100)

import asyncio
asyncio.run(main())
```

### SOL Staking
```python
from agentis import SolanaAgentKit

async def main():
    agent = SolanaAgentKit(
        private_key="your-base58-private-key",
        rpc_url="https://api.mainnet-beta.solana.com",
        openai_key="your-openai-api-key"
    )

    tx_sig = await agent.stake(amount=1)  # Stakes 1 SOL

import asyncio
asyncio.run(main())
```

### Development Fund Access
```python
from agentis import SolanaAgentKit

async def main():
    agent = SolanaAgentKit(
        private_key="your-base58-private-key",
        rpc_url="https://api.mainnet-beta.solana.com",
        openai_key="your-openai-api-key"
    )

    result = await agent.request_faucet_funds()
    print(result)

import asyncio
asyncio.run(main())
```

### Network Performance Monitoring
```python
from agentis import SolanaAgentKit

async def main():
    agent = SolanaAgentKit(
        private_key="your-base58-private-key",
        rpc_url="https://api.mainnet-beta.solana.com",
        openai_key="your-openai-api-key"
    )

    current_tps = await agent.get_tps()
    print(f"Network TPS: {current_tps}")

import asyncio
asyncio.run(main())
```

### Token Data Retrieval
```python
from agentis import SolanaAgentKit

async def main():
    agent = SolanaAgentKit(
        private_key="your-base58-private-key",
        rpc_url="https://api.mainnet-beta.solana.com",
        openai_key="your-openai-api-key"
    )

    # By symbol
    sol_data = await agent.get_token_data_by_ticker("SOL")
    print(sol_data)

    # By address
    token_data = await agent.get_token_data_by_address("token-mint-address")
    print(token_data)

import asyncio
asyncio.run(main())
```

### Token Launch
```python
from agentis import SolanaAgentKit
from agentis.types import PumpfunTokenOptions

async def main():
    agent = SolanaAgentKit(
        private_key="your-base58-private-key",
        rpc_url="https://api.mainnet-beta.solana.com",
        openai_key="your-openai-api-key"
    )

    options = PumpfunTokenOptions()
    result = await agent.launch_pump_fun_token(
        token_name="MyToken",
        token_ticker="MTK",
        description="Example token description",
        image_url="https://example.com/token.png",
        options=options
    )
    print(result)

import asyncio
asyncio.run(main())
```

### DLMM Pool Creation
```python
from agentis import SolanaAgentKit
from solders.pubkey import Pubkey
from agentis.utils.meteora_dlmm.types import ActivationType

async def main():
    agent = SolanaAgentKit(
        private_key="your-base58-private-key",
        rpc_url="https://api.mainnet-beta.solana.com",
        openai_key="your-openai-api-key"
    )

    result = await agent.create_meteora_dlmm_pool(
        bin_step=1,
        token_a_mint=Pubkey.from_string("token-a-mint"),
        token_b_mint=Pubkey.from_string("token-b-mint"),
        initial_price=1.0,
        price_rounding_up=True,
        fee_bps=30,
        activation_type=ActivationType.Timestamp,
        has_alpha_vault=True,
        activation_point=None
    )
    print(result)

import asyncio
asyncio.run(main())
```

## Core Functions Reference

### Asset Operations
- `transfer()`: Execute token transfers
- `trade()`: Perform token swaps
- `get_balance()`: Check wallet balances
- `lend_asset()`: Lend assets via Lulo
- `stake()`: Participate in SOL staking
- `request_faucet_funds()`: Access development funds
- `deploy_token()`: Create new tokens
- `fetch_price()`: Retrieve token prices

### Analytics & Data
- `get_tps()`: Monitor network performance
- `get_token_data_by_ticker()`: Token lookup by symbol
- `get_token_data_by_address()`: Token lookup by address

### Advanced Features
- `launch_pump_fun_token()`: Deploy custom tokens
- `create_meteora_dlmm_pool()`: Configure liquidity pools
- `buy_with_raydium()`: Execute Raydium purchases
- `sell_with_raydium()`: Execute Raydium sales
- `burn_and_close_accounts()`: Manage token accounts
- `multiple_burn_and_close_accounts()`: Bulk account management

## Technical Requirements

Essential dependencies:
- solana-py
- spl-token-py

## Community Participation

We welcome contributions! Feel free to submit pull requests.

## Licensing

ISC License

## Security Advisory

Exercise caution with private keys and ensure secure implementation practices.
