from fastapi import FastAPI
from sallmon.sallmon_core.routes.api import router as api_router  # Import API router
from sallmon.sallmon_core.routes.blocks import router as blocks_router  # Routes for blocks
from sallmon.sallmon_core.routes.mempool import router as mempool_router  # Routes for mempool
from sallmon.sallmon_core.routes.peers import router as peers_router  # Routes for peers
from sallmon.sallmon_core.routes.utxo import router as utxo_router  # Routes for UTXOs
from sallmon.sallmon_core.routes.mine import router as mine_router  # Routes for mining

# Create the FastAPI application
app = FastAPI()

# Include all routers
app.include_router(api_router)  # Routes for the main API
app.include_router(blocks_router)  # Routes for blocks
app.include_router(mempool_router)  # Routes for mempool
app.include_router(peers_router)  # Routes for peer management
app.include_router(utxo_router)  # Routes for UTXOs
app.include_router(mine_router)  # Routes for mining

# Start the FastAPI server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=1339)
